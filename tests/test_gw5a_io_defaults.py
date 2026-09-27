import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from apycula.gowin_pack import GW5A_25A


class IoDefaultsTest(unittest.TestCase):
    def setUp(self):
        self.device = GW5A_25A.__new__(GW5A_25A)
        self.original = [('PULLMODE', 'UP')]
        self.device.lvcmos33_defaults = [(self.original, [('PULLMODE', 'NONE')])]
        self.device.chipdb = Mock()
        self.device.chipdb.get_iob_attr_val.side_effect = lambda attr, codes: codes.add((attr.attr, attr.val))

    def attrs(self, attrs):
        bel = SimpleNamespace(cell=SimpleNamespace(attrs=attrs))
        return self.device.set_io_attrvals(bel, self.original)

    def test_lvcmos33(self):
        self.assertEqual(self.attrs({'IO_TYPE': 'LVCMOS33'}), {('PULLMODE', 'NONE')})
        self.assertEqual(self.attrs({}), {('PULLMODE', 'NONE')})

    def test_other_standard_keeps_original_defaults(self):
        self.assertEqual(self.attrs({'IO_TYPE': 'LVCMOS18'}), {('PULLMODE', 'UP')})

    def test_explicit_override(self):
        self.assertEqual(self.attrs({'IO_TYPE': 'LVCMOS33', 'PULLMODE': 'DOWN'}), {('PULLMODE', 'DOWN')})


if __name__ == '__main__':
    unittest.main()
