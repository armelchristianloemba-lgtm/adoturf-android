[app]

title = ADO TURF INTELLIGENT
package.name = adoturf
package.domain = org.adoturf

source.dir = .
source.include_exts = py,kv,json,txt
version = 1.0

requirements = python3,kivy
orientation = portrait
fullscreen = 0

android.permissions = READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

[buildozer]

log_level = 2
warn_on_root = 1
