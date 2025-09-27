#!/usr/bin/env python3
import os
import subprocess
import sys

def setup_buildozer():
    """Create buildozer.spec programmatically"""
    
    spec_content = f"""[app]
title = POS System
package.name = possystem
package.domain = org.kivy

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt

version = 1.0.0
requirements = python3,kivy

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b

orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2
"""

    with open('buildozer.spec', 'w') as f:
        f.write(spec_content)
    print("✅ buildozer.spec created")

def main():
    # Rename your main file if needed
    if os.path.exists('pos2.py') and not os.path.exists('main.py'):
        os.rename('pos2.py', 'main.py')
        print("✅ Renamed pos2.py to main.py")
    
    setup_buildozer()
    print("✅ Setup complete. Ready for GitHub Actions build.")

if __name__ == '__main__':
    main()
