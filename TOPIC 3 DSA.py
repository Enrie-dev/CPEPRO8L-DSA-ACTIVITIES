def insert_at(arr, index, value):
    new_list = []

    for i in range(index):
        new_list.append(arr[i])

    new_list.append(value)

    for i in range(index, len(arr)):
        new_list.append(arr[i])

    return new_list


numbers = [10, 20, 30, 40]
print(insert_at(numbers, 2, 25))