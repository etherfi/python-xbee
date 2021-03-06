"""
test_digimesh.py

By James Saunders, 2016
james@saunders-family.net

Tests the XBee DigiMesh implementation class for API compliance
"""
import unittest
from xbee.tornado import has_tornado

if not has_tornado:
    raise unittest.SkipTest("Requires Tornado")

from xbee.tornado.digimesh import DigiMesh  # noqa


class TestDigiMesh(unittest.TestCase):
    """
    Tests DigiMesh-specific features
    More tests will need adding in time
    """

    def setUp(self):
        self.digimesh = DigiMesh(None)
        super(TestDigiMesh, self).setUp()

    def test_split_tx_status(self):
            data = b'\x8b\x01\xff\xff\x01\x01\x01'
            info = self.digimesh._split_response(data)
            expected_info = {
                'id': 'tx_status',
                'frame_id': b'\x01',
                'reserved': b'\xff\xff',
                'retries': b'\x01',
                'deliver_status': b'\x01',
                'discover_status': b'\x01'
            }
            self.assertEqual(info, expected_info)


if __name__ == '__main__':
    unittest.main()
