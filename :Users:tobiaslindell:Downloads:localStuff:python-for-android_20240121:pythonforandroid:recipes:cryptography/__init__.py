from pythonforandroid.recipe import CompiledComponentsPythonRecipe, Recipe
import os

print("")
print(f"CC LOG __init__.py (cryptography) - ROUND TRE")

class CryptographyRecipe(CompiledComponentsPythonRecipe):
    name = 'cryptography'
    version = '38.0.1'
    url = 'https://github.com/pyca/cryptography/archive/{version}.tar.gz'
    depends = ['openssl', 'six', 'setuptools', 'cffi']
    call_hostpython_via_targetpython = False

    def get_recipe_env(self, arch):
        #env = os.environ.copy()
        
        env = super().get_recipe_env(arch)
        arch_name = arch.arch
        #print(f"CC LOG env: {env}")
        print(f"CC LOG arch:: {arch}")
        print(f"CC LOG arch_name: {arch_name}")

        ndk_sysroot = os.path.join(self.ctx.ndk_dir, 
            'toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/33')
        print(f"CC LOG ndk_sysroot: {ndk_sysroot}")    
        
        env["PYO3_CROSS_LIB_DIR"] = "/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_33/python3/android-build"
        
        # Use -lc instead of -lpthread
        env["RUSTFLAGS"] = (
        	"-C link-arg=-L/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/lib/aarch64-linux-android/33 "
        	"-C link-arg=-L//Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/libs/arm64-v8a "
        	"-C link-arg=-lc "
        	"-C link-arg=-ldl "
        	"-C link-arg=-lm "
        	"-C link-arg=-lpython3.11 "
        	"-C link-arg=-static-libgcc "
        	"-C link-arg=-static-libstdc++"
        )

        print(f"CC LOG env['RUSTFLAGS']: {env['RUSTFLAGS']}")

        env["CARGO_BUILD_TARGET"] = "aarch64-linux-android"
        env["CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER"] = (
            f"{self.ctx.ndk_dir}/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android33-clang"
        )
        print(f"CC LOG env['CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER']: {env['CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER']}")

        openssl_recipe = Recipe.get_recipe('openssl', self.ctx)
        print(f"CC LOG openssl_recipe: {openssl_recipe}")
        env["OPENSSL_DIR"] = openssl_recipe.get_build_dir(arch)
        print(f"CC LOG env['OPENSSL_DIR']: {env['OPENSSL_DIR']}")
        env["CFLAGS"] += f" {openssl_recipe.include_flags(arch)}"
        print(f"CC LOG env['CFLAGS']: {env['CFLAGS']}")
        env["LDFLAGS"] += (
            f" -L{os.path.join(openssl_recipe.get_build_dir(arch_name), '')} "
            "-lcrypto -lssl -lc -ldl"
        )
        env['LD_LIBRARY_PATH'] = "/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/libs/arm64-v8a"
        
        print(f"CC LOG env['LDFLAGS']: {env['LDFLAGS']}")
        print(f"CC LOG env NEW ['LD_LIBRARY_PATH']: {env['LD_LIBRARY_PATH']}")

        print(f"RUSTFLAGS: {env['RUSTFLAGS']}")
        print(f"CARGO_BUILD_TARGET: {env['CARGO_BUILD_TARGET']}")
        print(f"CARGO_LINKER: {env['CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER']}")
        print(f"OPENSSL_DIR: {env['OPENSSL_DIR']}")
        print(f"CFLAGS: {env['CFLAGS']}")
        print(f"LDFLAGS: {env['LDFLAGS']}")
        
        return env


recipe = CryptographyRecipe()