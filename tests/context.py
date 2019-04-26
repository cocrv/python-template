import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sample

# this handy fella handles all imports from external sources into this one context file.
# usage in tests would look like:
#   from .context import sample
