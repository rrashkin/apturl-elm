''' A file for testing the python apt module'''

# import sys
import apt

PACKAGE_NAME = "chromium-browser"

CACHE = apt.cache.Cache()
# CACHE.update()

if PACKAGE_NAME in CACHE:
    PACKAGE = CACHE[PACKAGE_NAME]
    print((PACKAGE.versions[0].description))
else:
    print(("Package %s not found" % PACKAGE_NAME))
