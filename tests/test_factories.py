# !/usr/bin/python
# This Python file uses the following encoding: utf-8
from io import StringIO
import unittest
from prettytable.factory import from_csv, from_md, split_md_row, strip_md_content
import textwrap

from .test_prettytable import BasicTests


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


class CsvConstructorTest(object):
    def setUp(self):
        self.fp = StringIO(textwrap.dedent("""\
            City name, Area , Population , Annual Rainfall
            Sydney, 2058 ,  4336374   ,      1214.8
            Melbourne, 1566 ,  3806092   ,       646.9
            Brisbane, 5905 ,  1857594   ,      1146.4
            Perth, 5386 ,  1554769   ,       869.4
            Adelaide, 1295 ,  1158259   ,       600.5
            Hobart, 1357 ,   205556   ,       619.5
            Darwin, 0112 ,   120900   ,      1714.7
        """))


class CsvConstructorTestEmpty(BasicTests, CsvConstructorTest):
    def setUp(self):
        CsvConstructorTest.setUp(self)
        self.x = from_csv(self.fp)


class CsvConstructorTest_fmtparams(BasicTests, CsvConstructorTest):
    def setUp(self):
        CsvConstructorTest.setUp(self)
        self.x = from_csv(self.fp, lineterminator="\n")


class CsvConstructorTest_Fieldnames(BasicTests, CsvConstructorTest):
    def setUp(self):
        CsvConstructorTest.setUp(self)
        self.x = from_csv(self.fp, field_names=("City", "Area", "Population", "Annual Rainfall"))

if __name__ == '__main__':
    unittest.main()
