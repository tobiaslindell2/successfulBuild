AS

nano ~/.zshrc
source ~/.zshrc



-NEW- Clean up:
cd /Users/tobiaslindell/appStuff
rm -rf /Users/tobiaslindell/appStuff/.buildozer
rm -rf /Users/tobiaslindell/.buildozer
rm -rf /Users/tobiaslindell/.android
rm -rf ~/.cache/pip
rm -rf liocal/share/python-for-android
pip3 cache purge
exit
pipenv --rm
pipenv --clear
sudo rm -rf ~/.gradle
Tandeli1234567!



-NEW- Set up new virtual environment and start build:
cd /Users/tobiaslindell/appStuff
pipenv install
pipenv shell
pipenv run buildozer -v android debug



Install and start app:
adb logcat
adb install -r /Users/tobiaslindell/appStuff/bin/convokeeper-0.1-arm64-v8a-debug.apk
adb shell am start -n com.crappcompany.convokeeper/org.kivy.android.PythonActivity



Check what is included in the APK file:
unzip /Users/tobiaslindell/appStuff/bin/convokeeper-0.1-arm64-v8a-debug.apk -d /Users/tobiaslindell/appStuff/bin/unzipped



Location of various files and dirs
libpython.so
/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_33/python3/android-build/
/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/libs/arm64-v8a
_openssl.abi3.so and _rust.abi3.so
/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/cryptography/arm64-v8a__ndk_target_33/cryptography/build/lib.macosx-14.4-arm64-cpython-311/cryptography/hazmat/bindings/
/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/python-installs/convokeeper/arm64-v8a/cryptography/hazmat/bindings/
/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/_python_bundle__arm64-v8a/_python_bundle/site-packages/cryptography/hazmat/bindings/
 _sysconfigdata__linux_aarch64-linux-android.py
/Users/tobiaslindell/Downloads/localStuff/python3/android-build/build/lib.linux-aarch64-3.11
Or /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_33/python3/android-build/build/lib.linux-aarch64-3.11
Cargo.toml
/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/cryptography/arm64-v8a__ndk_target_33/cryptography/src/rust/
p4a
/Users/tobiaslindell/Desktop/localStuff/p4a_20240121
NDK
/Users/tobiaslindell/Library/Android/sdk/ndk/25.2.9519653
Compilers
/Users/tobiaslindell/.buildozer/android/platform/android-ndk-r25b/toolchains/llvm/prebuilt/darwin-x86_64/bin
Rust project
/Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/cryptography/arm64-v8a__ndk_target_21/cryptography/src/rust
build_ext.py /Users/tobiaslindell/.local/lib/python3.11/site-packages/setuptools/command
build_openssl.py /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/cryptography/arm64-v8a__ndk_target_33/cryptography/src/_cffi_src



Manual compilation
tar -xvf /Users/tobiaslindell/Downloads/localStuff/tar/cryptography-38.0.1.tar.gz -C /Users/tobiaslindell/Downloads/localStuff/cryptography_manual_build/unpacked
cd /Users/tobiaslindell/Downloads/localStuff/cryptography_manual_build/unpacked/cryptography-38.0.1
python3 setup.py build install --root=/Users/tobiaslindell/Downloads/localStuff/cryptography_manual_build/compiled/cryptography-38.0.1

pip install . --target=/Users/tobiaslindell/Downloads/localStuff/cryptography_manual_build/compiled/cryptography-38.0.1 --global-option=build_ext --global-option="-I/Users/tobiaslindell/Library/Android/sdk/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/sysroot/usr/include" --global-option="-L/Users/tobiaslindell/Downloads/localStuff/openssl-android/usr/local/lib"



Other useful commands:
sudo find / -name 'libpython*.so'
sudo find / -name "libpython*.so" 2>/dev/null
sdkmanager --list_installed
pip show pip
pip install pipdeptree
pipdeptree -fl
python -c "import ssl; print(ssl.OPENSSL_VERSION)"
python -c "import kivy; print(kivy.__version__)"
nano /etc/zprofile
nano /etc/paths
echo PATH
unset PATH




Checking contents of binaries:
$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-readelf -d /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/cryptography/arm64-v8a__ndk_target_33/cryptography/build/lib.macosx-14.4-arm64-cpython-311/cryptography/hazmat/bindings/_rust.abi3.so				

$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-readelf -d /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/python-installs/convokeeper/arm64-v8a/cryptography/hazmat/bindings/_rust.abi3.so

$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-readelf -d /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/_python_bundle__arm64-v8a/_python_bundle/site-packages/cryptography/hazmat/bindings/_rust.abi3.so

objdump -x /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/_python_bundle__arm64-v8a/_python_bundle/site-packages/cryptography/hazmat/bindings/_rust.abi3.so

$ANDROID_NDK_HOME/toolchains/llvm/prebuilt/darwin-x86_64/bin/llvm-readelf -S /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/dists/convokeeper/_python_bundle__arm64-v8a/_python_bundle/site-packages/cryptography/hazmat/bindings/_rust.abi3.so

nm -D /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_33/python3/android-build/libpython3.11.so | grep Py_

nm -D /Users/tobiaslindell/appStuff/.buildozer/android/platform/build-arm64-v8a/build/other_builds/python3/arm64-v8a__ndk_target_33/python3/android-build/libpython3.11.so | grep Py_