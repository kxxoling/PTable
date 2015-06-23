# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import unittest

from prettytable.prettytable import _char_block_width



def _width_test_factory(width, words):
    def _(self):
        map(lambda x: self.assertEqual(width, _char_block_width(ord(x))),
            list(words))
    return _


class CharBlockWidthTest(unittest.TestCase):
    fixtures = {
        'normal': (1, '12345qwerljk/.,WESD'),
        'chs': (2, '石室诗士施氏嗜狮誓食十狮'),
        'jp': (2, 'はじめまして'),
        'hangul': (2, '우리글자언문청'),
        'full_width_latin': (2, 'ＸＹＺ［＼］＾＿ｘｙｚ｛｜｝～｟'),
        # 'cjk': (2, u''),
    }

    def test_fixtures(self):
        for name in self.fixtures:
            _width_test_factory(*self.fixtures[name])(self)

