[app]

# Application metadata
title = MINOS SIGINT UFO Scanner
package.name = minosufoscanner
package.domain = org.minos.sigint

# Source
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,onnx,txt
# Keep build/packaging files out of the APK
source.exclude_dirs = bin,.buildozer,.git,__pycache__
source.exclude_patterns = buildozer.spec,README.md

version = 1.0

# Python/runtime requirements.
# opencv + numpy are built from source for Android by python-for-android,
# which is the heavy part of the build.
requirements = python3,kivy,numpy,opencv

orientation = portrait
fullscreen = 0

# Android permissions required by the scanner (camera + model file storage).
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

# Android API / build tooling. SDK/NDK are auto-downloaded by buildozer.
android.api = 33
android.minapi = 24
# NDK version intentionally left unset so python-for-android downloads its
# own recommended NDK. The develop branch builds Python 3.14 + NumPy 2.x,
# whose C++ sources require a newer clang/libc++ than old NDKs (r25b's
# clang-14 fails to compile numpy's unique.cpp).
android.accept_sdk_license = True

# Target 64-bit ARM (covers essentially all modern phones).
android.archs = arm64-v8a

# Use the maintained p4a develop branch for current opencv/numpy recipes.
p4a.branch = develop

# Local recipe overrides. Ships a patched libthorvg recipe whose upstream
# version only globs the NDK r26+ "lib/clang/*" runtime layout and crashes
# (IndexError) on NDK r25b's "lib64/clang/*" layout. The override tries both.
p4a.local_recipes = ./p4a-recipes

[buildozer]

# Verbose so build progress/errors are visible in logs.
log_level = 2
# Required because this CI/container build runs as root.
warn_on_root = 0
