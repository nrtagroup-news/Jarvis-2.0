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
version = 3.5.0

# (list) Application requirements
# গিটহাবের জন্য 'kivy==2.2.1' সরিয়ে শুধু 'kivy' দেওয়া হলো যাতে অটোমেটিক লেটেস্ট ভার্সন নেয়
requirements = python3,kivy,requests,certifi,urllib3,charset-normalizer,idna,pillow

# (list) Permissions
# তোমার আগের এবং নতুন সব পারমিশন এখানে আছে
android.permissions = INTERNET, CAMERA, TRANSMIT_IR, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, RECORD_AUDIO, ACCESS_NETWORK_STATE

# (int) Target Android API
android.api = 33
android.minapi = 21
android.ndk = 25b

# (bool) Use the custom screen orientation
orientation = portrait
fullscreen = 1

# (list) Android architectures
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (list) The Android themes
android.theme = @android:style/Theme.NoTitleBar.Fullscreen

[buildozer]
# (int) Log level
log_level = 2
warn_on_root = 1
