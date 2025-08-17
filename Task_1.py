students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "John": 90,
    "Paul": 95,
    "Rob": 90,
    "Sarah": 90,
}

name=input("Enter student's name: ")

if name in students:
    print(f"{name}'s marks:", students[name])
else:
    print("Student not found")
