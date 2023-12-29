# sample_list = [1, 2, 3]
# sample_list = [1, 'a', '3', True, 'one', 'two', 'three', 4, 5]
# print(len(sample_list))
# print(sample_list[::2]) # [1, '3', 'one', 'three', 5]
# print(sample_list[::-1]) # reversing order-->[5, 4, 'three', 'two', 'one', True, '3', 'a', 1]
# sample_list = sample_list + [6, 7, 8]

# sample_list *= 2 # will be extended 2 times

# append(), extend()
# sample_list = [1, 2, 3]
# sample_list.append(4)
# sample_list.append([6, 7, 8])
# sample_list.extend([6, 7, 8])
# print(sample_list)

# sample_list = [1, 2, 3, 4, [6, 7, 8], 6, 7, 8]
# ele = sample_list.pop(0) # it will remove/pop off 0th index-->1 in sample_list and stores in ele
# print(ele)
# sample_list.reverse()
# sample_list = ['c', 'b', 'a', 'e', 'd', 'f']
#sample_list.sort() # it will affect original list
# sample_list_sorted = sorted(sample_list) # it will not affect original list
# print(sample_list_sorted)
# print(sample_list)

## Nesting lists
# sample_list = [1, 2, 3, 4, [60, 70, 80], 6, 7, 8]
# print(sample_list[4][0]) # print 0th index of 4th index.4th index is [60, 70, 80]

# creating nesting list
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# sample_list = [list1, list2] # [[1, 2, 3], [10, 20, 30]]

# sample_list = [[1, 2, 3], [10, 20, 30]]
# print(sample_list[1][1]) # 20

## List unpacking
a, b, c = 1, 2, 3
print(a, b, c) # unpacking

## swaping values
a = 1
b = 2
a, b = b ,a
print(a, b) # a=2, b=1 values swapped

sample_list = [1, 2, 3, 4, [60, 70, 80], 6, 7, 8]
sample_list[-2] = 700
sample_list[0] = 100
sample_list = sample_list[::-1] # reversing order
print(sample_list)