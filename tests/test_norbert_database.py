import hashlib
from pathlib import Path
import unittest

from apycula.chipdb import load_chipdb


class NorbertDatabaseTest(unittest.TestCase):
    def test_pinned_capabilities(self):
        path = Path(__file__).resolve().parents[1] / 'apycula/GW5A-25A.msgpack.xz'
        self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(),
                         'a5f9153446566c2217ce3c450a7889e2bc0fe823409d8f4759160951989cf7f2')
        db = load_chipdb(str(path))
        self.assertIn('HAS_5A_IOREG', db.chip_flags)
        self.assertTrue(db.tile_types['M'])
        self.assertEqual(sum('RAM16' in db[y, x].bels for y in range(db.rows) for x in range(db.cols)), 2880)
        self.assertTrue(any(bel.portmap.get('CE') == 'IOLOGICCE0'
                            for tile in db.tiles.values() for name, bel in tile.bels.items()
                            if name == 'IOLOGICB'))


if __name__ == '__main__':
    unittest.main()
