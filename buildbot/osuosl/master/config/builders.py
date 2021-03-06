from zorg.buildbot.builders import ClangBuilder
reload(ClangBuilder)
from zorg.buildbot.builders import ClangBuilder

from zorg.buildbot.builders import LLVMBuilder
reload(LLVMBuilder)
from zorg.buildbot.builders import LLVMBuilder

from zorg.buildbot.builders import LNTBuilder
reload(LNTBuilder)
from zorg.buildbot.builders import LNTBuilder

from zorg.buildbot.builders import NightlytestBuilder
reload(NightlytestBuilder)
from zorg.buildbot.builders import NightlytestBuilder

from zorg.buildbot.builders import PollyBuilder
reload(PollyBuilder)
from zorg.buildbot.builders import PollyBuilder

from zorg.buildbot.builders import LLDBBuilder
reload(LLDBBuilder)
from zorg.buildbot.builders import LLDBBuilder

from zorg.buildbot.builders import LLDBuilder
reload(LLDBBuilder)
from zorg.buildbot.builders import LLDBuilder

from zorg.buildbot.builders import ClangAndLLDBuilder
reload(ClangAndLLDBuilder)
from zorg.buildbot.builders import ClangAndLLDBuilder

from zorg.buildbot.builders import SanitizerBuilder
reload(SanitizerBuilder)
from zorg.buildbot.builders import SanitizerBuilder

from zorg.buildbot.builders import SanitizerBuilderII
reload(SanitizerBuilderII)
from zorg.buildbot.builders import SanitizerBuilderII

from zorg.buildbot.builders import Libiomp5Builder
reload(Libiomp5Builder)
from zorg.buildbot.builders import Libiomp5Builder

# Plain LLVM builders.
def _get_llvm_builders():
    return [
#        {'name': "llvm-x86_64-ubuntu",
#         'slavenames':["arxan_davinci"],
#         'builddir':"llvm-x86_64-ubuntu",
#         'factory': LLVMBuilder.getLLVMBuildFactory("x86_64-pc-linux-gnu", jobs=4,
#                                                    timeout=30)},
        {'name': "llvm-ppc64-linux1",
         'slavenames':["chinook"],
         'builddir':"llvm-ppc64",
         'factory': LLVMBuilder.getLLVMBuildFactory("ppc64-linux-gnu", jobs=2, clean=False, timeout=20)},

        {'name': "llvm-s390x-linux1",
         'slavenames':["systemz-1"],
         'builddir':"llvm-s390x-linux1",
         'factory': LLVMBuilder.getLLVMBuildFactory("s390x-linux-gnu", jobs=4, clean=False, timeout=20)},

        {'name': "llvm-x86_64-linux-vg_leak",
         'slavenames':["osu8"],
         'builddir':"llvm-x86_64-linux-vg_leak",
         'factory': LLVMBuilder.getLLVMBuildFactory("x86_64-pc-linux-gnu", valgrind=True,
                                             valgrindLeakCheck=True,
                                             valgrindSuppressions='utils/valgrind/x86_64-pc-linux-gnu.supp')},
        {'name': "llvm-mips-linux",
         'slavenames':["mipsswbrd002"],
         'builddir':"llvm-mips-linux",
         'factory': LLVMBuilder.getLLVMBuildFactory("mips-linux-gnu", timeout=40, config_name='Release+Asserts',
                                                    extra_configure_args=["--with-extra-options=-mips32r2",
                                                                          "CC=/mips/proj/build-compiler/clang-be-o32-latest/bin/clang",
                                                                          "CXX=/mips/proj/build-compiler/clang-be-o32-latest/bin/clang++",
                                                                          "--with-extra-ld-options=-mips32r2"])},
        {'name': "llvm-aarch64-linux",
         'slavenames':["aarch64-foundation"],
         'builddir':"llvm-aarch64-linux",
         'factory': LLVMBuilder.getLLVMBuildFactory(config_name='Release+Asserts',
                                                    outOfDir=True,
                                                    extra_configure_args=["--host=aarch64-linux-gnu"])},
        {'name': "llvm-hexagon-elf",
         'slavenames':["hexagon-build-03"],
         'builddir':"llvm-hexagon-elf",
         'factory': LLVMBuilder.getLLVMBuildFactory("hexagon-unknown-elf", timeout=40, config_name='Release+Asserts',
                                                       extra_configure_args=['--build=x86_64-linux-gnu',
                                                                             '--host=x86_64-linux-gnu',
                                                                             '--target=hexagon-unknown-elf',
                                                                             '--enable-targets=hexagon'])},
        ]

# Offline.
{'name': "llvm-x86_64-linux",
 'slavenames': ["gcc14"],
 'builddir': "llvm-x86_64",
 'factory': LLVMBuilder.getLLVMBuildFactory(triple="x86_64-pc-linux-gnu")},
{'name': "llvm-alpha-linux",
 'slavenames':["andrew1"],
 'builddir':"llvm-alpha",
 'factory': LLVMBuilder.getLLVMBuildFactory("alpha-linux-gnu", jobs=2)},
{'name': "llvm-i386-auroraux",
 'slavenames':["evocallaghan"],
 'builddir':"llvm-i386-auroraux",
 'factory': LLVMBuilder.getLLVMBuildFactory("i386-pc-auroraux", jobs="%(jobs)s", make='gmake')},
{'name': "llvm-ppc-linux",
 'slavenames':["nick1"],
 'builddir':"llvm-ppc",
 'factory': LLVMBuilder.getLLVMBuildFactory("ppc-linux-gnu", jobs=1, clean=False, timeout=40)},
{'name': "llvm-i686-linux",
 'slavenames': ["dunbar1"],
 'builddir': "llvm-i686",
 'factory': LLVMBuilder.getLLVMBuildFactory("i686-pc-linux-gnu", jobs=2, enable_shared=True)},

