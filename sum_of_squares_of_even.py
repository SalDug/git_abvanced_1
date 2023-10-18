def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum = 0
    for i in even_int_list:
        ii = i*i
        sum = sum + ii
    return sum