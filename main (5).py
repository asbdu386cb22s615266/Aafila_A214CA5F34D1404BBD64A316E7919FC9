class  Student:
    def_init_(self,name,roll_number,cgpa):
     self.name=Name
     self.roll_number
     self.cgpa=cgpa
    
def sort_student(student_list):
  #sort the list of student in descending order of CGPA
  sorted_students=sorted(student_list,key=lambda student:student.cgpa,reverse=True)
  return sorted_students

#Examole usage:
Student =[
   Student("Hari","A123",7.8),
   Student("Srikanth","A124",8.9),
   Student("Amit","A125",9.0),
   Student("Rahul","A126",8.5),
 ]

 sort_students=sort_students(Students)

#Print the sorted list of students
for student in sort_students:
  print("Name:{},RollNumber:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa)