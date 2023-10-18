from typing import List

def even_list(int_list: List[int]) -> List[int]:
    return_list = []
    for i in int_list:
        if i % 2 == 0:
            return_list.append(i)

    return return_list

def sum_of_squares_of_even(even_int_list: List[int]) -> int:
    sum = 0
    for i in even_int_list:
        ii = i*i
        sum = sum + ii
    return sum


def main():
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_int_list = even_list(int_list)
    output = sum_of_squares_of_even(even_int_list)
    print(output)
    
if __name__ == "__main__":
    main()