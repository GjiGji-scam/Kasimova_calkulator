[app]
title = Cosmic Calculator
package.name = cosmiccalc
package.domain = org.cosmic

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,ttf
source.include_patterns = ui.kv,settings.py

version = 1.0.0
requirements = python3,kivy==2.3.0

orientation = portrait
fullscreen = 1
icon.filename = %(source.dir)s/icon.png

android.permissions = 
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1