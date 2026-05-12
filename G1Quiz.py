#Part I: Sets (10 points)

# workshopA = {"Ana", "Mark", "John", "Liza", "Carlo"}
# workshopB = {"Mark", "John", "Sofia", "Liza", "David"}

# 1. Create 2 empty sets
workshopA = set()             
workshopB = set()

print("="* 100)

# 2. Add participants of workshop A and B
workshopA.add("Ana")
workshopA.add("Mark")
workshopA.add("John")
workshopA.add("Liza")
workshopA.add("Carlo")

workshopB.add("Mark")
workshopB.add("John")
workshopB.add("Sofia")
workshopB.add("Liza")
workshopB.add("David")

# 4. Display the participants of both workshops
print(f"The participants of Workshop A are: {workshopA}")
print(f"The participants of Workshop B are: {workshopB}")
print("="* 100)

# 5. Display the number of students in each workshop
print(f"The number of students in Workshop A is: {len(workshopA)}")
print(f"The number of students in Workshop B is: {len(workshopB)}")
print("="* 100)

# 6. Display the students who attended both workshop
print(f"The students who attended both workshops are: {workshopA.intersection(workshopB)}")
print("="* 100)

# 7. Display the student who attended only workshop A
print(f"The students who attended only workshop A are: {workshopA.difference(workshopB)}")
print("="* 100)

# 8. Display all unique students who attended any workshop
print(f"The students who attended any workshops are: {workshopA.union(workshopB)}")
print("="* 100)

# 9. Display the students who attended only one workshop
print(f"The students who attended only one workshop are: {workshopA.symmetric_difference(workshopB)}")
print("="* 100)


# Number 10

workshopA.remove("Ana")   # Remove Ana
# workshopB.remove("Carlos")   # Attempt to remove Carlos in Workshop B
workshopA.pop()    # Remove a random student in workshop A

# 11. Display the updated sets
print("="* 100)
print(f"Here are the updated set of workshopA: {workshopA}")
print(f"Here are the updated set of workshopB: {workshopB}")


# =============================================================================================================
# Part II: Dictionaries (10 points)

products = {
    "Laptop": 45000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 8000
}

print("="* 100)

# 1. Display the price of the Keyboard
print(f"The price of the keyboard is: P{products.get("Keyboard")}")
print("="* 100)

# 2. Add a new product
products["Headset"] = 1500

# 3. Update the price of Mouse
products["Mouse"] = 650

# 4. Remove Monitor
products.pop("Monitor")

# 5. Display all products and their prices
print(f"Here are the products and their corresponding prices: {products}")
print("="* 100)


# ==================================================================================================================
# Part III: List of Dictionaries (10 points)

students = [
    {"name": "Anna", "age": 20, "course": "IT", "grade": 90},
    {"name": "Mark", "age": 21, "course": "CS", "grade": 85},
    {"name": "Liza", "age": 19, "course": "IT", "grade": 88},
    {"name": "John", "age": 22, "course": "IS", "grade": 92}
]

print("="* 100)

# 1. Display the names of all students
# print("The name of the students are:")
# for student in students:
#     print(student["name"])
# print("=" * 100)

print(f"The name of the students are: {students[0]["name"], students[1]["name"], students[2]["name"], students[3]["name"]}")
print("="* 100)

# 2. Display the students who are taking the IT course
# print("The name of the students who are taking the IT course are:")
# for student in students:
#     if student["course"] == "IT":
#         print(student["name"])

# print("=" * 100)

print(f"The name of the students who are taking IT course are: {students[0]["name"], students[2]["name"]}")
print("=" * 100)

# 3. Find and display the student with the highest grade
# grades = []
# for student in students:
#     grades.append(student["grade"])

# print(f"The name of the student who has the highest grade is: {max(grades)}")
# print("=" * 100)

print(f"The name of the student who has the highest grade is: {students[3]["name"]}")
print("=" * 100)

# 4. Compute the average grade of all students
# print(f"The average grade of all the students is: {sum(grades) / len(students)}")
# print("=" * 100)

print(f"The average grade of all students is: {(students[0]["grade"] + students[1]["grade"] + students[2]["grade"] + students[3]["grade"]) / len(students)}")
print("=" * 100)

# 5. Add a new student record
students.append({"name": "Carlo", "age": 20, "course": "IT", "grade": 87})

# Display the updated student list
print(f"The updated list: {students}")
print("=" * 100)