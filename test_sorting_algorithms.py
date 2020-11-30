import unittest
from sorting_algorithms import bubble_sort, _compare_number, _move_largest_number_to_right, insertion_sort, \
    _move_smallest_number_to_left, _find_smallest_number, selection_sort, _split_list, merge_sort, \
    _determine_midpoint, _merge_list, _split_merge_sort


class TestBubbleSort(unittest.TestCase):

    def test_compare_number_num1_bigger(self):
        num1, num2 = 10, 5
        is_number_on_right_smaller = _compare_number(num1, num2)
        self.assertTrue(is_number_on_right_smaller)

    def test_compare_number_num2_bigger(self):
        num1, num2 = 10, 15
        is_number_on_right_smaller = _compare_number(num1, num2)
        self.assertFalse(is_number_on_right_smaller)

    def test_compare_number_num1_num2_equal(self):
        num1, num2 = 10, 10
        is_number_on_right_smaller = _compare_number(num1, num2)
        self.assertFalse(is_number_on_right_smaller)

    def test_move_largest_number_to_right(self):
        unsorted_list = [5, 3, 2, 1]
        rearranged_list = _move_largest_number_to_right(unsorted_list, 1)
        self.assertEqual([3, 2, 1, 5], rearranged_list)

    def test_bubble_sort(self):
        input = [5, 3, 1, 4, 2]
        sorted_input = bubble_sort(input)
        self.assertEqual([1, 2, 3, 4, 5], sorted_input)

    def test_bubble_sort_duplicate_numbers(self):
        input = [6, 4, 3, 1, 6, 2]
        sorted_input = bubble_sort(input)
        self.assertEqual([1, 2, 3, 4, 6, 6], sorted_input)

    def test_bubble_sort_negative_numbers(self):
        input = [5, 3, -2, -1, 1]
        sorted_input = bubble_sort(input)
        self.assertEqual([-2, -1, 1, 3, 5], sorted_input)


class TestInsertionSort(unittest.TestCase):

    def test_move_smallest_number_to_left_two_numbers(self):
        unsorted_list = [9, 3]
        rearranged_list = _move_smallest_number_to_left(unsorted_list, 1)
        self.assertEqual([3, 9], rearranged_list)

    def test_move_smallest_number_to_left_three_numbers(self):
        unsorted_list = [3, 9, 6]
        rearranged_list = _move_smallest_number_to_left(unsorted_list, 2)
        self.assertEqual([3, 6, 9], rearranged_list)

    def test_move_smallest_number_to_left_with_items_to_ignore(self):
        unsorted_list = [3, 5, 6, 4, 1, 2, 8]
        rearranged_list = _move_smallest_number_to_left(unsorted_list, 3)
        self.assertEqual([3, 4, 5, 6, 1, 2, 8], rearranged_list)

    def test_insertion_sort_basic(self):
        input = [5, 3, 1, 4, 2]
        sorted_input = insertion_sort(input)
        self.assertEqual([1, 2, 3, 4, 5], sorted_input)

    def test_insertion_sort_list_already_sorted(self):
        input = [1, 2, 3, 4, 5]
        sorted_input = insertion_sort(input)
        self.assertEqual([1, 2, 3, 4, 5], sorted_input)

    def test_insertion_sort_duplicate_numbers(self):
        input = [6, 4, 3, 1, 6, 2]
        sorted_input = insertion_sort(input)
        self.assertEqual([1, 2, 3, 4, 6, 6], sorted_input)

    def test_insertion_sort_negative_numbers(self):
        input = [5, 3, -2, -1, 1]
        sorted_input = bubble_sort(input)
        self.assertEqual([-2, -1, 1, 3, 5], sorted_input)


class TestSelectionSort(unittest.TestCase):

    def test_find_smallest_number(self):
        list_to_check = [5, 3, 1, 4, 2]
        smallest_number = _find_smallest_number(list_to_check, 0)
        self.assertEqual(1, smallest_number)

    def test_find_smallest_number_with_items_to_ignore(self):
        list_to_check = [1, 3, 5, 6, 4, 2, 8]
        smallest_number = _find_smallest_number(list_to_check, 2)
        self.assertEqual(2, smallest_number)

    def test_selection_sort_basic(self):
        input = [5, 3, 1, 4, 2]
        sorted_input = selection_sort(input)
        self.assertEqual([1, 2, 3, 4, 5], sorted_input)

    def test_selection_sort_list_already_sorted(self):
        input = [1, 2, 3, 4, 5]
        sorted_input = selection_sort(input)
        self.assertEqual([1, 2, 3, 4, 5], sorted_input)

    def test_selection_sort_duplicate_numbers(self):
        input = [6, 4, 3, 1, 6, 2]
        sorted_input = selection_sort(input)
        self.assertEqual([1, 2, 3, 4, 6, 6], sorted_input)

    def test_selection_sort_negative_numbers(self):
        input = [5, 3, -2, -1, 1]
        sorted_input = selection_sort(input)
        self.assertEqual([-2, -1, 1, 3, 5], sorted_input)


