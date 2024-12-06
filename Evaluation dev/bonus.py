def mysort(mylist: [int]) -> [int]:
    listcopy = mylist[:]

    list_length = len(list_copy)

    for i in range(list_length):
        for j in range(list_length - i - 1):
            if list_copy[j] > list_copy[j + 1]:
                list_copy[j], list_copy[j + 1] = list_copy[j + 1], list_copy[j]

    return list_copy

if __name == '__main':
    my_list = [17, 19, 8, 40, 1, 7, 22]
    sorted_list = my_sort(my_list)
    print("Liste triée :", sorted_list)


