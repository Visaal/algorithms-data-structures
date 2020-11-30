def binary_search(input_list, target):
    floor = 0
    ceiling = len(input_list) - 1

    while floor <= ceiling:

        midpoint = floor + (ceiling - floor)//2

        # print('floor: ', floor, '\tceiling: ', ceiling, '\tmidpoint: ', midpoint)

        if target == input_list[midpoint]:
            return midpoint
        else:
            if target < input_list[midpoint]:
                ceiling = midpoint - 1
            else:
                floor = midpoint + 1
    return -1
