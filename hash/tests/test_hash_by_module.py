import unittest

from hash import hash_by_module


class HashFunctionModuleTest(unittest.TestCase):

    def test_hash_default_table_positios_equal_10(self):
        default = hash_by_module.__defaults__[0]
        self.assertEqual(10, default)

    def test_hash_10(self):
        self.assertEqual(0, hash_by_module(10))

    def test_hash_4579(self):
        self.assertEqual(9, hash_by_module(4579))

    def test_hash_897893(self):
        self.assertEqual(3, hash_by_module(897893))

    def test_hash_10_with_5_table_positions(self):
        self.assertEqual(0, hash_by_module(10, 5))

    def test_hash_4579_with_5_table_positions(self):
        self.assertEqual(4, hash_by_module(4579, 5))

    def test_hash_897893_with_5_table_positions(self):
        self.assertEqual(3, hash_by_module(897893, 5))


if __name__ == '__main__':
    unittest.main()
