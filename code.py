# var_name = ['John', True, 3.14, 20]
# print(var_name[2])

# fruits = ["Apple", "Banana", "Guava"]
# print(fruits[-1])

# items = ['John', True, 3.14, 20]

# print(items[:3])

# print(items[1:-1])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 6]

# numbers.count(6)
print(numbers.count(6))

# list append
# add a new number to your list
numbers.append(11)
print(numbers)

# list insert
# list.insert(index,value)
num = [1, 2, 3]
num.insert(2,4)
print(num)

# remove function 
num.remove(2)
print(num)

# list.pop(index)
# list.pop() #if not specified it will delete the last item

num.pop(0)
print(num)

# del list[]
# del var_name #if not specified it will delete the array/list

del num[1]
print(num)

# list.clear() #clears it
num.clear()
print(num)

# copy()
nomber = [1, 2, 3]
namber = nomber.copy()
print("Original list =", nomber)
print("Duplicate list =", namber)

# (+) combining list 
add = nomber + namber
print(add)

# extend function 
# varname.extend(var2)
nomber.extend(namber)
print(nomber)

# reverse list
namber.reverse()
print(namber)

# list.sort() assending order
# list.sort(reverse=True) descending order
namber.sort()
print("Asseding order:", namber)
namber.sort(reverse=True)
print("Desceding order:", namber)

# #Lists/Printing lists

# different_types = ["Susan",1,3.14,True]
# print("1. Original List: ",different_types)

# #Assigning List Items/Update the value according to the index
# different_types[2] = 1
# print("2. Updated list items: ",different_types)

# #Access individual elements
# print("3 individual item: ",different_types[3])

# #Index Range (end index=1)
# print("4. Access Specified Start Index/End Index: ",different_types[1:3])
# print("5. Access index 0 and specified end index: ",different_types[ :2]) 
# print("6. Access specified start index and end index: ",different_types[2:])

# #Length means number of item inside the List
# print("7. Number of items inside the collection: ",len(different_types))

# #Count function is to count how many times an elements occur inside the collection
# print("8. Count this item: ",different_types.count(1))

# #Inserting a value
# different_types.insert(0,15)
# print("9. Inserting a value: "_different_types)

#Nested List

#              0 1 2     3       4
random_list = [1,2,3,[4,5,6],"Susan"]
print("10. Nested List: ",random_list)

#Access individual item inside the nested list
print("11. Access individual item: ",random_list[4])


