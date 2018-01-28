from uk.ac.bristol.rechurn.topology import Topology

import unittest

class TestTopology(unittest.TestCase):

    def test_load(self):
        top = Topology()
        loaded = top.load_from_csvs('../nodes.csv','../edges.csv')
        self.assertTrue(loaded)

if __name__ == '__main__':
    unittest.main()