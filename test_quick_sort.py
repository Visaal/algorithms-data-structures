import unittest
from quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_single_element_list(self):
        input_list = [2]
        sorted_input = quick_sort(input_list)
        self.assertEqual([2], sorted_input)

    def test_quick_sort_two_element_list(self):
        input_list = [5, 2]
        sorted_input = quick_sort(input_list)
        self.assertEqual([2, 5], sorted_input)

    def test_quick_sort_three_element_list(self):
        input_list = [5, 2, 3]
        sorted_input = quick_sort(input_list)
        self.assertEqual([2, 3, 5], sorted_input)

    def test_quick_sort_even_list(self):
        input_list = [5, 2, 3, 7, 1, 6]
        sorted_input = quick_sort(input_list)
        self.assertEqual([1, 2, 3, 5, 6, 7], sorted_input)

    def test_quick_sort_odd_list(self):
        input_list = [5, 2, 3, 11, 7, 1, 6]
        sorted_input = quick_sort(input_list)
        self.assertEqual([1, 2, 3, 5, 6, 7, 11], sorted_input)

    def test_quick_sort_udacity_list(self):
        input_list = [8, 3, 1, 7, 0, 10, 2]
        sorted_input = quick_sort(input_list)
        self.assertEqual([0, 1, 2, 3, 7, 8, 10], sorted_input)


if __name__ == '__main__':
    unittest.main()

