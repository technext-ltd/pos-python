[app]
title = POS System
package.name = possystem
package.domain = org.kivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0
requirements = python3,kivy

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b

orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
