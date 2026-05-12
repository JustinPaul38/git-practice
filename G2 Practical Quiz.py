print("1. What are your favorite subjects?")
list = [input(), input(), input()]

print("2. My favorite subjects are:", list[0], list[1], list[2])

print("\n3. Add another subject to the list:")
list.append(input())

print("\n4. My new favorite subjects are:", list)

print("\n5. What subject would you like to remove from the list?")
list.remove(input())

print("\n6. My updated favorite subjects are:", list)
print("The total number of subjects in my list is:", len(list))

list.sort()
print("\n7. My favorite subjects in alphabetical order are:", list)

