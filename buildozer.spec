[app]
# Имя приложения (отображается на телефоне)
title = Calculator

# Имя пакета
package.name = mycalculator
package.domain = org.example

# Версия
version = 0.1

# Папка с исходниками (главное исправление!)
source.dir = .

# Что включать в сборку
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_patterns = license,test*

# Требования
requirements = python3,kivy,pyjnius

# Ориентация экрана
orientation = portrait

# Полноэкранный режим (0 = нет)
fullscreen = 0

# Android API
android.api = 33
android.minapi = 21
android.ndk = 25b

# Архитектуры (Realme C55 — arm64)
android.archs = arm64-v8a, armeabi-v7a

# Разрешения
android.permissions = 

# Артефакты
android.release_artifact = apk
android.debug_artifact = apk

# Цвет презагрузки (чёрный, как у iOS-калькулятора)
android.presplash_color = #000000
