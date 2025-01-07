list1 = [1,2,3]

# Addind items

# Insert specifiyng the index
list1.insert(1,55)

# Just append to the list
list1.append(77)

# Extend items to the list
list1.extend([8,9,10])

print(list1, sep=" ")


# remove item from the list
list1.pop(4)

del list1[1]


print(list1, sep=" ")