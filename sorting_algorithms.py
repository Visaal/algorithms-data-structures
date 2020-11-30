def _compare_number(num1, num2):
    if num1 > num2:
        return True
    else:
        return False


def _move_largest_number_to_right(unsorted_list, pass_of_list_count):
    # pass_of_list_count used to avoid comparing against the number on the far right that are already sorted
    for x in range(len(unsorted_list) - pass_of_list_count):
        number_on_right_smaller = _compare_number(unsorted_list[x], unsorted_list[x + 1])
        if number_on_right_smaller:
            unsorted_list[x], unsorted_list[x + 1] = unsorted_list[x + 1], unsorted_list[x]
    return unsorted_list


def bubble_sort(list_to_sort):
    # Use start, stop, interval Range options to keep track of the number of passes through the list
    # After a pass the number on the right of the list is sorted so would not need to be compared
    for x in range(1, len(list_to_sort), 1):
        _move_largest_number_to_right(list_to_sort, x)
    return list_to_sort


def _move_smallest_number_to_left(unsorted_list, list_position_to_compare_from):
    for x in range(list_position_to_compare_from, 0, -1):
        number_on_left_bigger = _compare_number(unsorted_list[x - 1], unsorted_list[x])
        if number_on_left_bigger:
            unsorted_list[x], unsorted_list[x - 1] = unsorted_list[x - 1], unsorted_list[x]
    return unsorted_list


def insertion_sort(list_to_sort):
    for x in range(1, len(list_to_sort), 1):
        number_on_left_bigger = _compare_number(list_to_sort[x - 1], list_to_sort[x])
        if number_on_left_bigger:
            _move_smallest_number_to_left(list_to_sort, x)
    return list_to_sort


def _find_smallest_number(list_to_sort, list_position_to_compare_from):
    smallest_number = list_to_sort[list_position_to_compare_from]
    for x in range(list_position_to_compare_from, len(list_to_sort) - 1, 1):
        if _compare_number(smallest_number, list_to_sort[x + 1]):
            smallest_number = list_to_sort[x + 1]
    return smallest_number


def selection_sort(list_to_sort):
    for x in range(0, len(list_to_sort) -1, 1):
        smallest_number = _find_smallest_number(list_to_sort, x)
        smallest_number_index = list_to_sort.index(smallest_number)
        list_to_sort[x], list_to_sort[smallest_number_index] = list_to_sort[smallest_number_index], list_to_sort[x]
    return list_to_sort


def _determine_midpoint(left_index, right_index):
    return left_index + ((right_index - left_index)//2)


def _split_list(left_index, right_index):
    midpoint = _determine_midpoint(left_index, right_index)
    left_start = left_index
    left_end = midpoint
    right_start = midpoint + 1
    right_end = right_index
    return left_start, left_end, right_start, right_end


def _merge_list(list, left_index, right_index):
    midpoint = _determine_midpoint(left_index, right_index)

    # Create indexes for left & right sublists to navigate through them incrementally without altering original params
    left_sub_list_start_index = left_index
    right_half_start_index = midpoint + 1

    # Create temp list to store the re-ordered values of the sublist before copying back into the original list
    temp_list = [0] * (right_index - left_index + 1)
    temp_list_index = 0

    # Compare left hand side to right hand side of sublist noting that these have already been sorted and move...
    # ...the lover values into the temp list until we run out of elements on one side
    while left_sub_list_start_index <= midpoint and right_half_start_index <= right_index:
        if list[left_sub_list_start_index] < list[right_half_start_index]:
            temp_list[temp_list_index] = list[left_sub_list_start_index]
            left_sub_list_start_index += 1
        else:
            temp_list[temp_list_index] = list[right_half_start_index]
            right_half_start_index += 1
        temp_list_index += 1

    # Move any remaining values on the left hand side to the temp list
    while left_sub_list_start_index <= midpoint:
        temp_list[temp_list_index] = list[left_sub_list_start_index]
        left_sub_list_start_index += 1
        temp_list_index += 1

    # Move any remaining values on the right hand side to the temp list
    while right_half_start_index <= right_index:
        temp_list[temp_list_index] = list[right_half_start_index]
        right_half_start_index += 1
        temp_list_index += 1

    #  Copy the ordered values from the temp list to the relevant index positions of the original list
    for i in range(0, len(temp_list)):
        list[left_index] = temp_list[i]
        left_index += 1

    return list


def _split_merge_sort(list_to_sort, left_index, right_index):
    # Split list based on index values rather than slicing the list as slicing operator is O(k)
    left_half_start, left_half_stop, right_half_start, right_half_stop = _split_list(left_index, right_index)
    # Recursively split the list until they are broken down to single elements
    if left_half_start < left_half_stop:
        _split_merge_sort(list_to_sort, left_half_start, left_half_stop)
        _split_merge_sort(list_to_sort, right_half_start, right_half_stop)
    # Once elements have been split start recursively merging
    _merge_list(list_to_sort, left_index, right_index)
    return list_to_sort


def merge_sort(list_to_sort):
    left_index = 0
    right_index = len(list_to_sort)-1
    return _split_merge_sort(list_to_sort, left_index, right_index)