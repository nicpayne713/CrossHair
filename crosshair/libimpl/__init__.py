import importlib
import sys

# WARNING: This is destructive for the datetime module.
# It disables the C implementation for the entire interpreter.
sys.modules['_datetime'] = None  # type: ignore
import datetime
importlib.reload(datetime)




from crosshair.libimpl import builtinslib
from crosshair.libimpl import collectionslib
from crosshair.libimpl import datetimelib
from crosshair.libimpl import randomlib
from crosshair.libimpl import relib

def make_registrations():
    builtinslib.make_registrations()
    collectionslib.make_registrations()
    datetimelib.make_registrations()
    randomlib.make_registrations()
    relib.make_registrations()

