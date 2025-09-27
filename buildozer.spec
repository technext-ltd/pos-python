[app]
title = POS System
package.name = possystem
package.domain = org.kivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json

version = 0.1
requirements = python3,kivy

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21

orientation = portrait

[buildozer]
log_level = 2
