# For ADB to work
export ANDROID_HOME=/Users/tobiaslindell/Library/Android/sdk
export PATH=$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$ANDROID_HOME/cmdline-tools/latest/bin:$PATH

# Android NDK environment variables
export ANDROID_NDK_HOME=/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393
export TOOLCHAIN=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64
export TARGET=aarch64-linux-android
export API=33

# Cross-compilation environment variables
export AR=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-ar
export AS=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-as
export CC=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android33-clang
export CXX=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android33-clang++
export LD=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/ld
export RANLIB=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/$TARGET-ranlib
export STRIP=$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/$TARGET-strip
export PATH=$TOOLCHAIN/bin:$PATH

# Compiler and linker flags for cross-compilation
export OPENSSL_DIR=/Users/tobiaslindell/Downloads/localStuff/openssl1.1
export LDFLAGS="-L$OPENSSL_DIR"
export CFLAGS="-Wno-error=implicit-function-declaration -I$OPENSSL_DIR/include"
export CPPFLAGS="-I$OPENSSL_DIR/include"
export PKG_CONFIG_PATH="$OPENSSL_DIR"
export LD_LIBRARY_PATH=/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/libs/arm64-v8a

# Cargo/Rust paths and flags
#export RUSTFLAGS="-C link-args=-L/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/libs/arm64-v8a -lpython3.11 -lc -ldl -lm -static-libgcc -static-libstdc++"
export CARGO_BUILD_TARGET=aarch64-linux-android
export CARGO_TARGET_AARCH64_LINUX_ANDROID_LINKER="/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android33-clang"
export CARGO_TARGET_AARCH64_LINUX_ANDROID_AR="/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/bin/aarch64-linux-android-ar"

# pyo3 flags
export PYO3_CROSS=1
export PYO3_CROSS_LIB_DIR=/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_33/python3/android-build/
export PYO3_CROSS_PYTHON_VERSION=3.11
export PYO3_ABI3=1
export PYO3_ABI3_VERSION=3.11

# Homebrew path
export PATH="/opt/homebrew/bin:$PATH"

# Pipenv language flag
export LANG=en_US.UTF-8

# Cargo path
export PATH="$HOME/.cargo/bin:$PATH"

# Perl path
eval "$(perl -I$HOME/perl5/lib/perl5 -Mlocal::lib=$HOME/perl5)"

# Python path
export PATH=/usr/local/bin:$PATH
export SSL_CERT_FILE=$(/usr/local/bin/python3 -m certifi)

# Java path
export JAVA_HOME=/usr/local/jdk-17/jdk-17.0.14.jdk/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH

# OpenSSL path
export PATH=$OPENSSL_DIR:$PATH

# # # START OF FILE  # # #