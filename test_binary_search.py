import unittest
from binary_search import binary_search
from random import randint


class TestBinarySearch(unittest.TestCase):

    def test_number_found_right_side(self):
        input_list, target = [1, 4, 6, 7, 9, 11, 13], 11
        found_index = binary_search(input_list, target)
        self.assertEqual(5, found_index)

    def test_number_found_left_side(self):
        input_list, target = [1, 4, 6, 7, 9, 11, 13], 4
        found_index = binary_search(input_list, target)
        self.assertEqual(1, found_index)

    def test_number_not_in_list(self):
        input_list, target = [1, 4, 6, 7, 9, 11, 13], 44
        found_index = binary_search(input_list, target)
        self.assertEqual(-1, found_index)

    def test_number_empty_list(self):
        input_list, target = [], 4
        found_index = binary_search(input_list, target)
        self.assertEqual(-1, found_index)

    def test_negative_number_in_list(self):
        input_list, target = [-10, -5, 4, 7, 9, 11, 13], -5
        found_index = binary_search(input_list, target)
        self.assertEqual(1, found_index)

    def test_negative_number_not_in_list(self):
        input_list, target = [1, 4, 6, 7, 9, 11, 13], -5
        found_index = binary_search(input_list, target)
        self.assertEqual(-1, found_index)

    def test_number_appears_twice(self):
        input_list, target = [1, 4, 6, 7, 9, 11, 11], 11
        found_index = binary_search(input_list, target)
        self.assertEqual(5 or 6, found_index)

    def test_all_nums_in_list(self):
        input_list = [1, 4, 6, 7, 9, 11, 13]
        index = 0
        for num in input_list:
            found_index = binary_search(input_list, num)
            self.assertEqual(index, found_index)
            index += 1

    # Test functions to check binary search with numerous combinations
    def check_value(self, input_list, value):
        found_index = binary_search(input_list, value)
        # print('found index is: ', found_index, 'value is: ', value)
        if ((found_index == -1) and (value in input_list)) or ((found_index != -1) and (value != input_list[found_index])):
            exit()

    def create_input_list(self):
        list_size = randint(0, 10000)
        smallest_number = randint(-5, 50)
        largest_number = randint(51, 11000)
        input_list = sorted([randint(smallest_number, largest_number) for x in range(list_size)])
        return input_list, smallest_number, largest_number

    def test_randomly_generated_values(self):
        runs = 50
        for run in range(runs):
            input_list, smallest_number, largest_number = self.create_input_list()
            # print(input_list, smallest_number, largest_number)
            # check every possible value that may exist in list and a few that definitely will not be
            for value in range(smallest_number-2, largest_number+2):
                self.check_value(input_list, value)


