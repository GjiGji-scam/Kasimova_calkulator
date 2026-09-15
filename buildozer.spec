[app]
# Имя приложения (отображается на телефоне)
title = Calculator

# Имя пакета (должно быть уникальным, обычно домен в обратном порядке)
package.name = mycalculator
package.domain = org.example

# Версия приложения
version = 0.1

# Точка входа (файл, который запускается)
source.include_exts = py,png,jpg,kv,atlas,json
source.include_patterns = assets/*,images/*.png
source.exclude_patterns = license,test*

# Требования (библиотеки)
requirements = python3,kivy,pyjnius>=1.4.0

# Ориентация: портрет
orientation = portrait

# Полноэкранный режим (0 = нет, 1 = да)
fullscreen = 0

# Целевой Android API (33 подходит для Android 13)
android.api = 33

# Минимальный API (21 = Android 5.0)
android.minapi = 21

# NDK (25b совместим с API 33)
android.ndk = 25b

# Архитектуры (arm64-v8a нужна для Realme C55)
android.archs = arm64-v8a, armeabi-v7a

# Разрешения (калькулятору ничего не нужно, оставим пустым)
android.permissions = 

# Имя APK-файла
android.release_artifact = apk
android.debug_artifact = apk

# Иконка (если добавите позже)
# icon.filename = %(source.dir)s/data/icon.png

# Презагрузка (оставьте по умолчанию)
android.presplash_color = #000000