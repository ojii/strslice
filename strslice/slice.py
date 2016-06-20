# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .grapheme import cluster_boundaries


class strslice(object):
    def __init__(self, s):
        gen = cluster_boundaries(s)
        try:
            start = next(gen)
        except StopIteration:
            self.bits = []
        else:
            self.bits = []
            end = next(gen)
            self.bits.append(s[start:end])
            for new_end in gen:
                start = end
                end = new_end
                self.bits.append(s[start:end])

    def __getitem__(self, item):
        return u''.join(self.bits[item])
