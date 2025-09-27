[app]
title = POS System
package.name = possystem
package.domain = org.kivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,ttf

version = 1.0.0
requirements = 
    python3,
    kivy==2.3.0,
    openssl,
    requests,
    pyopenssl,
    certifi,
    chardet,
    idna,
    urllib3,
    android,
    pyjnius

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK

android.api = 33
android.minapi = 21
android.ndk = 25b
android.ndk_api = 21

# Add specific ABI support to reduce APK size
android.arch = armeabi-v7a

orientation = portrait
fullscreen = 0

# Presplash and icon
presplash.filename = presplash.png
icon.filename = icon.png

# Log level
log_level = 2

# Add garden dependencies if needed
# garden_requirements =

# Add additional build options
[buildozer]
log_level = 2
warn_on_root = 1

# Add service declarations for Android
#[service]
#name = myservice

# Add intent filters if needed
#[intent-filter]
#<action android:name="android.intent.action.VIEW" />
#<category android:name="android.intent.category.DEFAULT" />
#<category android:name="android.intent.category.BROWSABLE" />
#<data android:scheme="http" />
