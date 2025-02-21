import sh
import os
import time

from multiprocessing import cpu_count
from pathlib import Path
from os.path import join

from pythonforandroid.logger import shprint
from pythonforandroid.recipe import Recipe
from pythonforandroid.util import (
    BuildInterruptingException,
    current_directory,
    ensure_dir,
)
from pythonforandroid.prerequisites import OpenSSLPrerequisite

HOSTPYTHON_VERSION_UNSET_MESSAGE = (
    'The hostpython recipe must have set version'
)

SETUP_DIST_NOT_FIND_MESSAGE = (
    'Could not find Setup.dist or Setup in Python build'
)


class HostPython3Recipe(Recipe):
    '''
    The hostpython3's recipe.

    .. versionchanged:: 2019.10.06.post0
        Refactored from deleted class ``python.HostPythonRecipe`` into here.

    .. versionchanged:: 0.6.0
        Refactored into  the new class
        :class:`~pythonforandroid.python.HostPythonRecipe`
    '''

    version = '3.11.5'
    name = 'hostpython3'

    build_subdir = 'native-build'
    '''Specify the sub build directory for the hostpython3 recipe. Defaults
    to ``native-build``.'''

    url = 'https://www.python.org/ftp/python/{version}/Python-{version}.tgz'
    '''The default url to download our host python recipe. This url will
    change depending on the python version set in attribute :attr:`version`.'''

    patches = ['patches/pyconfig_detection.patch']

    @property
    def _exe_name(self):
        '''
        Returns the name of the python executable depending on the version.
        '''
        if not self.version:
            raise BuildInterruptingException(HOSTPYTHON_VERSION_UNSET_MESSAGE)
        return f'python{self.version.split(".")[0]}'

    @property
    def python_exe(self):
        '''Returns the full path of the hostpython executable.'''
        return join(self.get_path_to_python(), self._exe_name)

    def get_recipe_env(self, arch=None):
        #env = os.environ.copy()
        env = {'__CFBundleIdentifier': 'com.apple.Terminal', 'TMPDIR': '/var/folders/ny/9ct_l4gs3ll27rkt3stsm2qm0000gn/T/', 'XPC_FLAGS': '0x0', 'LaunchInstanceID': '6B9846DB-C326-47F9-BB79-90B716DBD6D1', 'TERM': 'xterm-256color', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.CWx1XS1gEv/Listeners', 'SECURITYSESSIONID': '186b1', 'XPC_SERVICE_NAME': '0', 'TERM_PROGRAM': 'Apple_Terminal', 'TERM_PROGRAM_VERSION': '453', 'TERM_SESSION_ID': 'F2EAEB84-B46A-408F-AB35-B8FDFD7FC395', 'SHELL': '/bin/zsh', 'HOME': '/Users/tobiaslindell', 'LOGNAME': 'tobiaslindell', 'USER': 'tobiaslindell', 'PATH': '/Users/tobiaslindell/.buildozer/android/platform/apache-ant-1.9.4/bin:/Users/tobiaslindell/.local/share/virtualenvs/appStuff-YE0LHSod/bin:/Users/tobiaslindell/.local/share/virtualenvs/appStuff-YE0LHSod/bin:/usr/local/openssl-1.1/bin:/usr/local/jdk-17/jdk-17.0.14.jdk/Contents/Home/bin:/usr/local/bin:/Users/tobiaslindell/.cargo/bin:/opt/homebrew/opt/lld/bin:/opt/homebrew/bin:/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin:/Users/tobiaslindell/Library/Android/sdk/platform-tools:/Users/tobiaslindell/Library/Android/sdk/emulator:/Users/tobiaslindell/Library/Android/sdk/cmdline-tools/latest/bin:/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin:/usr/local/openssl-1.1/bin:/usr/local/jdk-17/jdk-17.0.14.jdk/Contents/Home/bin:/usr/local/bin:/Users/tobiaslindell/perl5/bin:/Users/tobiaslindell/.cargo/bin:/opt/homebrew/opt/lld/bin:/opt/homebrew/bin:/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin:/Users/tobiaslindell/Library/Android/sdk/platform-tools:/Users/tobiaslindell/Library/Android/sdk/emulator:/Users/tobiaslindell/Library/Android/sdk/cmdline-tools/latest/bin:/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/Library/Apple/usr/bin', 'SHLVL': '2', 'PWD': '/Users/tobiaslindell/appStuff', 'OLDPWD': '/Users/tobiaslindell/appStuff', 'ANDROID_NDK_HOME': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393', 'NDK_PROJECT_PATH': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393', 'TARGET': 'aarch64-linux-android', 'API': '21', 'CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin/clang', 'ANDROID_HOME': '/Users/tobiaslindell/Library/Android/sdk', 'CARGO_BUILD_TARGET': 'aarch64-linux-android', 'NDK_ROOT': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin', 'TOOLCHAIN': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64', 'SYSROOT': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/sysroot', 'CARGO_TARGET_AARCH64_LINUX_ANDROID_AR': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android-ar', 'PKG_CONFIG_SYSROOT_DIR': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/sysroot', 'PKG_CONFIG_PATH': '/usr/local/openssl-1.1/lib/pkgconfig:/opt/homebrew/opt/zlib/lib/pkgconfig:/opt/homebrew/opt/bzip2/lib/pkgconfig:/opt/homebrew/opt/libffi/lib/pkgconfig:/opt/homebrew/opt/expat/lib/pkgconfig: /opt/homebrew/opt/lld/lib/pkgconfig', 'PKG_CONFIG_LIBDIR': '/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/pkgconfig:/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/share/pkgconfig', 'OPENSSL_DIR': '/Users/tobiaslindell/Downloads/localStuff/openssl-android/usr/local', 'PKG_CONFIG': '/Users/tobiaslindell/appStuff/pkg-config-wrapper', 'PYO3_CROSS': '1', 'PYO3_CROSS_LIB_DIR': '/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_21/python3/android-build', 'PYO3_CROSS_PYTHON_VERSION': '3.11', 'LDFLAGS': '-L/opt/homebrew/opt/zlib/lib -L/opt/homebrew/opt/bzip2/lib -L/usr/local/openssl-1.1/lib -L/opt/homebrew/opt/libffi/lib -L/opt/homebrew/opt/binutils/lib -L/usr/local/opt/expat/lib -L/opt/homebrew/opt/lld/lib', 'CPPFLAGS': '-I/opt/homebrew/opt/zlib/include -I/opt/homebrew/opt/bzip2/include -I/usr/local/openssl-1.1/include -I/opt/homebrew/opt/libffi/include -I/opt/homebrew/opt/binutils/include -I/usr/local/opt/expat/include -I/opt/homebrew/opt/lld/include', 'PERL5LIB': '/Users/tobiaslindell/perl5/lib/perl5', 'PERL_LOCAL_LIB_ROOT': '/Users/tobiaslindell/perl5', 'PERL_MB_OPT': '--install_base "/Users/tobiaslindell/perl5"', 'PERL_MM_OPT': 'INSTALL_BASE=/Users/tobiaslindell/perl5', 'SSL_CERT_FILE': '/usr/local/lib/python3.11/site-packages/certifi/cacert.pem', 'JAVA_HOME': '/usr/local/jdk-17/jdk-17.0.14.jdk/Contents/Home', 'OPENSSL_HOME': '/usr/local/openssl-1.1', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 'PIP_DISABLE_PIP_VERSION_CHECK': '1', 'PYTHONDONTWRITEBYTECODE': '1', 'PIP_PYTHON_PATH': '/Users/tobiaslindell/.local/share/virtualenvs/appStuff-YE0LHSod/bin/python', 'PIPENV_ACTIVE': '1', 'VIRTUAL_ENV': '/Users/tobiaslindell/.local/share/virtualenvs/appStuff-YE0LHSod', 'VIRTUAL_ENV_PROMPT': 'appStuff', 'PS1': '(appStuff) %n@%m %1~ %# ', 'LANG': 'en_US.UTF-8', 'LC_CTYPE': 'UTF-8', '_': '/usr/local/bin/pipenv', 'PACKAGES_PATH': '/Users/tobiaslindell/.buildozer/android/packages', 'ANDROIDSDK': '/Users/tobiaslindell/.buildozer/android/platform/android-sdk', 'ANDROIDNDK': '/Users/tobiaslindell/.buildozer/android/platform/android-ndk-r25b', 'ANDROIDAPI': '33', 'ANDROIDMINAPI': '21', 'VERSION_hostpython3': '3.11.5', 'VERSION_python3': '3.11.5', 'VERSION_kivy': '2.3.1', 'VERSION_setuptools': '75.8.0', 'VERSION_cffi': '1.15.1', 'VERSION_semantic_version': '2.10.0', 'VERSION_setuptools_rust': '1.10.2', 'VERSION_cryptography': '38.0.1', 'VERSION_pyrebase4': '4.8.0', 'VERSION_filetype': '1.2.0', 'VERSION_urllib3': '1.26.20', 'VERSION_oauth2client': '4.1.3', 'VERSION_httplib2': '0.22.0', 'VERSION_pyparsing': '3.2.1', 'VERSION_pyasn1': '0.6.1', 'VERSION_pyasn1_modules': '0.4.1', 'VERSION_rsa': '4.9', 'VERSION_gcloud': '0.18.3', 'VERSION_googleapis-common-protos': '1.66.0', 'VERSION_protobuf': '5.29.3', 'VERSION_requests-toolbelt': '0.10.1', 'VERSION_python-jwt': '4.1.0', 'VERSION_jwcrypto': '1.4.2', 'VERSION_pycparser': '2.22', 'VERSION_deprecated': '1.2.18', 'VERSION_wrapt': '1.17.2', 'VERSION_pycryptodome': '3.21.0'}
        print("")
        print(f" - - - - - - - - - -  HOSTPYTHON3 - - - - - - - - - - ")
        #print(f"env:")
        #print(f"{env}")
        #print("")
        openssl_prereq = OpenSSLPrerequisite()
        if env.get("PKG_CONFIG_PATH", ""):
            env["PKG_CONFIG_PATH"] = os.pathsep.join(
                [openssl_prereq.pkg_config_location, env["PKG_CONFIG_PATH"]]
            )
        else:
            env["PKG_CONFIG_PATH"] = openssl_prereq.pkg_config_location
        return env

    def should_build(self, arch):
        if Path(self.python_exe).exists():
            # no need to build, but we must set hostpython for our Context
            self.ctx.hostpython = self.python_exe
            return False
        return True

    def get_build_container_dir(self, arch=None):
        choices = self.check_recipe_choices()
        dir_name = '-'.join([self.name] + choices)
        return join(self.ctx.build_dir, 'other_builds', dir_name, 'desktop')

    def get_build_dir(self, arch=None):
        '''
        .. note:: Unlike other recipes, the hostpython build dir doesn't
            depend on the target arch
        '''
        return join(self.get_build_container_dir(), self.name)

    def get_path_to_python(self):
        return join(self.get_build_dir(), self.build_subdir)

    def build_arch(self, arch):
        
        #time.sleep(60)
        
        env = self.get_recipe_env(arch)

        recipe_build_dir = self.get_build_dir(arch.arch)

        # Create a subdirectory to actually perform the build
        build_dir = join(recipe_build_dir, self.build_subdir)
        ensure_dir(build_dir)

        # Configure the build
        with current_directory(build_dir):
            if not Path('config.status').exists():
                shprint(sh.Command(join(recipe_build_dir, 'configure')), _env=env)
                #shprint(sh.Command('./configure'), '--host=aarch64-linux-android', _env=env)

        with current_directory(recipe_build_dir):
            # Create the Setup file. This copying from Setup.dist is
            # the normal and expected procedure before Python 3.8, but
            # after this the file with default options is already named "Setup"
            setup_dist_location = join('Modules', 'Setup.dist')
            if Path(setup_dist_location).exists():
                shprint(sh.cp, setup_dist_location,
                        join(build_dir, 'Modules', 'Setup'))
            else:
                # Check the expected file does exist
                setup_location = join('Modules', 'Setup')
                if not Path(setup_location).exists():
                    raise BuildInterruptingException(
                        SETUP_DIST_NOT_FIND_MESSAGE
                    )

            shprint(sh.make, '-j', str(cpu_count()), '-C', build_dir, _env=env)

            # make a copy of the python executable giving it the name we want,
            # because we got different python's executable names depending on
            # the fs being case-insensitive (Mac OS X, Cygwin...) or
            # case-sensitive (linux)...so this way we will have an unique name
            # for our hostpython, regarding the used fs
            for exe_name in ['python.exe', 'python']:
                exe = join(self.get_path_to_python(), exe_name)
                if Path(exe).is_file():
                    shprint(sh.cp, exe, self.python_exe)
                    break

        self.ctx.hostpython = self.python_exe


recipe = HostPython3Recipe()
