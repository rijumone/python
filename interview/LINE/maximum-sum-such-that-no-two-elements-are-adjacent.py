def max_non_adjacent_sum(lst):
    inclusive_sum = 0
    exclusive_sum = 0

    for idx in lst:
        # set current maximum excluding idx
        new_exclusive_sum = exclusive_sum if exclusive_sum > inclusive_sum else inclusive_sum

        # set current maximum including idx
        inclusive_sum = exclusive_sum + idx
        exclusive_sum = new_exclusive_sum

    # return maximum of exclusive_sum and inclusive_sum
    return max(exclusive_sum, inclusive_sum)


if __name__ == '__main__':

    _arr = [1, 2, 3, 1]
    _arr = [4, 1, 1, 4]
    # _arr = [4, 1, 1, 4, 5]
    # _arr = [4, 1, 1, 4, 5, 1]
    _f = max_non_adjacent_sum(lst=_arr)
    print(_f)
    # print(len({'1': 'a', '2': 'a', }))
