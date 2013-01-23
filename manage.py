#!/usr/bin/env python
import sys
from os.path import abspath, dirname, join
from django.core.management import execute_manager

try:
    from settings import active as settings
except ImportError:
    sys.stderr.write("Error: Can't find the file 'active.py'")
    sys.exit(1)

sys.path.insert(0, abspath(join(dirname(__file__), "../")))
sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))

if __name__ == "__main__":
    execute_manager(settings)
