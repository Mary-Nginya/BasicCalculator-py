# An empty list use block parenthesis.
my_list = []

# Append elements to the list.*add a single number.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# I want to see the results
print("All values added to the list:", my_list)
# Insert 15 at the second position (starts from 0 on the left.)
my_list.insert(1, 15)
# Check to see what I have now. 
print("The list has 15 in second place from the left:", my_list)

# Extend the list with another list. 
# Extend is same as append but can add more at once/in sequence which makes it better. 
my_list.extend([50, 60, 70])

print('My  list has been extended with 50,60 and 70 at once easily:', my_list)

# Remove the last element. I want to use slicing and negatives here. 
my_list = my_list[:-1]
# Sort the list in ascending order
print("The last number on the list has been removed:",my_list)
my_list.sort()
print("Here comes the ascending order: ",my_list)
# Find and print the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
