def bubble_sort(list):
    counter = 0
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            # print("Intermediate step {0}: {1}".format(counter, list))
            counter += 1
            if list[j] > list [j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list


def bubble_sort_rev(list):
    counter = 0
    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            # print("Intermediate step {0}: {1}".format(counter, list))
            counter += 1
            if list[j] < list [j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    return list

lst = [int(x) for x in input("Please enter unique numbers to be sorted: ").split()]

lst_init = lst.copy()

print("\nInitial list: ", lst_init)
print("Sorted list: ", bubble_sort(lst))
print("Reversed sorted list: ", bubble_sort_rev(lst))
