from __future__ import absolute_import
import sys

if sys.version_info[0] >= 3:  # pragma: no cover
    strslice = str
else:
    from .slice import strslice
