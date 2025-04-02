my_list = []
print("Intial empty list:", my_list)

# Append elemts 10,20,30,40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("\nAfter appending 10, 20, 30, 40:", my_list)

# Inserting 15 at the second position
my_list.insert(1, 15)
print("\nAfter inserting 15 at position 2:", my_list)

# Extend with [50, 60,70]
my_list.extend([50, 60, 70])
print("\nAfter extending with [50, 60, 70]: ", my_list)

# Remove the last element
my_list.pop()
print("\nAfter removing the last element: ", my_list)

# Sort in ascending order
my_list.sort()
print("\nAfter sorting: ", my_list)

# Find and print index of 30
print("\nIndex of 30:", my_list.index(30))