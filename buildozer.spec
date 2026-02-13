[app]
# (str) Title of your application
title = Jarvis Eternal

# (str) Package name
package.name = jarvis_mobile

# (str) Package domain (needed for android packaging)
package.domain = org.nrtagroup

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 3.0.0

# (list) Application requirements
# এখানে requests এবং certifi যোগ করা হয়েছে যাতে অনলাইন এপিআই ঠিকঠাক কাজ করে
requirements = python3,kivy==2.2.1,requests,certifi,urllib3,charset-normalizer,idna

# (list) Permissions
# ক্যামেরা, ইন্টারনেট এবং IR Blaster এর জন্য প্রয়োজনীয় পারমিশন
android.permissions = INTERNET, CAMERA, TRANSMIT_IR, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, RECORD_AUDIO

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use the custom screen orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Android architectures to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (list) The Android themes to use
android.theme = @android:style/Theme.NoTitleBar.Fullscreen

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
