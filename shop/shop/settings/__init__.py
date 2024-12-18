"""
try to activate local settings. if it failed, we
load the production environment.
"""


try:
    from .local import *
except ImportError:
    from .production import *
