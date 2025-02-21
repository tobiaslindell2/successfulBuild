# This file is dual licensed under the terms of the Apache License, Version
# 2.0, and the BSD License. See the LICENSE file in the root of this repository
# for complete details.


import os
import sys
from distutils import dist
from distutils.ccompiler import get_default_compiler
from distutils.command.config import config

from _cffi_src.utils import build_ffi_for_binding, compiler_type

print("")
print("")
print("CC LOG build_openssl.py - ROUND UNO")

def _get_openssl_libraries(platform):
    print(f"CC LOG os.environ.get('CRYPTOGRAPHY_SUPPRESS_LINK_FLAGS'): {os.environ.get('CRYPTOGRAPHY_SUPPRESS_LINK_FLAGS')}")
    if os.environ.get("CRYPTOGRAPHY_SUPPRESS_LINK_FLAGS", None):
        return []
    # OpenSSL goes by a different library name on different operating systems.
    if platform == "win32" and compiler_type() == "msvc":
        print("2 2 2 2 2")
        return [
            "libssl",
            "libcrypto",
            "advapi32",
            "crypt32",
            "gdi32",
            "user32",
            "ws2_32",
        ]
    else:
        # darwin, linux, mingw all use this path
        # In some circumstances, the order in which these libs are
        # specified on the linker command-line is significant;
        # libssl must come before libcrypto
        # (https://marc.info/?l=openssl-users&m=135361825921871)
        # -lpthread required due to usage of pthread an potential
        # existance of a static part containing e.g. pthread_atfork
        # (https://github.com/pyca/cryptography/issues/5084)
        if sys.platform == "zos":
            return ["ssl", "crypto"]
        else:
            return ["ssl", "crypto"]


def _extra_compile_args(platform):
    """
    We set -Wconversion args here so that we only do Wconversion checks on the
    code we're compiling and not on cffi itself (as passing -Wconversion in
    CFLAGS would do). We set no error on sign conversion because some
    function signatures in LibreSSL differ from OpenSSL have changed on long
    vs. unsigned long in the past. Since that isn't a precision issue we don't
    care.
    """
    # make sure the compiler used supports the flags to be added
    is_gcc = False
    if get_default_compiler() == "unix":
        d = dist.Distribution()
        print(f"CC LOG d: {d}")
        cmd = config(d)
        print(f"CC LOG cmd: {cmd}")
        cmd._check_compiler()
        print(f"CC LOG cmd._check_compiler(): {cmd._check_compiler()}")
        is_gcc = (
            "gcc" in cmd.compiler.compiler[0]
            or "clang" in cmd.compiler.compiler[0]
        )
        print(f"CC LOG is_gcc: {is_gcc}")
    if is_gcc or not (
        platform in ["win32", "hp-ux11", "sunos5"]
        or platform.startswith("aix")
    ):
        return ["-Wconversion", "-Wno-error=sign-conversion"]
    else:
        return []


ffi = build_ffi_for_binding(
    module_name="cryptography.hazmat.bindings._openssl",
    module_prefix="_cffi_src.openssl.",
    modules=[
        # This goes first so we can define some cryptography-wide symbols.
        "cryptography",
        # Provider comes early as well so we define OSSL_LIB_CTX
        "provider",
        "asn1",
        "bignum",
        "bio",
        "cmac",
        "conf",
        "crypto",
        "dh",
        "dsa",
        "ec",
        "ecdsa",
        "engine",
        "err",
        "evp",
        "fips",
        "hmac",
        "nid",
        "objects",
        "opensslv",
        "osrandom_engine",
        "pem",
        "pkcs12",
        "rand",
        "rsa",
        "ssl",
        "x509",
        "x509name",
        "x509v3",
        "x509_vfy",
        "pkcs7",
        "callbacks",
    ],
    libraries=_get_openssl_libraries(sys.platform),
    extra_compile_args=_extra_compile_args(sys.platform),
)
print(f"CC LOG ffi: {ffi}")
test11 = _get_openssl_libraries(sys.platform)
test22 = extra_compile_args=_extra_compile_args(sys.platform)
print(f"CC LOG _get_openssl_libraries(sys.platform): {test11}")
print(f"CC LOG extra_compile_args=_extra_compile_args(sys.platform): {test22}")
print("")
print("")
