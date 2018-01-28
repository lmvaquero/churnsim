from uk.ac.bristol.rechurn.topology import Topology
from uk.ac.bristol.rechurn.modes.random_mode import RandomFailures
import unittest

class TestRandomFailure(unittest.TestCase):

    def test_random(self):
        top = Topology()
        loaded = top.load_from_csvs('../nodes.csv','../edges.csv')
        self.assertTrue(loaded)
        random_failure = RandomFailures()
        failed_top = random_failure.get_new_topology(top)
        self.assertTrue(len(failed_top.nodes)<len(top.nodes))


if __name__ == '__main__':
    unittest.main()