import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from apycula.gowin_pack import Device


class RamInitTest(unittest.TestCase):
    def pack(self, params):
        device = Device.__new__(Device)
        device.used_slices = Mock()
        device.chipdb = Mock()
        device.chipdb.get_lut_data.side_effect = lambda x, y, lane: [{(lane, bit)} for bit in range(16)]
        bel = SimpleNamespace(x=2, y=3, cell=SimpleNamespace(parms=params))
        return [(f.x, f.y, set(f.bits)) for f in device.get_RAM16SDP4_fuses(bel)]

    def test_missing_init_matches_explicit_zero(self):
        self.assertEqual(self.pack({}), self.pack({f'INIT_{i}': '0' * 16 for i in range(4)}))

    def test_explicit_init_is_preserved(self):
        params = {f'INIT_{i}': '1' * 16 for i in range(4)}
        params['INIT_0'] = '0' * 15 + '1'
        self.assertEqual(self.pack(params), [(2, 3, {(0, bit) for bit in range(1, 16)})])


if __name__ == '__main__':
    unittest.main()
