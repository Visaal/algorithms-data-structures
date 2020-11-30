# Process steps with example list of [3, 5, 7, 9, 1, 4]:
# - Pick pivot point (convention to take value at end) => index 5 value 4
# - Compare pivot value to first element => 4 to 3
# -- if pivot value larger do nothing else swap logic => 4 > 3
# -- Compare pivot value to second element => 4 to 5
# -- if pivot value larger do nothing else swap logic => 4 < 5 so SWAP => [3, 1, 7, 9, 4, 5]
# ----- SWAP LOGIC:
# --------- Move 5 to index point after the pivot
# --------- Move 4 (pivot) to pivot index -1
# --------- Move 1 (value in pivot index -1) to index point of 5
# -- Compare pivot value to second element as this has ben swapped => 4 to 1 => nothing to do
# -- Compare pivot value to third element => 4 to 7
# -- if pivot value larger do nothing else swap logic => 4 < 7 so SWAP => [3, 1, 9, 4, 7, 5]
# -- Compare pivot value to second element as this has ben swapped => 4 to 9 => SWAP => [3, 1, 4, 9, 7, 5]
# STOP -> Pivot index is now at the comparison index point so everything on left of pivot is smaller, on right is bigger
# START from beginning for the two sides of the list (initial pivot is in correct place)
# - left side is [3, 1 ... AND the right side is .... 9, 7, 5]
# REPEAT until left side start and end indexes equal the new pivot index AND the right side index start and end indexes equal the new pivot


def _split_list(pivot, left_index, right_index):
    left_start = left_index
    left_end = pivot - 1
    right_start = pivot + 1
    right_end = right_index
    return left_start, left_end, right_start, right_end


def _sort_pivot(input_list, left_index, right_index):
    pivot = right_index
    compare_index = left_index
    while pivot != compare_index:
        if input_list[pivot] < input_list[compare_index]:
            # move pivot -1 to compare index
            input_list[compare_index], input_list[pivot - 1] = input_list[pivot - 1], input_list[compare_index]
            # swap pivot index and pivot index-1
            input_list[pivot], input_list[pivot - 1] = input_list[pivot - 1], input_list[pivot]
            # move the pivot index back one to where the pivot now is
            pivot = pivot - 1
        else:
            compare_index += 1

    # Sort the left and right sections of the list recursively
    left_start, left_end, right_start, right_end = _split_list(pivot, left_index, right_index)
    if left_start < left_end:
        _sort_pivot(input_list, left_start, left_end)
    if right_start < right_end:
        _sort_pivot(input_list, right_start, right_end)

    return input_list


def quick_sort(input_list):
    right_index = len(input_list) - 1
    left_index = 0
    return _sort_pivot(input_list, left_index, right_index)
