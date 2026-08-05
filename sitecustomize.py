"""
sitecustomize.py

Temporary compatibility shim to provide pkgutil.get_loader in Python runtimes
that no longer expose it (e.g., very new Python 3.14 builds). Some libraries
(such as older Flask versions) call pkgutil.get_loader; if it's missing an
AttributeError occurs during app initialization. This shim restores a
get_loader implementation using importlib.util.find_spec and is only applied
if the attribute is absent, so it won't override the stdlib behavior.

Add this file to the project root so Python will import it automatically on
startup (sitecustomize is automatically imported if found on sys.path).
"""

import pkgutil
import importlib.util


def _get_loader(name):
    """Find and return the loader for the named module, or None."""
    spec = importlib.util.find_spec(name)
    return spec.loader if spec is not None else None


# Only set if missing to avoid hiding other issues
if not hasattr(pkgutil, 'get_loader'):
    pkgutil.get_loader = _get_loader