clang_i386_linux_xfails = [
    'LLC.MultiSource/Applications/oggenc/oggenc',
    'LLC.MultiSource/Benchmarks/VersaBench/bmm/bmm',
    'LLC.MultiSource/Benchmarks/VersaBench/dbms/dbms',
    'LLC.SingleSource/Benchmarks/Misc-C++/Large/sphereflake',
    'LLC.SingleSource/Regression/C++/EH/ConditionalExpr',
    'LLC_compile.MultiSource/Applications/oggenc/oggenc',
    'LLC_compile.MultiSource/Benchmarks/VersaBench/bmm/bmm',
    'LLC_compile.MultiSource/Benchmarks/VersaBench/dbms/dbms',
    'LLC_compile.SingleSource/Benchmarks/Misc-C++/Large/sphereflake',
    'LLC_compile.SingleSource/Regression/C++/EH/ConditionalExpr',
]

clang_x86_64_linux_xfails = [
    'LLC.SingleSource/UnitTests/Vector/SSE/sse.expandfft',
    'LLC.SingleSource/UnitTests/Vector/SSE/sse.stepfft',
    'LLC_compile.SingleSource/UnitTests/Vector/SSE/sse.expandfft',
    'LLC_compile.SingleSource/UnitTests/Vector/SSE/sse.stepfft',
]

# TODO: The following tests marked as expected failures on FreeBSD temporarily.
# Remove after http://llvm.org/bugs/show_bug.cgi?id=18089
# and http://llvm.org/bugs/show_bug.cgi?id=18056 will be fixed and closed.
clang_x86_64_freebsd_xfails = [
    'LLC.MultiSource/Benchmarks/SciMark2-C/scimark2',
    'LLC_compile.MultiSource/Benchmarks/SciMark2-C/scimark2',
    'LLC.MultiSource/Benchmarks/nbench/nbench',
    'LLC_compile.MultiSource/Benchmarks/nbench/nbench',
    'LLC.SingleSource/Benchmarks/Misc-C++/Large/sphereflake',
    'LLC_compile.SingleSource/Benchmarks/Misc-C++/Large/sphereflake',
    'LLC.SingleSource/UnitTests/ms_struct_pack_layout',
    'LLC_compile.SingleSource/UnitTests/ms_struct_pack_layout',

]

# Clang fast builders.
def _get_clang_fast_builders():
    return [
        {'name': "clang-x86_64-debian-fast",
         'slavenames':["gribozavr1"],
         'builddir':"clang-x86_64-debian-fast",
         'factory': ClangBuilder.getClangBuildFactory(
                    env={'PATH':'/home/llvmbb/bin/clang-latest/bin:/home/llvmbb/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin',
                         'CC': 'ccache clang', 'CXX': 'ccache clang++', 'CCACHE_CPP2': 'yes'},
                    stage1_config='Release+Asserts',
                    checkout_compiler_rt=True,
                    outOfDir=True)},

        {'name': "llvm-clang-lld-x86_64-debian-fast",
         'slavenames':["gribozavr1"],
         'builddir':"llvm-clang-lld-x86_64-debian-fast",
         'factory': ClangAndLLDBuilder.getClangAndLLDBuildFactory(
                    env={'PATH':'/home/llvmbb/bin/clang-latest/bin:/home/llvmbb/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin',
                         'CC': 'ccache clang', 'CXX': 'ccache clang++', 'CCACHE_CPP2': 'yes'})},

        {'name': "llvm-clang-lld-x86_64-ubuntu-13.04",
         'slavenames':["gribozavr2"],
         'builddir':"llvm-clang-lld-x86_64-ubuntu-13.04",
         'factory': ClangAndLLDBuilder.getClangAndLLDBuildFactory(
                    env={'PATH':'/home/llvmbb/bin/clang-latest/bin:/home/llvmbb/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin',
                         'CC': 'ccache clang', 'CXX': 'ccache clang++', 'CCACHE_CPP2': 'yes'})},

        {'name': "llvm-clang-lld-x86_64-centos-6.5",
         'slavenames':["gribozavr3"],
         'builddir':"llvm-clang-lld-x86_64-centos-6.5",
         'factory': ClangAndLLDBuilder.getClangAndLLDBuildFactory(
                    env={'PATH': '/opt/centos/devtoolset-1.1/root/usr/bin:/home/llvmbb/bin:/bin:/usr/bin',
                         'LD_LIBRARY_PATH': '/opt/centos/devtoolset-1.1/root/usr/lib64',
                         'CC': 'ccache clang', 'CXX': 'ccache clang++', 'CCACHE_CPP2': 'yes'},
                    withLLD=False,
                    extraCompilerOptions=['--gcc-toolchain=/opt/centos/devtoolset-1.1/root/usr'])},
        ]

