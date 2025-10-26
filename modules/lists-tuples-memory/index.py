arr = [10, 2, 3, 5]
arr2 = [1, 2]

first_elem, *rest, last_elem = arr2
print((first_elem + last_elem, sum(rest)))

arr[0] = 10
arr[-1] = 50
print(arr)
arr.append(60)
print(arr)
arr.insert(2, 25)
print(arr)
arr.extend([70, 80, 90])
print(arr)
arr.reverse()
print(arr)
arr.append(4)
arr.remove(4)
print(arr)
arr.pop(0)
arr.extend((1, 2))
print(arr)
arr2 = arr.copy()
print(arr2)
index = arr.index(25)
print(index)
filtered_arr = arr[1:4]
print(filtered_arr)
a, b, *rest, c = arr
print(a, b, c)
t = 1, 2, 3,
print(t)
print(type(t))

numbers = [1, 2, 3, 4]

list_a = numbers
list_b = list_a
list_a[1] = 99

print(list_a)
print(list_b)


numbers = [1, 2, 3, 4, 5, 6]
first_three = numbers[0:3]
last_two = numbers[-2:]
every_second = numbers[::2]
print(first_three)
print(last_two)
print(every_second)
print(numbers + numbers)
print(numbers * 2)


numbers = [1, 2, 3]
var_1 = var_2 = numbers
print(id(var_1))
print(id(var_2))
print(var_1 is var_2)
print(var_1 == var_2)

numbers = [1, 2, 3, 4]
copy_list = numbers.copy()
slice_copy = numbers[:]
print(numbers)
print(slice_copy)
print(copy_list)
print(slice_copy is copy_list)
print(slice_copy == copy_list)
copy_list[1] = 99
print(copy_list)
