"""
backend/sitecustomize.py

Compatibility shim to provide pkgutil.get_loader when running the backend
script directly. Placing this file inside backend/ ensures Python will include
it on sys.path when you run `python backend/app.py` and fixes the
AttributeError raised by Flask on some Python versions where pkgutil.get_loader
is missing.
"""

import pkgutil
import importlib.util


def _get_loader(name):
    spec = importlib.util.find_spec(name)
    return spec.loader if spec is not None else None


if not hasattr(pkgutil, 'get_loader'):
    pkgutil.get_loader = _get_loader
