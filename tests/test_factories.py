# !/usr/bin/python
# This Python file uses the following encoding: utf-8
from __future__ import print_function
import unittest
from prettytable.factory import from_md, split_md_row, strip_md_content


md = \
'''| name | age | 姓名 | 年龄  |   |
|------|-----|---|---|---|
| ke   | 1   | Kane  |  二十 |   |

| wa   | 2   |  王 |   |  三十 |
|      |     |   |   |   |
'''


class FromMdTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.md = md

    def test_from_md(self):
        print(from_md(self.md))

    def test_split_md_row(self):
        s = '| ke   | 1   | Kane  |  二十 |   |'
        splited_s = split_md_row(s)
        self.assertIn('ke', splited_s)
        self.assertIn('', splited_s)
        self.assertIn('1', splited_s)
        self.assertIn('二十', splited_s)
        self.assertNotIn(' ', splited_s)

        blank_row = '|      |     |   |   |   |'
        splited_bs = split_md_row(blank_row)
        for i in splited_bs:
            self.assertEqual('', i)

    def test_strip_md_content(self):
        s_list = ':ke', ' kane:', 'kane :', ' : kane:', '    '
        for s in s_list:
            stripped_s = strip_md_content(s)
            if stripped_s:
                self.assertNotEqual(' ', stripped_s[0])
                self.assertNotEqual(' ', stripped_s[-1])

                self.assertNotEqual(':', stripped_s[0])
                self.assertNotIn(':', stripped_s[0])


if __name__ == '__main__':
    unittest.main()