# Clang builders.
def _get_clang_builders():

    return [
        {'name': "clang-atom-d525-fedora-rel",
         'slavenames':["atom1-buildbot"],
         'builddir':"clang-atom-d525-fedora-rel",
         'factory' : ClangBuilder.getClangBuildFactory(stage1_config='Release+Asserts')},

#        {'name': "clang-x86_64-ubuntu",
#         'slavenames':["arxan_raphael"],
#         'builddir':"clang-x86_64-ubuntu",
#         'factory' : ClangBuilder.getClangBuildFactory(extra_configure_args=['--enable-shared'])},

        {'name': "clang-native-arm-cortex-a9",
         'slavenames':["as-bldslv1", "as-bldslv2", "as-bldslv3"],
         'builddir':"clang-native-arm-cortex-a9",
         'factory' : ClangBuilder.getClangBuildFactory(
                     stage1_config='Release+Asserts',
                     clean=False,
                     env = { 'CXXFLAGS' : '-Wno-psabi', 'CFLAGS' : '-Wno-psabi'},
                     extra_configure_args=['--build=armv7l-unknown-linux-gnueabihf',
                                           '--host=armv7l-unknown-linux-gnueabihf',
                                           '--target=armv7l-unknown-linux-gnueabihf',
                                           '--with-cpu=cortex-a9',
                                           '--with-fpu=neon',
                                           '--with-float=hard',
                                           '--enable-targets=arm'])},

        {'name': "clang-native-arm-cortex-a15",
         'slavenames':["linaro-chrome-01"],
         'builddir':"clang-native-arm-cortex-a15",
         'factory' : ClangBuilder.getClangBuildFactory(
                     stage1_config='Release+Asserts',
                     clean=True,
                     test=True,
                     extra_configure_args=[ '--with-cpu=cortex-a15',
                                            '--with-fpu=neon',
                                            '--with-float=hard',
                                            '--enable-targets=arm'])},

        {'name': "clang-native-arm-cortex-a15-self-host",
         'slavenames':["linaro-chrome-02"],
         'builddir':"clang-native-arm-cortex-a15-self-host",
         'factory' : ClangBuilder.getClangBuildFactory(
                     stage1_config='Release+Asserts',
                     stage2_config='Release+Asserts',
                     useTwoStage=True,
                     clean=False,
                     test=True,
                     extra_configure_args=[ '--with-cpu=cortex-a15',
                                            '--with-fpu=neon',
                                            '--with-float=hard',
                                            '--enable-targets=arm'])},

        {'name' : "clang-native-arm-lnt",
         'slavenames':["linaro-chrome-03"],
         'builddir':"clang-native-arm-lnt",
         'factory' : LNTBuilder.getLNTFactory(triple='armv7l-unknown-linux-gnueabihf',
                                              nt_flags=['--cflag', '-mcpu=cortex-a15', '-j2'],
                                              jobs=2, use_pty_in_tests=True, clean=False,
                                              testerName='LNT-TestOnly-O3', run_cxx_tests=True)},

        {'name': "clang-native-mingw32-win7",
         'slavenames':["as-bldslv7"],
         'builddir':"clang-native-mingw32-win7",
         'factory' : ClangBuilder.getClangBuildFactory(triple='i686-pc-mingw32',
                                                       useTwoStage=True, test=False,
                                                       stage1_config='Release+Asserts',
                                                       stage2_config='Release+Asserts')},

        {'name' : "clang-ppc64-elf-linux",
         'slavenames' :["chinook-clangslave1"],
         'builddir' :"clang-ppc64-1",
         'factory' : LNTBuilder.getLNTFactory(triple='ppc64-elf-linux1',
                                              nt_flags=['--multisample=3','--cflag','-mcpu=native'],
                                              jobs=2,  use_pty_in_tests=True,
                                              testerName='O3-plain', run_cxx_tests=True)},

        {'name' : "clang-ppc64-elf-linux2",
         'slavenames' :["chinook-clangslave2"],
         'builddir' :"clang-ppc64-2",
         'factory' : ClangBuilder.getClangBuildFactory(triple='ppc64-elf-linux',
                                                       useTwoStage=True, test=True,
                                                       checkout_compiler_rt=True,
                                                       stage1_config='Release+Asserts',
                                                       stage2_config='Release+Asserts')},

         {'name': "clang-x86_64-linux-vg",
          'slavenames':["osu8"],
          'builddir':"clang-x86_64-linux-vg",
          'factory': ClangBuilder.getClangBuildFactory(valgrind=True)},

         {'name' : "clang-x86_64-linux-selfhost-rel",
          'slavenames' : ["osu8"],
          'builddir' : "clang-x86_64-linux-selfhost-rel",
          'factory' : ClangBuilder.getClangBuildFactory(triple='x86_64-pc-linux-gnu',
                                               useTwoStage=True,
                                               stage1_config='Release+Asserts',
                                               stage2_config='Release+Asserts')},

         {'name' : "clang-x86_64-linux-fnt",
          'slavenames' : ['osu8'],
          'builddir' : "clang-x86_64-linux-fnt",
          'factory' : NightlytestBuilder.getFastNightlyTestBuildFactory(triple='x86_64-pc-linux-gnu',
                                                               stage1_config='Release+Asserts',
                                                               test=False,
                                                               xfails=clang_x86_64_linux_xfails)},

         {'name': "clang-mergefunc-x86_64-freebsd",
          'slavenames':["as-bldslv5"],
         'builddir':"clang-mergefunc-x86_64-freebsd",
         'factory' : NightlytestBuilder.getFastNightlyTestBuildFactory(triple='x86_64-unknown-freebsd10.0',
                                                               stage1_config='Release+Asserts',
                                                               merge_functions=True,
                                                               make='gmake',
                                                               test=False,
                                                               env={'CC'  : '/usr/local/bin/gcc49',
                                                                    'CXX' : '/usr/local/bin/g++49'},
                                                               xfails=clang_x86_64_freebsd_xfails)},

        # Clang cross builders.
        {'name' : "clang-x86_64-darwin13-cross-mingw32",
         'slavenames' :["as-bldslv9"],
         'builddir' :"clang-x86_64-darwin13-cross-mingw32",
         'factory' : ClangBuilder.getClangBuildFactory(outOfDir=True, use_pty_in_tests=True,
                                                       test=False,
                                                       env = { 'CC' : 'clang',
                                                               'CXX' : 'clang++',
                                                               'CXXFLAGS' : '-stdlib=libc++'},
                                                       extra_configure_args=['--build=x86_64-apple-darwin13',
                                                                             '--host=x86_64-apple-darwin13',
                                                                             '--target=i686-pc-mingw32'])},

        {'name' : "clang-x86_64-darwin13-cross-arm",
         'slavenames' :["as-bldslv9"],
         'builddir' :"clang-x86_64-darwin13-cross-arm",
         'factory' : ClangBuilder.getClangBuildFactory(outOfDir=True, use_pty_in_tests=True,
                                                       env = { 'CC' : 'clang',
                                                               'CXX' : 'clang++',
                                                               'CXXFLAGS' : '-stdlib=libc++'},
                                                       test=False,
                                                       extra_configure_args=['--build=x86_64-apple-darwin13',
                                                                             '--host=x86_64-apple-darwin13',
                                                                             '--target=arm-eabi',
                                                                             '--enable-targets=arm'])},

        {'name' : "clang-x86_64-ubuntu-gdb-75",
         'slavenames' :["hpproliant1"],
         'builddir' :"clang-x86_64-ubuntu-gdb-75",
         'factory' : ClangBuilder.getClangBuildFactory(stage1_config='Release+Asserts', run_modern_gdb=True, clean=False)},

        {'name' : "clang-hexagon-elf",
         'slavenames' :["hexagon-build-03"],
         'builddir' :"clang-hexagon-elf",
         'factory' : ClangBuilder.getClangBuildFactory(
                     triple='x86_64-linux-gnu',
                     stage1_config='Release+Asserts',
                     extra_configure_args=['--enable-shared',
                                           '--target=hexagon-unknown-elf',
                                           '--enable-targets=hexagon'])},

        {'name' : "clang-aarch64-lnt",
         'slavenames' :["aarch64-qemu-lnt"],
         'builddir' :"clang-aarch64-lnt",
         'factory' : LNTBuilder.getLNTFactory(triple='aarch64-linux-gnu',
                                              nt_flags=['--llvm-arch=AArch64', '-j4'],
                                              package_cache="http://webkit.inf.u-szeged.hu/llvm/",
                                              jobs=4, use_pty_in_tests=True, clean=False,
                                              testerName='LNT-TestOnly-AArch64', run_cxx_tests=True)},
        {'name': "perf-x86_64-penryn-O3",
         'slavenames':["pollyperf2", "pollyperf3", "pollyperf4", "pollyperf5", "pollyperf15"],
         'builddir':"perf-x86_64-penryn-O3",
         'factory': PollyBuilder.getPollyLNTFactory(triple="x86_64-pc-linux-gnu",
                                                    nt_flags=['--multisample=10'],
                                                    reportBuildslave=False,
                                                    package_cache="http://parkas1.inria.fr/packages",
                                                    submitURL='http://llvm.org/perf/submitRun',
                                                    testerName='x86_64-penryn-O3')},
        ]

