def selection_sort(list):
    for n in range(len(list)):
        min_index = n
        for i in range(n + 1, len(list)):
            if list[min_index] > list[i]:
                min_index = i
        list[n], list[min_index] = list[min_index], list[n]
    return list

def selection_sort_rev(list):
    for n in range(len(list)):
        max_index = n
        for i in range(n + 1, len(list)):
            if list[max_index] < list[i]:
                max_index = i
        list[n], list[max_index] = list[max_index], list[n]
    return list


nums = [int(x) for x in input("Please enter numbers to be sorted separated by a space: ").split()]

print("Initial list: ", nums)
print("Sorted list: ", selection_sort(nums))
print("Reverse sorted list: ", selection_sort_rev(nums))
