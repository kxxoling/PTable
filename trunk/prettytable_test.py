import unittest
import sys
sys.path.append("../src/")
from math import pi, e, sqrt
from prettytable import *

class BuildEquivelanceTest(unittest.TestCase):

    """Make sure that building a table row-by-row and column-by-column yield the same results"""

    def setUp(self):

        # Row by row...
        self.row = PrettyTable()
        self.row.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
        self.row.add_row(["Adelaide",1295, 1158259, 600.5])
        self.row.add_row(["Brisbane",5905, 1857594, 1146.4])
        self.row.add_row(["Darwin", 112, 120900, 1714.7])
        self.row.add_row(["Hobart", 1357, 205556, 619.5])
        self.row.add_row(["Sydney", 2058, 4336374, 1214.8])
        self.row.add_row(["Melbourne", 1566, 3806092, 646.9])
        self.row.add_row(["Perth", 5386, 1554769, 869.4])

        # Column by column...
        self.col = PrettyTable()
        self.col.add_column("City name",["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
        self.col.add_column("Area", [1295, 5905, 112, 1357, 2058, 1566, 5386])
        self.col.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
        self.col.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

        # A mix of both!
        self.mix = PrettyTable()
        self.mix.field_names = ["City name", "Area"]
        self.mix.add_row(["Adelaide",1295])
        self.mix.add_row(["Brisbane",5905])
        self.mix.add_row(["Darwin", 112])
        self.mix.add_row(["Hobart", 1357])
        self.mix.add_row(["Sydney", 2058])
        self.mix.add_row(["Melbourne", 1566])
        self.mix.add_row(["Perth", 5386])
        self.mix.add_column("Population", [1158259, 1857594, 120900, 205556, 4336374, 3806092, 1554769])
        self.mix.add_column("Annual Rainfall",[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9, 869.4])

    def testRowColEquivalenceASCII(self):

        self.assertEqual(self.row.get_string(), self.col.get_string())

    def testRowMixEquivalenceASCII(self):

        self.assertEqual(self.row.get_string(), self.mix.get_string())

    def testRowColEquivalenceHTML(self):

        self.assertEqual(self.row.get_html_string(), self.col.get_html_string())

    def testRowMixEquivalenceHTML(self):

        self.assertEqual(self.row.get_html_string(), self.mix.get_html_string())

#class FieldnamelessTableTest(unittest.TestCase):
#
#    """Make sure that building and stringing a table with no fieldnames works fine"""
#
#    def setUp(self):
#        self.x = PrettyTable()
#        self.x.add_row(["Adelaide",1295, 1158259, 600.5])
#        self.x.add_row(["Brisbane",5905, 1857594, 1146.4])
#        self.x.add_row(["Darwin", 112, 120900, 1714.7])
#        self.x.add_row(["Hobart", 1357, 205556, 619.5])
#        self.x.add_row(["Sydney", 2058, 4336374, 1214.8])
#        self.x.add_row(["Melbourne", 1566, 3806092, 646.9])
#        self.x.add_row(["Perth", 5386, 1554769, 869.4])
#
#    def testCanStringASCII(self):
#        self.x.get_string()
#
#    def testCanStringHTML(self):
#        self.x.get_html_string()
#
#    def testAddFieldnamesLater(self):
#        self.x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
#        self.x.get_string()

class CityDataTest(unittest.TestCase):

    """Just build the Australian capital city data example table."""

    def setUp(self):

        self.x = PrettyTable(["City name", "Area", "Population", "Annual Rainfall"])
        self.x.add_row(["Adelaide",1295, 1158259, 600.5])
        self.x.add_row(["Brisbane",5905, 1857594, 1146.4])
        self.x.add_row(["Darwin", 112, 120900, 1714.7])
        self.x.add_row(["Hobart", 1357, 205556, 619.5])
        self.x.add_row(["Sydney", 2058, 4336374, 1214.8])
        self.x.add_row(["Melbourne", 1566, 3806092, 646.9])
        self.x.add_row(["Perth", 5386, 1554769, 869.4])

class OptionOverrideTests(CityDataTest):

    """Make sure all options are properly overwritten by get_string."""

    def testBorder(self):
        default = self.x.get_string()
        override = self.x.get_string(border=False)
        self.assertTrue(default != override)

    def testHeader(self):
        default = self.x.get_string()
        override = self.x.get_string(header=False)
        self.assertTrue(default != override)

    def testHrulesAll(self):
        default = self.x.get_string()
        override = self.x.get_string(hrules=ALL)
        self.assertTrue(default != override)

    def testHrulesNone(self):

        default = self.x.get_string()
        override = self.x.get_string(hrules=NONE)
        self.assertTrue(default != override)

class BasicTests(CityDataTest):

    """Some very basic tests."""

    def testNoBlankLines(self):

        """No table should ever have blank lines in it."""

        string = self.x.get_string()
        lines = string.split("\n")
        self.assertTrue("" not in lines)

    def testAllLengthsEqual(self):

        """All lines in a table should be of the same length."""

        string = self.x.get_string()
        lines = string.split("\n")
        lengths = [len(line) for line in lines]
        lengths = set(lengths)
        self.assertEqual(len(lengths),1)

class NoBorderBasicTests(BasicTests):

    """Run the basic tests with border = False"""

    def setUp(self):
        BasicTests.setUp(self)
        self.x.border = False

class NoHeaderBasicTests(BasicTests):

    """Run the basic tests with header = False"""

    def setUp(self):
        BasicTests.setUp(self)
        self.x.header = False

class HrulesNoneBasicTests(BasicTests):

    """Run the basic tests with hrules = NONE"""

    def setUp(self):
        BasicTests.setUp(self)
        self.x.hrules = NONE

class HrulesAllBasicTests(BasicTests):

    """Run the basic tests with hrules = ALL"""

    def setUp(self):
        BasicTests.setUp(self)
        self.x.hrules = ALL

class PresetBasicTests(BasicTests):

    """Run the basic tests after using set_style"""

    def setUp(self):
        BasicTests.setUp(self)
        self.x.set_style(MSWORD_FRIENDLY)

class SlicingTests(CityDataTest):

    def setUp(self):
        CityDataTest.setUp(self)

    def testSliceFirstTwoRows(self):
        y = self.x[0:2]
        string = y.get_string()
        assert len(string.split("\n")) == 6
        assert "Adelaide" in string
        assert "Brisbane" in string
        assert "Melbourne" not in string
        assert "Perth" not in string

    def testSliceLastTwoRows(self):
        y = self.x[-2:]
        string = y.get_string()
        assert len(string.split("\n")) == 6
        assert "Adelaide" not in string
        assert "Brisbane" not in string
        assert "Melbourne" in string
        assert "Perth" in string

class SortingTests(CityDataTest):

    def setUp(self):
        CityDataTest.setUp(self)

    def testSortBy(self):
        self.x.sortby = self.x.field_names[0]
        old = self.x.get_string()
        for field in self.x.field_names[1:]:
            self.x.sortby = field
            new = self.x.get_string()
            assert new != old

    def testReverseSort(self):
        for field in self.x.field_names:
            self.x.sortby = field
            self.x.reversesort = False
            forward = self.x.get_string()
            self.x.reversesort = True
            backward = self.x.get_string()
            forward_lines = forward.split("\n")[2:] # Discard header lines
            backward_lines = backward.split("\n")[2:]
            backward_lines.reverse()
            assert forward_lines == backward_lines

    def testSortKey(self):
        # Test sorting by length of city name
        def key(vals):
            vals[0] = len(vals[0])
            return vals
        self.x.sortby = "City name"
        self.x.sort_key = key
        assert self.x.get_string().strip() == """+-----------+------+------------+-----------------+
| City name | Area | Population | Annual Rainfall |
+-----------+------+------------+-----------------+
|   Perth   | 5386 |  1554769   |      869.4      |
|   Darwin  | 112  |   120900   |      1714.7     |
|   Hobart  | 1357 |   205556   |      619.5      |
|   Sydney  | 2058 |  4336374   |      1214.8     |
|  Adelaide | 1295 |  1158259   |      600.5      |
|  Brisbane | 5905 |  1857594   |      1146.4     |
| Melbourne | 1566 |  3806092   |      646.9      |
+-----------+------+------------+-----------------+
""".strip()

class IntegerFormatBasicTests(BasicTests):

    """Run the basic tests after setting an integer format string"""

    def setUp(self):
        BasicTests.setUp(self)
        self.x.int_format = "04"

class FloatFormatBasicTests(BasicTests):

    """Run the basic tests after setting a float format string"""

    def setUp(self):
        BasicTests.setUp(self)
        self.x.float_format = "6.2"

class FloatFormatTests(unittest.TestCase):

    def setUp(self):
        self.x = PrettyTable(["Constant", "Value"])
        self.x.add_row(["Pi", pi]) 
        self.x.add_row(["e", e]) 
        self.x.add_row(["sqrt(2)", sqrt(2)]) 

    def testNoDecimals(self):
        self.x.float_format = ".0"
        self.x.caching = False
        assert "." not in self.x.get_string()

    def testRoundTo5DP(self):
        self.x.float_format = ".5"
        string = self.x.get_string()
        assert "3.14159" in string
        assert "3.141592" not in string
        assert "2.71828" in string 
        assert "2.718281" not in string 
        assert "2.718282" not in string 
        assert "1.41421" in string
        assert "1.414213" not in string

    def testPadWith2Zeroes(self):
        self.x.float_format = "06.2"
        string = self.x.get_string()
        assert "003.14" in string
        assert "002.72" in string
        assert "001.41" in string

class BreakLineTests(unittest.TestCase):
    def testAsciiBreakLine(self):
        t = PrettyTable(['Field 1', 'Field 2'])
        t.add_row(['value 1', 'value2\nsecond line'])
        t.add_row(['value 3', 'value4'])
        result = t.get_string(hrules=True)
        assert result.strip() == """
+---------+-------------+
| Field 1 |   Field 2   |
+---------+-------------+
| value 1 |    value2   |
|         | second line |
+---------+-------------+
| value 3 |    value4   |
+---------+-------------+
""".strip()

        t = PrettyTable(['Field 1', 'Field 2'])
        t.add_row(['value 1', 'value2\nsecond line'])
        t.add_row(['value 3\n\nother line', 'value4\n\n\nvalue5'])
        result = t.get_string(hrules=True)
        assert result.strip() == """
+------------+-------------+
|  Field 1   |   Field 2   |
+------------+-------------+
|  value 1   |    value2   |
|            | second line |
+------------+-------------+
|  value 3   |    value4   |
|            |             |
| other line |             |
|            |    value5   |
+------------+-------------+
""".strip()

        t = PrettyTable(['Field 1', 'Field 2'])
        t.add_row(['value 1', 'value2\nsecond line'])
        t.add_row(['value 3\n\nother line', 'value4\n\n\nvalue5'])
        result = t.get_string()
        assert result.strip() == """
+------------+-------------+
|  Field 1   |   Field 2   |
+------------+-------------+
|  value 1   |    value2   |
|            | second line |
|  value 3   |    value4   |
|            |             |
| other line |             |
|            |    value5   |
+------------+-------------+
""".strip()

    def testHtmlBreakLine(self):
        t = PrettyTable(['Field 1', 'Field 2'])
        t.add_row(['value 1', 'value2\nsecond line'])
        t.add_row(['value 3', 'value4'])
        result = t.get_html_string(hrules=True)
        assert result.strip() == """
<table border="1">
    <tr>
        <th>Field 1</th>
        <th>Field 2</th>
    </tr>
    <tr>
        <td>value 1</td>
        <td>value2<br />second line</td>
    </tr>
    <tr>
        <td>value 3</td>
        <td>value4</td>
    </tr>
</table>
""".strip()

class HtmlOutputTests(unittest.TestCase):
    def testHtmlOutput(self):
        t = PrettyTable(['Field 1', 'Field 2', 'Field 3'])
        t.add_row(['value 1', 'value2', 'value3'])
        t.add_row(['value 4', 'value5', 'value6'])
        t.add_row(['value 7', 'value8', 'value9'])
        result = t.get_html_string()
        assert result.strip() == """
<table border="1">
    <tr>
        <th>Field 1</th>
        <th>Field 2</th>
        <th>Field 3</th>
    </tr>
    <tr>
        <td>value 1</td>
        <td>value2</td>
        <td>value3</td>
    </tr>
    <tr>
        <td>value 4</td>
        <td>value5</td>
        <td>value6</td>
    </tr>
    <tr>
        <td>value 7</td>
        <td>value8</td>
        <td>value9</td>
    </tr>
</table>
""".strip()

    def testHtmlOutputFormated(self):
        t = PrettyTable(['Field 1', 'Field 2', 'Field 3'])
        t.add_row(['value 1', 'value2', 'value3'])
        t.add_row(['value 4', 'value5', 'value6'])
        t.add_row(['value 7', 'value8', 'value9'])
        result = t.get_html_string(format=True)
        assert result.strip() == """
<table border="1">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">Field 1</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">Field 2</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">Field 3</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value 1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value2</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value 4</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value5</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value6</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value 7</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value8</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center">value9</td>
    </tr>
</table>
""".strip()

if __name__ == "__main__":
    unittest.main()
