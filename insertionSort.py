testlist = [5, 3, 2, 1, 4]


def insertionSort(list, length):
    for index in range(1, length):
            key = list[index]
            i = index - 1
            while i >= 0 and list[i] > key:
                list[i+1] = list[i]
                i = i-1
            list[i+1] = key
    return list


testlistResult = insertionSort(testlist, len(testlist))
print(testlistResult)
