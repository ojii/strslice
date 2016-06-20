import re
import sys


if sys.maxunicode < 0x10000:
    # narrow unicode build
    rx_codepoints = re.compile(ur'[\ud800-\udbff][\udc00-\udfff]|.', re.DOTALL)

    def code_point(s, index):
        L = rx_codepoints.findall(s)
        return L[index]


    def code_points(s):
        return rx_codepoints.findall(s)
else:  # pragma: no cover
    # wide unicode build
    def code_point(s, index):
        return s[index or 0]


    def code_points(s):
        return list(s)
