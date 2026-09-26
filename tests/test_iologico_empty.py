import unittest
from types import SimpleNamespace
from unittest.mock import Mock

from apycula.gowin_pack import Device


class EmptyOutputRegisterTest(unittest.TestCase):
    def test_attributes_are_converted_before_fuse_lookup(self):
        device = Device.__new__(Device)
        bel = SimpleNamespace(x=2, y=3, idx_str='A')
        attrs = [object()]
        codes = {42}
        device.make_IologicBelDesc = Mock(return_value=bel)
        device.common_iologic_handler = Mock(return_value=attrs)
        device.set_iologic_attrvals = Mock(return_value=codes)
        device.chipdb = Mock()
        device.chipdb.get_iologic_fuses.return_value = {(0, 1)}

        fuses = device.get_IOLOGICO_EMPTY_fuses(bel)

        device.set_iologic_attrvals.assert_called_once_with(bel, attrs)
        device.chipdb.get_iologic_fuses.assert_called_once_with(2, 3, codes, 'A')
        self.assertEqual(set(fuses[0].bits), {(0, 1)})


if __name__ == '__main__':
    unittest.main()
