[app]
title = Calculator

package.name = mycalculator
package.domain = org.example

version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_patterns = license,test*

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.ndk = 25b
# android.sdk = 24  <-- УДАЛИТЬ ЭТУ СТРОКУ
android.build_tools_version = 33.0.2
android.accept_sdk_license = True  <-- ДОБАВИТЬ ЭТУ СТРОКУ

android.archs = arm64-v8a, armeabi-v7a
android.permissions = 
android.release_artifact = apk
android.debug_artifact = apk
android.presplash_color = #000000
