from __future__ import absolute_import
from unittest import TestCase

from . import strslice


class Tests(TestCase):
    def test_normal(self):
        self.assertEqual(
            strslice(u'abc')[0],
            u'a'
        )

    def test_normal_slice(self):
        self.assertEqual(
            strslice(u'abc')[:2],
            u'ab',
        )

    def test_emoji(self):
        self.assertEqual(
            strslice(u'\U0001f602\U0001f3e9\U0001f684')[0],
            u'\U0001f602'
        )

    def test_emoji_slice(self):
        self.assertEqual(
            strslice(u'\U0001f602\U0001f3e9\U0001f684')[1:],
            u'\U0001f3e9\U0001f684'
        )

    def test_empty(self):
        self.assertRaises(
            IndexError,
            lambda: strslice(u'')[0],
        )

    def test_empty_slice(self):
        self.assertEqual(
            strslice(u'')[0:100],
            u''
        )