class TestMergeSort(unittest.TestCase):

    def test_determine_midpoint(self):
        input = [5, 3, 7, 6, 8, 2, 4, 1]
        list_midpoint = _determine_midpoint(0, len(input)-1)
        self.assertEqual(3, list_midpoint)


    def test_determine_midpoint_odd_numbered_list(self):
        input = [5, 3, 7, 6, 8, 2, 4, 1, 9]
        list_midpoint = _determine_midpoint(0, len(input)-1)
        self.assertEqual(4, list_midpoint)

    def test_determine_midpoint_middle_of_list(self):
        sub_list_midpoint = _determine_midpoint(4, 7)
        self.assertEqual(5, sub_list_midpoint)

    def test_split_list_even_number(self):
        # input = [5, 3, 7, 6, 8, 2, 4, 1]
        left_index = 0
        right_index = 7
        left_half_start, left_half_stop, right_half_start, right_half_stop = _split_list(left_index, right_index)
        self.assertEqual(0, left_half_start)
        self.assertEqual(3, left_half_stop)
        self.assertEqual(4, right_half_start)
        self.assertEqual(7, right_half_stop)

    def test_split_list_odd_number(self):
        # input = [5, 3, 7, 6, 8, 2, 4, 1, 9]
        left_index = 0
        right_index = 8
        left_half_start, left_half_stop, right_half_start, right_half_stop = _split_list(left_index, right_index)
        self.assertEqual(0, left_half_start)
        self.assertEqual(4, left_half_stop)
        self.assertEqual(5, right_half_start)
        self.assertEqual(8, right_half_stop)

    def test_split_final_split_to_single_elements(self):
        left_index = 0
        right_index = 1
        left_half_start, left_half_stop, right_half_start, right_half_stop = _split_list(left_index, right_index)
        self.assertEqual(0, left_half_start)
        self.assertEqual(0, left_half_stop)
        self.assertEqual(1, right_half_start)
        self.assertEqual(1, right_half_stop)

    def test_split_final_split_to_single_elements_middle_of_list(self):
        left_index = 6
        right_index = 7
        left_half_start, left_half_stop, right_half_start, right_half_stop = _split_list(left_index, right_index)
        self.assertEqual(6, left_half_start)
        self.assertEqual(6, left_half_stop)
        self.assertEqual(7, right_half_start)
        self.assertEqual(7, right_half_stop)

    def test_merge_first_two_elements(self):
        list = [5, 3, 7, 6, 8, 2, 4, 1]
        left_index = 0
        right_index = 1
        merged_list = _merge_list(list, left_index, right_index)
        self.assertEqual([3, 5, 7, 6, 8, 2, 4, 1], merged_list)

    def test_merge_third_forth_elements(self):
        list = [5, 3, 7, 6, 8, 2, 4, 1]
        left_index = 2
        right_index = 3
        merged_list = _merge_list(list, left_index, right_index)
        self.assertEqual([5, 3, 6, 7, 8, 2, 4, 1], merged_list)

    def test_merge_last_two_elements(self):
        list = [5, 3, 7, 6, 8, 2, 4, 1]
        left_index = 6
        right_index = 7
        merged_list = _merge_list(list, left_index, right_index)
        self.assertEqual([5, 3, 7, 6, 8, 2, 1, 4], merged_list)

    def test_merge_first_four_elements(self):
        list = [3, 7, 4, 5, 8, 2, 6, 1]
        left_index = 0
        right_index = 3
        merged_list = _merge_list(list, left_index, right_index)
        self.assertEqual([3, 4, 5, 7, 8, 2, 6, 1], merged_list)

    def test_merge_last_four_elements(self):
        list = [3, 7, 4, 5, 2, 8, 1, 6]
        left_index = 4
        right_index = 7
        merged_list = _merge_list(list, left_index, right_index)
        self.assertEqual([3, 7, 4, 5, 1, 2, 6, 8], merged_list)

    def test_split_merge_sort(self):
        input = [5, 3, 7, 6, 8, 2, 4, 1]
        sorted_list = _split_merge_sort(input, 0, len(input)-1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], sorted_list)

    def test_split_merge_sort_odd_numbered_list(self):
        input = [9, 5, 3, 7, 6, 8, 2, 4, 1]
        sorted_list = _split_merge_sort(input, 0, len(input)-1)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], sorted_list)

    def test_merge_sort(self):
        input = [5, 3, 7, 6, 8, 2, 4, 1]
        sorted_list = merge_sort(input)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], sorted_list)

    def test_merge_sort_odd_numbered_list(self):
        input = [9, 5, 3, 7, 6, 8, 2, 4, 1]
        sorted_list = merge_sort(input)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], sorted_list)

if __name__ == '__main__':
    unittest.main()