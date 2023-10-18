def even_list(int_list: List[int]) -> List[int]:
    return_list = []
    for i in int_list:
        if i % 2 == 0:
            return_list.append(i)

    return return_list
