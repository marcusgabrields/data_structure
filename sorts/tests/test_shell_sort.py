import unittest

from shell import shellsort


class ShellTest(unittest.TestCase):

    def test_sort_one_element(self):
        self.assertEqual([1], shellsort([1]))

    def test_sort_two_elemets(self):
        self.assertEqual([1, 2], shellsort([2, 1]))

    def test_sort_three_elements(self):
        self.assertEqual([1, 2, 3], shellsort([3, 2, 1]))

    def test_sort_random_list(self):
        import random
        random_array = random.sample(range(100), 50)
        random_array_sorted = sorted(random_array)
        self.assertEqual(random_array_sorted, shellsort(random_array))
