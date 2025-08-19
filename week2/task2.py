# create an empty list
my_list = [] 

# append elements in my_list
my_list.extend([10, 20, 30, 40])

# insert 15 at second position
my_list.insert(1, 15)

# extend with another list
my_list.extend([50, 60, 70])

# remove the last item
my_list.pop()

#sort in ascending order
my_list.sort()

# Find and print the index of 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)