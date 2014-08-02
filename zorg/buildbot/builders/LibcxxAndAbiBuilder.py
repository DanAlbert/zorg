import os

import buildbot
import buildbot.process.factory
import buildbot.steps.shell
import buildbot.steps.source as source
import buildbot.steps.source.svn as svn
import buildbot.process.properties as properties

import zorg.buildbot.commands.LitTestCommand as lit_test_command
import zorg.buildbot.util.artifacts as artifacts
import zorg.buildbot.util.phasedbuilderutils as phased_builder_utils

reload(lit_test_command)
reload(artifacts)
reload(phased_builder_utils)

def getLibcxxWholeTree(f, src_root):
    llvm_path = src_root
    llvm_url = 'http://llvm.org/svn/llvm-project/llvm/trunk'
    libcxx_url = 'http://llvm.org/svn/llvm-project/libcxx/trunk'
    libcxx_path = os.path.join(llvm_path, 'projects/libcxx')
    libcxxabi_url = 'http://llvm.org/svn/llvm-project/libcxxabi/trunk'
    libcxxabi_path = os.path.join(llvm_path, 'projects/libcxxabi')

    f = phased_builder_utils.SVNCleanupStep(f, source_path)
    f.addStep(SVN(name='svn-llvm',
                  mode='full',
                  baseURL='http://llvm.org/svn/llvm-project/llvm/',
                  defaultBranch='trunk',
                  workdir=llvm_path))
    f.addStep(SVN(name='svn-libcxx',
                  mode='full',
                  baseURL='http://llvm.org/svn/llvm-project/libcxx/',
                  defaultBranch='trunk',
                  workdir=libcxx_path))
    f.addStep(SVN(name='svn-libcxxabi',
                  mode='full',
                  baseURL='http://llvm.org/svn/llvm-project/libcxxabi/',
                  defaultBranch='trunk',
                  workdir=libcxxabi_path))
    return f

def getLibcxxAndAbiBuilder(f=None)
    if f is None:
        f = buildbot.process.factory.BuildFactory()
        # Find the build directory. We assume if f is passed in that the build
        # directory has already been found.
        f = phased_builder_utils.getBuildDir(f)

    # Grab the sources if we are not passed in any.
    src_root = 'llvm'
    build_path = os.path.join(src_root, 'build')
    f = getLibcxxWholeTree(f, src_root)

    # Grab the artifacts for our build.
    f = artifacts.GetCompilerArtifacts(f)
    host_compiler_dir = properties.WithProperties('%(builddir)s/host-compiler')
    f = artifacts.GetCCFromCompilerArtifacts(f, host_compiler_dir)
    f = artifacts.GetCXXFromCompilerArtifacts(f, host_compiler_dir)

    # Make build directory and run CMake
    CC = properties.WithProperties('%(cc_path)s')
    CXX = properties.WithProperties('%(cxx_path)s')

    build_path = os.path.join(source_path, 'build')
    f.addStep(buildbot.steps.shell.ShellCommand(
        name='make.builddir', command=['mkdir', build_path], haltOnFailure=True,
        workdir=source_path)

    f.addStep(buildbot.steps.shell.ShellCommand(
        name='cmake', command=[ 'cmake', '..' ], haltOnFailure=True,
        workdir=build_path, env={'CC': CC, 'CXX':, CXX}}))

    # Build libcxxabi
    f.addStep(buildbot.steps.shell.ShellCommand(
              name='build.libcxxabi', command=['make', 'cxxabi'],
              haltOnFailure=True, workdir=build_path))

    # Build libcxx
    f.addStep(buildbot.steps.shell.ShellCommand(
              name='build.libcxx', command=['make', 'cxx'],
              haltOnFailure=True, workdir=build_path))

    # Test libc++abi
    f.addStep(buildbot.steps.shell.ShellCommand(
            name='test.libcxxabi', command=[make, 'check-libcxxabi'],
            workdir=build_path))

    # Test libc++
    f.addStep(buildbot.steps.shell.ShellCommand(
            name='test.libcxxabi', command=[make, 'check-libcxxabi'],
            workdir=build_path))

    return f
