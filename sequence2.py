# 1
# list is an ordered sequence of items, most used datatype 
# can hold multiple datatype 

my_list=[1,2,3,4,5,6,7,8,9,10]

# here we see bulit in method to manipluate lists

print(len(my_list))
print(my_list[0])
print(my_list[-1])   # this is accessong reversely the last element 
print(my_list[2: 6])  # used to slice the string and display the sub string form index 2 to 6 (not including 6)


print(my_list.sort(reverse=True))

my_list.append(26) #used to add a member(26) to our list at end
print("this is a list afrer using append elemnt and add 26 at the end ", my_list)

my_list.insert(0, 0) # we use insert to append a member at specfic index 
print("this is a list after inserting 0  at specific index ", my_list)

my_list.extend([34,67,88,99])    # used to append another list at the end
print("this is a list after using extend to add other list at end ", my_list)


#2
# tuple is an ordered sequence of items same as list 
# the only difference is tuples are immutable : means
#can not be modified once it is defined
mytuple=(1, 2, 3, 4, 5, 6)

print( mytuple[2])


#3
# set use curly brace that end by  ''  to differentiate it form the dictionary
# set will ignore repeated values
# set is unordered collection of unique elements 
# dictionaries also used curly brace 

myset={1,2 ,3, ''}
# myset2=set(1,2,3)

#4
# dictionary is unorder collection of unique items
# has concept of key: value ... here use key to access the value
# we can not have two simlar keys in a single dictionaries

mydiction= {'name': 'sami', 'age': 23, 'gender': 'male'}

# here let us check bulit in methods for manipulating 
print(mydiction['name'])   # here the value will be print out

# or we can use get function
print(mydiction.get('name'))  # simlar with the above using get method



# now let us check our datatype for each and print it out :) 

print(type(my_list))
print(type(mytuple))
print(type(myset))
print(type(mydiction))