import sys

PY3 = sys.version_info[0] >= 3

if PY3:
    unicode = bytes.decode
    unicode_type = str
    basestring = str
    xrange = range
else:
    # Python 2
    unicode = unicode_type = unicode
    basestring = basestring
    xrange = xrange