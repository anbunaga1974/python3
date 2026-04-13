students=[]
n=int(input("Enter no. of students:"))
for i in range(n):
    s_id=int(input("Enter student id:"))
    name=input("Enter student name:")
    marks=int(input("Enter student marks:"))
    student=(s_id,name,marks)
    students.append(student)
students=tuple(students)
print("\nStudent details:")
for  s in students:
    print("ID:",s[0],"Name:",s[1],"Marks:",s[2])
key=int(input("\nEnter student id:"))
f=0
for s in students:
   if s[0]==key:
      print("Student found")
      print("ID:",s[0],"Name:",s[1],"Marks",s[2])
      f=1
if not f:
   print("Student not found")
max=students[0]
for s in students:
   if s[2]>max[2]:
      max=s
print("\nStudent with highest marks:")
print("ID:",max[0],"Name",max[1],"Marks",max[2])
print("\nStudents with less than 40 marks")
for s in students:
   if s[2]<40:
      print("ID:",s[0],"Name:",s[1],"Marks:",s[2])
total=0
for s in students:
   total=total+s[2]
avg=total/len(students)
print("\nAverage Marks:",avg)
