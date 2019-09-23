###  Lists ###

# A list is merely a collection of items. We can define a list like so:
my_list = [] # This defines an empyt list
my_list2 = [1, 2, 3] # This defines a list with a collection of integers

# If we want to get an item from the list, we can do so by calling the position of the item
# The position starts at 0 for the first element, 1 for the second, and so on.
# It continues to count up all the way to n - 1.
print(my_list2[0]) # Get the first element
print(my_list2[1]) # Get the second element
# print(my_list2[3]) # This will fail because there aren't 4 elements in the list

# To add items to our list, we can do it two ways
my_list.append('Dave') # This adds an item to the end of the list
my_list.append('Mac')
my_list.append('Ben')
my_list.append('Brodie')
print(my_list)

# Like in class, Mac and Ben tend to not get along, so we can insert Sam between them
my_list.insert(2, 'Sam') # Here we want to insert Sam at position 2 and shift everyone else down
print(my_list)

# To find what position someone is, we can use index
print(my_list.index('Brodie')) # This will give me the position he is in

# We can keep going further and define a list of lists, which is just a collection within a collection
mac = ['Coffee', 'Phone', 'Wallet']
sam = ['Water', 'Phone']
students = [mac, sam]

print(students)

# How can I get Mac's Coffee from students?
print(students[0][0]) # This says, give me the first item in the list, followed by the first item in the second list

# If we just did
print(students[0]) # We'd get the list; mac

# Now like I said earlier, Ben and Mac don't get along very well, and so Ben stole Mac's wallet.
# How can we adjust that list to no longer include Mac's wallet?
mac.pop() # This removes the last element on the list
print(mac)

# I stepped in and gave Mac his wallet back, but in a different location
mac.insert(1, 'Wallet')
print('Mac:', mac)

# However Ben is pretty crafty so he managed to steal it again. This time though, he found the index of Mac's wallet and removed it.
macs_wallet_location = mac.index('Wallet')
mac.pop(macs_wallet_location)
print('Mac:', mac)

# Alternatively, he could have just done:
# mac.remove('Wallet') # And would have achieved the same effect.

# Now say I want to select a group of students, we can do something called list slicing and it looks like this:
print(my_list[1:3]) # Notice the use of the : operator
# What this did was take the element from position 1 up to, but not including, position 3

# This operator is kinda cool, we can do things like:
print(my_list[2:]) # Print everything in my_list after and including position 2
print(my_list[:2]) # Print everything in my_list up to position 2
print(my_list[-1]) # Print the last element in the list

### Tuples ###