# Offline.
{'name': "clang-native-arm-cortex-a15",
 'slavenames':["linaro-chrome-01"],
 'builddir':"clang-native-arm-cortex-a15",
 'factory' : ClangBuilder.getClangBuildFactory(
             stage1_config='Release+Asserts',
             clean=False,
             env = { 'CXXFLAGS' : '-Wno-psabi', 'CFLAGS' : '-Wno-psabi'},
             extra_configure_args=['--build=armv7l-unknown-linux-gnueabihf',
                                   '--host=armv7l-unknown-linux-gnueabihf',
                                   '--target=armv7l-unknown-linux-gnueabihf',
                                   '--with-cpu=cortex-a15',
                                   '--with-fpu=neon',
                                   '--with-float=hard',
                                   '--enable-targets=arm'])},
{'name': "clang-i386-auroraux",
 'slavenames':["evocallaghan"],
 'builddir':"clang-i386-auroraux",
 'factory': ClangBuilder.getClangBuildFactory("i386-pc-auroraux",
                                              jobs="%(jobs)s", make='gmake')},
{'name': "clang-x86_64-linux",
 'slavenames':["gcc14"],
 'builddir':"clang-x86_64-linux",
 'factory': ClangBuilder.getClangBuildFactory(examples=True)},
{'name': "clang-i686-linux",
 'slavenames':["dunbar1"],
 'builddir':"clang-i686-linux",
 'factory': ClangBuilder.getClangBuildFactory()},
{'name': "clang-arm-linux",
 'slavenames':["nick3"],
 'builddir':"clang-arm-linux",
 'factory': ClangBuilder.getClangBuildFactory()},
{'name' : "clang-i686-darwin10",
 'slavenames' :["dunbar-darwin10"],
 'builddir' :"clang-i686-darwin10",
 'factory': ClangBuilder.getClangBuildFactory(triple='i686-apple-darwin10',
                                              stage1_config='Release')},
{'name' : "clang-i686-xp-msvc9",
 'slavenames' :['dunbar-win32-2'],
 'builddir' :"clang-i686-xp-msvc9",
 'factory' : ClangBuilder.getClangMSVCBuildFactory(jobs=2)},
{'name' : "clang-x86_64-darwin10-selfhost",
 'slavenames' : ["dunbar-darwin10"],
 'builddir' : "clang-x86_64-darwin10-selfhost",
 'factory' : ClangBuilder.getClangBuildFactory(triple='x86_64-apple-darwin10',
                                               useTwoStage=True,
                                               stage1_config='Release+Asserts',
                                               stage2_config='Debug+Asserts')},
{'name': "clang-i686-freebsd",
 'slavenames':["freebsd1"],
 'builddir':"clang-i686-freebsd",
 'factory': ClangBuilder.getClangBuildFactory(clean=True, use_pty_in_tests=True)},
{'name' : "clang-i686-linux-fnt",
 'slavenames' : ['balint1'],
 'builddir' : "clang-i686-linux-fnt",
 'factory' : NightlytestBuilder.getFastNightlyTestBuildFactory(triple='i686-pc-linux-gnu',
                                                               stage1_config='Release+Asserts',
                                                               test=False,
                                                               xfails=clang_i386_linux_xfails) },
{'name' : "clang-x86_64-darwin11-cross-linux-gnu",
 'slavenames' :["as-bldslv11"],
 'builddir' :"clang-x86_64-darwin11-cross-linux-gnu",
 'factory' : ClangBuilder.getClangBuildFactory(outOfDir=True, jobs=4,  use_pty_in_tests=True,
                                               run_cxx_tests=True,
                                               extra_configure_args=['--build=x86_64-apple-darwin11',
                                                                     '--host=x86_64-apple-darwin11',
                                                                     '--target=i686-pc-linux-gnu '])},
{'name': "clang-x86_64-debian",
 'slavenames':["gcc12"],
 'builddir':"clang-x86_64-debian",
 'factory': ClangBuilder.getClangBuildFactory(extra_configure_args=['--enable-shared'])},
{'name' : "clang-x86_64-debian-selfhost-rel",
 'slavenames' : ["gcc13"],
 'builddir' : "clang-x86_64-debian-selfhost-rel",
 'factory' : ClangBuilder.getClangBuildFactory(triple='x86_64-pc-linux-gnu',
                                                useTwoStage=True,
                                                stage1_config='Release+Asserts',
                                                stage2_config='Release+Asserts')},
{'name' : "clang-x86_64-debian-fnt",
 'slavenames' : ['gcc20'],
 'builddir' : "clang-x86_64-debian-fnt",
 'factory' : NightlytestBuilder.getFastNightlyTestBuildFactory(triple='x86_64-pc-linux-gnu',
                                                               stage1_config='Release+Asserts',
                                                               test=False,
                                                               xfails=clang_x86_64_linux_xfails)},
{'name': "clang-x86_64-darwin11-self-mingw32",
 'slavenames':["as-bldslv11"],
 'builddir':"clang-x86_64-darwin11-self-mingw32",
 'factory' : ClangBuilder.getClangBuildFactory(outOfDir=True, jobs=4, test=False,
                                                       env = { 'PATH' : "/mingw_build_tools/install_with_gcc/bin:/opt/local/bin:/opt/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/usr/X11/bin",
                                                               'CC' : 'clang',
                                                               'CXX' : 'clang++',
                                                               'CXXFLAGS' : '-stdlib=libc++'},
                                                       extra_configure_args=['--build=x86_64-apple-darwin11',
                                                                             '--host=i686-pc-mingw32',
                                                                             '--target=i686-pc-mingw32'])},
{'name': "clang-X86_64-freebsd",
 'slavenames':["as-bldslv6"],
 'builddir':"clang-X86_64-freebsd",
 'factory': NightlytestBuilder.getFastNightlyTestBuildFactory(triple='x86_64-unknown-freebsd8.2',
                                                              stage1_config='Release+Asserts',
                                                              test=True)},

