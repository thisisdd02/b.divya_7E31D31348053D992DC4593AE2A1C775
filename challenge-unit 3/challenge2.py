"""
Challenge 2check

Implement a function called sort_students that takes a list of student objects as
input and sorts the list based on their CGPA (Cumulative Grade Point Average) in 
descending order. Each student object has the following attributes: name (string), 
roll_number (string), and cgpa (float). Test the function with different input
lists of students.
"""
class Student:
    def __init__(self,name,r_no,cgpa):
        self.name = name
        self.r_no = r_no
        self.cgpa = cgpa
        
def sort_students(student_list):
    sort_list = sorted(student_list,key= lambda student: student.cgpa,reverse=True)
    return sort_list

student = [
    Student("hari",221,7.7),
    Student("ram",222,9.3),
    Student("priya",223,8.9),
    Student("raj",224,6.2)
    ]
sort_student = sort_students(student)

for s in sort_student:
    print("Name: {}  Roll no: {} cgpa: {}".format(s.name,s.r_no,s.cgpa))