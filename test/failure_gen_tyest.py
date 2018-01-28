from uk.ac.bristol.rechurn.failure_gen import FailureGenerator

import unittest

class TestFailureGen(unittest.TestCase):

    def test_crud(self):
        gen = FailureGenerator()
        names = gen.get_failure_mode_names()
        self.assertTrue(len(names)==0)
        added = gen.add_failure_mode("mode1","name1")
        names = gen.get_failure_mode_names()
        self.assertTrue(added)
        self.assertTrue(len(names)==1)

        added = gen.add_failure_mode("", "name1")
        names = gen.get_failure_mode_names()
        self.assertTrue(not added)
        self.assertTrue(len(names) == 1)

        gen.delete_failure_mode("name2")
        names = gen.get_failure_mode_names()
        self.assertTrue(len(names) == 1)

        replaced = gen.replace_failure_mode("mode2", "name")
        names = gen.get_failure_mode_names()
        self.assertTrue(not replaced)
        self.assertTrue(len(names) == 1)

        replaced = gen.replace_failure_mode("mode2", "name1")
        names = gen.get_failure_mode_names()
        self.assertTrue(replaced)
        self.assertTrue(len(names) == 1)

        gen.delete_failure_mode("name")
        names = gen.get_failure_mode_names()
        self.assertTrue(len(names) == 1)

        gen.delete_failure_mode("name1")
        names = gen.get_failure_mode_names()
        self.assertTrue(len(names) == 0)

if __name__ == '__main__':
    unittest.main()