from .compat import code_point, code_points
from .constants import names, break_table
from .gen import grapheme_break_properties


def cluster_break(c, index=0):
    """Return the Grapheme_Cluster_Break property of `c`

    `c` must be a single Unicode code point string.

    If `index` is specified, this function consider `c` as a unicode
    string and return Grapheme_Cluster_Break property of the code
    point at c[index].
    """

    return grapheme_break_properties.get(code_point(c, index))


def cluster_breakables(s):
    """Iterate grapheme cluster breaking opportunities for every
    position of `s`

    1 for "break" and 0 for "do not break".  The length of iteration
    will be the same as ``len(s)``.
    """

    if not s:
        return

    prev_gcbi = 0
    i = 0
    for c in code_points(s):
        gcb = cluster_break(c)
        gcbi = names.index(gcb)
        if i > 0:
            breakable = break_table[prev_gcbi][gcbi]
        else:
            breakable = 1
        for j in range(len(c)):
            yield int(j == 0 and breakable)
        prev_gcbi = gcbi
        i += len(c)


def boundaries(breakables):
    """Iterate boundary indices of the breakabe table, `breakables`

    The boundaries start from 0 to the end of the sequence (==
    len(breakables)).

    It yields empty when the given sequence is empty.
    []
    """
    i = None
    for i, breakable in enumerate(breakables):
        if breakable:
            yield i
    if i is not None:
        yield i + 1


def cluster_boundaries(s):
    breakables = cluster_breakables(s)
    return boundaries(breakables)
