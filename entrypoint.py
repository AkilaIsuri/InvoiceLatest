import sys
import os

# Remove any problematic asyncio packages
try:
    import importlib
    if 'asyncio' in sys.modules:
        # Use the built-in asyncio, not any installed package
        del sys.modules['asyncio']
except:
    pass

# Then import your app
from main import app

# This file will be used by Gunicorn