# Polly builders.
def _get_polly_builders():
    return [
        {'name': "polly-amd64-linux",
         'slavenames':["grosser1"],
         'builddir':"polly-amd64-linux",
         'factory': PollyBuilder.getPollyBuildFactory()},

        {'name': "perf-x86_64-penryn-O3-polly",
         'slavenames':["pollyperf6"],
         'builddir':"perf-x86_64-penryn-O3-polly",
         'factory': PollyBuilder.getPollyLNTFactory(triple="x86_64-pc-linux-gnu",
                                                    nt_flags=['--multisample=10', '--mllvm=-polly'],
                                                    reportBuildslave=False,
                                                    package_cache="http://parkas1.inria.fr/packages",
                                                    submitURL='http://llvm.org/perf/submitRun',
                                                    testerName='x86_64-penryn-O3-polly')},
        {'name': "perf-x86_64-penryn-O3-polly-codegen-isl",
         'slavenames':["pollyperf7"],
         'builddir':"pollyperf-O3-polly-codegen-isl",
         'factory': PollyBuilder.getPollyLNTFactory(triple="x86_64-pc-linux-gnu",
                                                    nt_flags=['--multisample=10', '--mllvm=-polly', '--mllvm=-polly-code-generator=isl'],
                                                    reportBuildslave=False,
                                                    package_cache="http://parkas1.inria.fr/packages",
                                                    submitURL='http://llvm.org/perf/submitRun',
                                                    testerName='x86_64-penryn-O3-polly-codegen-isl')},
        {'name': "perf-x86_64-penryn-O3-polly-scev",
         'slavenames':["pollyperf10"],
         'builddir':"perf-x86_64-penryn-O3-polly-scev",
         'factory': PollyBuilder.getPollyLNTFactory(triple="x86_64-pc-linux-gnu",
                                                    nt_flags=['--multisample=10', '--mllvm=-polly', '--mllvm=-polly-codegen-scev'],
                                                    reportBuildslave=False,
                                                    package_cache="http://parkas1.inria.fr/packages",
                                                    submitURL='http://llvm.org/perf/submitRun',
                                                    testerName='x86_64-penryn-O3-polly-scev')},
        {'name': "perf-x86_64-penryn-O3-polly-scev-codegen-isl",
         'slavenames':["pollyperf11"],
         'builddir':"perf-x86_64-penryn-O3-polly-svev-codegen-isl",
         'factory': PollyBuilder.getPollyLNTFactory(triple="x86_64-pc-linux-gnu",
                                                    nt_flags=['--multisample=10', '--mllvm=-polly', '--mllvm=-polly-code-generator=isl', '--mllvm=-polly-codegen-scev'],
                                                    reportBuildslave=False,
                                                    package_cache="http://parkas1.inria.fr/packages",
                                                    submitURL='http://llvm.org/perf/submitRun',
                                                    testerName='x86_64-penryn-polly-scev-codegen-isl')},
        {'name': "perf-x86_64-penryn-O3-polly-detect",
         'slavenames':["pollyperf14"],
         'builddir':"perf-x86_64-penryn-O3-polly-detect",
         'factory': PollyBuilder.getPollyLNTFactory(triple="x86_64-pc-linux-gnu",
                                                    nt_flags=['--multisample=10', '--mllvm=-polly', '--mllvm=-polly-code-generator=none', '--mllvm=-polly-optimizer=none', '--mllvm=-polly-run-dce=false'],
                                                    reportBuildslave=False,
                                                    package_cache="http://parkas1.inria.fr/packages",
                                                    submitURL='http://llvm.org/perf/submitRun',
                                                    testerName='x86_64-penryn-O3-polly-detect')}
       ]

