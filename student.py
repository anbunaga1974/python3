n=int(input("Enter no. of students:"))
students={}
for i in range(n):
    name=input("Enter student name:")
    marks=int(input("Enter marks:"))
    students[name]=marks
search=input("Enter student name to find marks:")
if search in students:
    print("Marks:",students[search])
else:
    print("Student not found")
