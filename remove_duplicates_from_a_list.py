my_list = ['a', 'b', 'c', 'a', 'a']

# option 1
list_from_set = list(set(my_list))
print(list_from_set)

# option 2
seen = []
for element in my_list:
    if element not in seen:
        seen.append(element)
print(seen)

# option 3
my_list.sort()
i = 0
while i < len(my_list)-1:
    if my_list[i] == my_list[i+1]:
        my_list.pop(i)
    else:
        i += 1
print(my_list)