# Offline.
{'name': "polly-intel32-linux",
 'slavenames':["botether"],
 'builddir':"polly-intel32-linux",
 'factory': PollyBuilder.getPollyBuildFactory()},

# LLDB builders.
def _get_lldb_builders():

#   gcc_m32_latest_env = gcc_latest_env.copy()
#   gcc_m32_latest_env['CC'] += ' -m32'
#   gcc_m32_latest_env['CXX'] += ' -m32'
#
    return [
        {'name': "lldb-x86_64-debian-clang",
         'slavenames': ["gribozavr1"],
         'builddir': "lldb-x86_64-clang",
         'factory': LLDBBuilder.getLLDBBuildFactory(triple=None, # use default
                                                    extra_configure_args=['--enable-cxx11', '--enable-optimized', '--enable-assertions'],
                                                    env={'PATH':'/home/llvmbb/bin/clang-latest/bin:/home/llvmbb/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games'})},

        {'name': "lldb-x86_64-darwin12",
         'slavenames': ["lab-mini-02"],
         'builddir': "build.lldb-x86_64-darwin12",
         'factory': LLDBBuilder.getLLDBxcodebuildFactory()},

        {'name': "lldb-x86_64-freebsd",
         'slavenames': ["as-bldslv5"],
         'builddir': "lldb-x86_64-freebsd",
         'factory': LLDBBuilder.getLLDBBuildFactory(triple=None, # use default
                                                    make='gmake',
                                                    extra_configure_args=['--enable-cxx11', '--enable-optimized', '--enable-assertions'])},
       ]

# Offline.
{'name': "lldb-x86_64-linux",
 'slavenames': ["gcc20"],
 'builddir': "lldb-x86_64",
 'factory': LLDBBuilder.getLLDBBuildFactory(triple="x86_64-pc-linux-gnu",
                                            env={'CXXFLAGS' : '-std=c++0x'})},
#{'name': "lldb-i686-debian",
# 'slavenames': ["gcc15"],
# 'builddir': "lldb-i686-debian",
# 'factory': LLDBBuilder.getLLDBBuildFactory(triple="i686-pc-linux-gnu",
#                                            env=gcc_m32_latest_env)}

# LLD builders.
def _get_lld_builders():
    return [
        {'name': "lld-x86_64-darwin13",
         'slavenames' :["as-bldslv9"],
         'builddir':"lld-x86_64-darwin13",
         'factory': LLDBuilder.getLLDBuildFactory(),
         'category'   : 'lld'},

        {'name': "lld-x86_64-win7",
         'slavenames' :["as-bldslv4"],
         'builddir':"lld-x86_64-win7",
         'factory': LLDBuilder.getLLDWinBuildFactory(),
         'category'   : 'lld'},

        {'name': "lld-x86_64-freebsd",
         'slavenames' :["as-bldslv5"],
         'builddir':"lld-x86_64-freebsd",
         'factory': LLDBuilder.getLLDBuildFactory(jobs=32,
                                                  extra_configure_args=[
                                                      '-DCMAKE_EXE_LINKER_FLAGS=-lcxxrt',
                                                      '-DLLVM_ENABLE_WERROR=OFF'],
                                                  env={'CXXFLAGS' : "-std=c++11 -stdlib=libc++"}),
         'category'   : 'lld'},

         ]

