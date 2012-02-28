import os

import buildbot
import buildbot.process.factory
from buildbot.steps.source import SVN
from buildbot.steps.shell import Configure, SetProperty
from buildbot.steps.shell import ShellCommand, WarningCountingShellCommand
from buildbot.process.properties import WithProperties

def getLLDBBuildFactory(triple, outOfDir=False, useTwoStage=False, jobs='%(jobs)s',
                        always_install=False, extra_configure_args=[],
                        env={}, *args, **kwargs):

    inDir = not outOfDir and not useTwoStage
    if inDir:
        llvm_srcdir = "llvm"
        llvm_objdir = "llvm"
    else:
        llvm_srcdir = "llvm.src"
        llvm_objdir = "llvm.obj"

    f = buildbot.process.factory.BuildFactory()

    # Determine the build directory.
    f.addStep(buildbot.steps.shell.SetProperty(name="get_builddir",
                                               command=["pwd"],
                                               property="builddir",
                                               description="set build dir",
                                               workdir="."))

    # We really want to revert the patched llvm/clang files but svn sometimes
    # doesn't do the right thing. We're left with removing and rebuilding.
    f.addStep(ShellCommand(name='rm-%s' % llvm_srcdir,
                           command=['rm', '-rf', llvm_srcdir],
                           haltOnFailure = True,
                           workdir='.', env=env))
    # Find out what version of llvm and clang are needed to build this version
    # of lldb. Right now we will assume they use the same version.
    # XXX - could this be done directly on the master instead of the slave?
    f.addStep(SetProperty(command='svn cat http://llvm.org/svn/llvm-project/lldb/trunk/scripts/build-llvm.pl | grep ^our.*llvm_revision | cut -d \\" -f 2',
                          property='llvmrev'))

    # The SVN build step provides no mechanism to check out a specific revision
    # based on a property, so just run the commands directly here.

    svn_co = ['svn', 'checkout', '--force']
    svn_co += ['--revision', WithProperties('%(llvmrev)s')]

    # build llvm svn checkout command
    svn_co_llvm = svn_co + \
     [WithProperties('http://llvm.org/svn/llvm-project/llvm/trunk@%(llvmrev)s'),
                     llvm_srcdir]
    # build clang svn checkout command
    svn_co_clang = svn_co + \
     [WithProperties('http://llvm.org/svn/llvm-project/cfe/trunk@%(llvmrev)s'),
                     '%s/tools/clang' % llvm_srcdir]

    f.addStep(ShellCommand(name='svn-llvm',
                           command=svn_co_llvm,
                           haltOnFailure=True,
                           workdir='.'))
    f.addStep(ShellCommand(name='svn-clang',
                           command=svn_co_clang,
                           haltOnFailure=True,
                           workdir='.'))

    f.addStep(SVN(name='svn-lldb',
                  mode='update',
                  baseURL='http://llvm.org/svn/llvm-project/lldb/',
                  defaultBranch='trunk',
                  always_purge=True,
                  workdir='%s/tools/lldb' % llvm_srcdir))

    # Patch llvm with lldb changes
    f.addStep(ShellCommand(name='patch.llvm',
        command='for i in tools/lldb/scripts/llvm*.diff; do echo "Patching with file $i"; patch -p0 -i $i; done',
        workdir=llvm_srcdir))

    # Patch clang with lldb changes
    f.addStep(ShellCommand(name='patch.clang',
        command='for i in ../lldb/scripts/clang*.diff; do echo "Patching with file $i"; patch -p0 -i $i; done',
        workdir='%s/tools/clang' % llvm_srcdir))

    # Run configure
    config_args = [WithProperties("%%(builddir)s/%s/configure" % llvm_srcdir),
                   "--disable-bindings",
                   "--without-llvmgcc",
                   "--without-llvmgxx",
                  ]
    if triple:
        config_args += ['--build=%s' % triple]
    config_args += extra_configure_args

    f.addStep(Configure(name='configure',
        command=config_args,
        workdir=llvm_objdir))

    f.addStep(WarningCountingShellCommand(name="compile",
                                          command=['nice', '-n', '10',
                                          'make', WithProperties("-j%s" % jobs)
                                          ],
                                          haltOnFailure=True,
                                          workdir=llvm_objdir))

    # The tests are hanging on Linux at the moment due to some "expect"
    # functionality not happening correctly. For now we will stub out the tests
    # so we can at least get builds running and reinstate the tests later.

    # Fixup file needed for tests
    # f.addStep(ShellCommand(name"copy-gnu_libstdcpp.py",
    #                       command="cp tools/lldb/examples/synthetic/gnu_libstdcpp.py Debug+Asserts/bin",
    #                       workdir=llvm_srcdir))

    # Test.
    #f.addStep(ShellCommand(name="test",
    #                       command=['nice', '-n', '10',
    #                                'make'],
    #                       haltOnFailure=True, description="test lldb",
    #                       env=env,
    #                       workdir='%s/tools/lldb/test' % llvm_objdir))

    return f
