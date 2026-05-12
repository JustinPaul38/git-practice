
#Part I
print("part 1")
workshopA = set()
workshopB = set()

participants_A = ["Anna","Mark","John","Liza","Carlos"]
participants_B = ["Mark","John","Sofia","Liza","David"]

workshopA.update(participants_A)
workshopB.update(participants_B)
print("Workshop A partipants: ", workshopA)
print("Wrkshop B participants: ", workshopB)

print("Workshop A patricipants number: ", len(workshopA))
print("Workshop B patricipants number: ", len(workshopB))

all_participants = workshopA.union(workshopB)
print("Workshop A and B participants: ", all_participants)

print("Workshop A attendees: ", workshopA)

unique_names = workshopA.union(workshopB)
print("Unique names of attendee: ", unique_names)
print("Unique names: ", workshopA.symmetric_difference(workshopB))

workshopA.remove("Anna")
workshopB.discard("Carlos")
workshopA.pop()
print("Updated list of workshop A: ", workshopA)
print("Updated list of workshop B: ", workshopB)

# Part II
print("Part 2")
Product = {
    "Laptop" : 4500,
    "Mouse": 500,
    "Keyboard" : 1200,
    "Monitor": 8000
}
#display keyboard price
print("Keyboard Price: ", Product["Keyboard"])
#
Product["Headset"]= 1500
print(Product)
Product["Mouse"] = 650
Product.pop("Monitor")
print("Remove monitor from the dicitonary: ",Product)

#Part III
print("part 3")
students = [
    {"name": "Anna", "Age": 20, "course": "IT", "grade": 90},
    {"name": "Mark", "Age": 21, "course": "CS", "grade": 85},
    {"name": "Liza", "Age": 19, "course": "IT", "grade": 88},
    {"name": "John", "Age": 22, "course": "IS", "grade": 92}   
]
#display name
print("Name of All Students: ",students)

#display students taking IT course
print("Students Taking IT course: ", students[0]["name"],students[2]["name"])

#Find Student with the Highest Grade
print("Students who have the highest grade: ", students[3]["name"])
#compute All the Average
computed_grade = (90 + 85 + 88 + 92) / 4
print("Computed grade of all students: ", computed_grade)
#Add new STudent Record
new_studentrec =  {"name": "Carlo", "Age": 20, "course": "IT", "grade": 87}
students.append(new_studentrec)
#display the updated LIst
print("Updated List: ",students)