# Sanitizer builders.
def _get_sanitizer_builders():
      return [
          {'name': "sanitizer-x86_64-linux",
           'slavenames' :["sanitizer-buildbot1"],
           'builddir': "sanitizer-x86_64-linux",
           'factory': SanitizerBuilder.getSanitizerBuildFactory()},

          {'name': "sanitizer-x86_64-linux-bootstrap",
           'slavenames' :["sanitizer-buildbot2"],
           'builddir': "sanitizer-x86_64-linux-bootstrap",
           'factory': SanitizerBuilder.getSanitizerBuildFactory()},

          #{'name': "llvm-clang-lld-x86_64-ubuntu-sanitize-address",
          # 'slavenames':["hexagon-build-03"],
          # 'builddir':"llvm-clang-lld-x86_64-ubuntu-sanitize-address",
          # 'factory': ClangAndLLDBuilder.getClangAndLLDBuildFactory(
          #                                   buildWithSanitizerOptions=['-fsanitize=address'],
          #                                   env={'PATH':'/usr/local/bin:/usr/bin:/bin'})},

          {'name': "sanitizer_x86_64-freebsd",
           'slavenames':["as-bldslv5"],
           'builddir':"sanitizer_x86_64-freebsd",
           'factory' : SanitizerBuilderII.getSanitizerBuildFactoryII(
                                          clean=True,
                                          sanitizers=['sanitizer','lsan','msan','tsan','ubsan','dfsan'],
                                          common_cmake_options='-DCMAKE_EXE_LINKER_FLAGS=-lcxxrt')},

          {'name': "sanitizer-ppc64-linux1",
           'slavenames' :["sanitizer-ppc64-1"],
           'builddir': "sanitizer-ppc64-1",
           'factory': SanitizerBuilder.getSanitizerBuildFactory()},

          ]

def _get_openmp_builders():
    return [
        {'name': "libiomp5-gcc-x86_64-linux-debian",
         'slavenames':["gribozavr4"],
         'builddir':"libiomp5-gcc-x86_64-linux-debian",
         'factory' : Libiomp5Builder.getLibiomp5BuildFactory(
                         buildcompiler="gcc",
                         env={'PATH':'/home/llvmbb/bin/clang-latest/bin:/home/llvmbb/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin'}),
         'category' : 'libiomp5'},

        {'name': "libiomp5-clang-x86_64-linux-debian",
         'slavenames':["gribozavr4"],
         'builddir':"libiomp5-clang-x86_64-linux-debian",
         'factory' : Libiomp5Builder.getLibiomp5BuildFactory(
                         buildcompiler="clang",
                         env={'PATH':'/home/llvmbb/bin/clang-latest/bin:/home/llvmbb/bin:/usr/local/bin:/usr/local/bin:/usr/bin:/bin'}),
         'category' : 'libiomp5'},
        ]


# Experimental and stopped builders
def _get_experimental_builders():
    return [
        {'name': "llvm-ppc64-linux2",
         'slavenames':["coho"],
         'builddir':"llvm-ppc64-2",
         'factory': LLVMBuilder.getLLVMBuildFactory("ppc64-linux-gnu", jobs=2, clean=False, timeout=20),
         'category' : 'llvm'},

        {'name': "clang-atom-d525-fedora",
         'slavenames':["atom-buildbot"],
         'builddir':"clang-atom-d525-fedora",
         'factory' : ClangBuilder.getClangBuildFactory(extra_configure_args=['--enable-shared']),
         'category' : 'clang'},

        {'name': "clang-amd64-openbsd",
         'slavenames':["openbsd-buildslave"],
         'builddir':"clang-openbsd",
         'factory' : ClangBuilder.getClangBuildFactory(stage1_config='Release+Asserts'),
         'category' : 'clang'},
        ]

def get_builders():
    for b in _get_llvm_builders():
        b['category'] = 'llvm'
        yield b

    for b in _get_clang_fast_builders():
        b['category'] = 'clang_fast'
        yield b

    for b in _get_clang_builders():
        b['category'] = 'clang'
        yield b

    for b in _get_polly_builders():
        b['category'] = 'polly'
        yield b

    for b in _get_lld_builders():
        b['category'] = 'lld'
        yield b

    for b in _get_lldb_builders():
        b['category'] = 'lldb'
        yield b

    for b in _get_sanitizer_builders():
        b['category'] = 'sanitizer'
        yield b

    for b in _get_openmp_builders():
        b['category'] = 'openmp'
        yield b

    for b in _get_experimental_builders():
        yield b

# Random other unused builders...
{'name': "clang-x86_64-openbsd",
 'slavenames':["ocean1"],
 'builddir':"clang-x86_64-openbsd",
 'factory': ClangBuilder.getClangBuildFactory(),
 'category':'clang.exp'},
{'name': "clang-x86_64-linux-checks",
 'slavenames':["osu2"],
 'builddir':"clang-x86_64-linux-checks",
 'factory': ClangBuilder.getClangBuildFactory(stage1_config='Debug+Asserts+Checks'),
 'category':'clang.exp'},
{'name' : "clang-i386-darwin10-selfhost-rel",
 'slavenames' : ["dunbar-darwin10"],
 'builddir' : "clang-i386-darwin10-selfhost-rel",
 'factory' : ClangBuilder.getClangBuildFactory(triple='i386-apple-darwin10',
                                               useTwoStage=True,
                                               stage1_config='Release+Asserts',
                                               stage2_config='Release+Asserts'),
 'category' : 'clang.exp' },
{'name' : "clang-x86_64-darwin10-selfhost-rel",
 'slavenames' : ["dunbar-darwin10"],
 'builddir' : "clang-x86_64-darwin10-selfhost-rel",
 'factory' : ClangBuilder.getClangBuildFactory(triple='x86_64-apple-darwin10',
                                               useTwoStage=True,
                                               stage1_config='Release+Asserts',
                                               stage2_config='Release+Asserts'),
 'category' : 'clang.exp' },
{'name' : "clang-i686-xp-msvc9_alt",
 'slavenames' :['adobe1'],
 'builddir' :"clang-i686-xp-msvc9_alt",
 'factory' : ClangBuilder.getClangMSVCBuildFactory(jobs=2),
 'category' : 'clang.exp' },
{'name': "clang-i686-freebsd-selfhost-rel",
 'slavenames':["freebsd1"],
 'builddir':"clang-i686-freebsd-selfhost-rel",
 'factory': ClangBuilder.getClangBuildFactory(triple='i686-pc-freebsd',
                                              useTwoStage=True,
                                              stage1_config='Release+Asserts',
                                              stage2_config='Release+Asserts'),
 'category' : 'clang.exp' },
{'name': "llvm-x86_64-debian-debug-werror",
 'slavenames':["obbligato-ellington"],
 'builddir':"llvm-x86-64-debian-debug-werror",
 'factory': LLVMBuilder.getLLVMBuildFactory("x86_64-pc-linux-gnu",
                                            config_name='Debug+Asserts',
                                            extra_configure_args=["--enable-werror"]),
 'category' : 'llvm'},
{'name': "llvm-x86_64-debian-release-werror",
 'slavenames':["obbligato-ellington"],
 'builddir':"llvm-x86-64-debian-release-werror",
 'factory': LLVMBuilder.getLLVMBuildFactory("x86_64-pc-linux-gnu",
                                            config_name='Release+Asserts',
                                            extra_configure_args=["--enable-werror"]),
 'category' : 'llvm'},
{'name': "clang-x86_64-debian-debug-werror",
 'slavenames':["obbligato-ellington"],
 'builddir':"clang-x86-64-debian-debug-werror",
 'factory': ClangBuilder.getClangBuildFactory(triple="x86_64-pc-linux-gnu",
                                             useTwoStage=True,
                                             stage1_config='Debug+Asserts',
                                             stage2_config='Debug+Asserts',
                                             extra_configure_args=["--enable-werror"]),
 'category' : 'clang'},
# Cortex-A9 check-all self-host
{'name': "clang-native-arm-cortex-a9-self-host",
 'slavenames':["linaro-panda-02"],
 'builddir':"clang-native-arm-cortex-a9-self-host",
 'factory' : ClangBuilder.getClangBuildFactory(
             stage1_config='Release+Asserts',
             stage2_config='Release+Asserts',
             useTwoStage=True,
             clean=False,
             test=True,
             extra_configure_args=[ '--with-cpu=cortex-a9',
                                    '--with-fpu=neon',
                                    '--with-float=hard',
                                    '--enable-targets=arm']),
 'category' : 'clang'},
{'name': "clang-x86_64-debian-release-werror",
 'slavenames':["obbligato-ellington"],
 'builddir':"clang-x86-64-debian-release-werror",
 'factory': ClangBuilder.getClangBuildFactory(triple="x86_64-pc-linux-gnu",
                                             useTwoStage=True,
                                             stage1_config='Release+Asserts',
                                             stage2_config='Release+Asserts',
                                             extra_configure_args=["--enable-werror"]),
 'category' : 'clang'},
{'name': "clang-native-mingw64-win7",
 'slavenames':["sschiffli1"],
 'builddir':"clang-native-mingw64-win7",
 'factory' : ClangBuilder.getClangMinGWBuildFactory(),
 'category' : 'clang'},
LabPackageCache = 'http://10.1.1.2/packages/'
{'name' : "clang-x86_64-darwin12-nt-O3-vectorize",
 'slavenames' :["lab-mini-03"],
 'builddir' :"clang-x86_64-darwin12-nt-O3-vectorize",
 'factory' : LNTBuilder.getLNTFactory(triple='x86_64-apple-darwin12',
                                      nt_flags=['--mllvm=-vectorize', '--multisample=3'], jobs=2,
                                      use_pty_in_tests=True, testerName='O3-vectorize',
                                      run_cxx_tests=True, package_cache=LabPackageCache),
 'category' : 'clang'},
{'name' : "clang-x86_64-darwin10-nt-O0-g",
 'slavenames' :["lab-mini-03"],
 'builddir' :"clang-x86_64-darwin10-nt-O0-g",
 'factory' : LNTBuilder.getLNTFactory(triple='x86_64-apple-darwin10',
                                      nt_flags=['--multisample=3', 
                                                '--optimize-option',
                                                '-O0', '--cflag', '-g'],
                                      jobs=2,  use_pty_in_tests=True,
                                      testerName='O0-g', run_cxx_tests=True,
                                      package_cache=LabPackageCache),
 'category' : 'clang'},
{'name' : "clang-x86_64-darwin12-gdb",
 'slavenames' :["lab-mini-04"],
 'builddir' :"clang-x86_64-darwin12-gdb",
 'factory' : ClangBuilder.getClangBuildFactory(triple='x86_64-apple-darwin12', stage1_config='Release+Asserts', run_gdb=True),
 'category' : 'clang'},
{'name': "llvm-ppc-darwin",
 'slavenames':["arxan_bellini"],
 'builddir':"llvm-ppc-darwin",
 'factory': LLVMBuilder.getLLVMBuildFactory("ppc-darwin", jobs=2, clean=True,
                    config_name = 'Release',
                    env = { 'CC' : "/usr/bin/gcc-4.2",
                            'CXX': "/usr/bin/g++-4.2" },
                    extra_configure_args=['--enable-shared'],
                    timeout=600),
 'category' : 'llvm'},
