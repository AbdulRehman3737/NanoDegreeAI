# Question 1 (Short)

# 1
print("----PROBLEM 1----")
dict = {'name': 'Abdul Rehman', 'age': 27, 'city': 'Lahore'}
print("Dictionary: ", dict.get("city"))

# 2
print("----PROBLEM 2----")
students = {"Abdul": "97", "Rehman": "98", "Mukhtar": "99", "Ahmad": "100"}
for student in students.items():
    print("Name: ", student[0], "- Marks: ", student[1])

# 3
print("----PROBLEM 3----")
def match_statement (x_assign):
    match x_assign:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
    print("Invalid Day")

match_statement(6)

# 4
print("----PROBLEM 4----")
counter = 1
while counter < 11:
    print(counter)
    if counter == 6:
        break
    counter+=1

# 5
print("----PROBLEM 5----")
list_num = [1,2,3,4,5,6,7,8,9,10]
for num in list_num:
    if num != 5:
        print(num)

# 6
print("----PROBLEM 6----")
int_set_1 = {3, 5, 7, 9}
int_set_2 = {4, 5, 6, 8, 10}
print("Union: ", int_set_1.union(int_set_2))
print("Intersection: ", int_set_1.intersection(int_set_2))

# 7
print("----PROBLEM 7----")
tuple_colors = ('Red', 'Blue', 'Green')
colors_list = [x for x in tuple_colors]
colors_list[1] = "Yellow"
tuple_colors = tuple(colors_list)
print("Tuple: ", tuple_colors)

# 8
print("----PROBLEM 8----")
def square(num_arg):
    print("Squared: ", num_arg*num_arg)
square(4)

# 9
print("----PROBLEM 9----")
try:
    file_name = 'data.txt'
    file_obj = open(file_name, 'x')
    with open(file_name, 'w') as w:
        w.write("Python File Handling.\n")
    with open(file_name, 'r') as f:
        print("Reading File: ", f.read())
except:
    print("File Already Exists")

# 10
print("----PROBLEM 10----")
input_assign = input('Enter Numeric Number: ')
try:
    int_val = int(input_assign)
    print("Correct Type")
except ValueError:
    print("ValueError - Incorrect Type")

# -------------------------------------------------------------------------

# Question 2 (Long)
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, title, first_name, last_name, given_name, birth_date, gender, address, phone, number):
        self.title = title
        self.first_name = first_name
        self.last_name = last_name
        self.given_name = given_name
        self.birth_date = birth_date
        self.gender = gender
        self.address = address
        self.phone = phone
        self.number = number

    @abstractmethod
    def is_faculty(self):
        pass

class Hospital():
    def __init__(self, name, address, phone_no):
        self.name = name
        self.address = address
        self.phone_no = phone_no

class Patient(Person):
    def __init__(self, title, first_name, last_name, given_name, birth_date, gender, address, phone, number, sickness_history, prescription, allergies, spec_req):
        super().__init__(title, first_name, last_name, given_name, birth_date, gender, address, phone, number)
        self.department = sickness_history
        self.prescription = prescription
        self.allergies = allergies
        self.spec_req = spec_req

    def is_faculty(self):
        return False

class Staff(Person, ABC):
    def __init__(self, title, first_name, last_name, given_name, birth_date, gender, address, phone, number, joining_date, education, certs, langs):
        super().__init__(title, first_name, last_name, given_name, birth_date, gender, address, phone, number)
        self.joining_date = joining_date
        self.education = education
        self.certs = certs
        self.langs = langs

    def is_faculty(self):
        return True

class Nurses(Staff):
    def __init__(self, title, first_name, last_name, given_name, birth_date, gender, address, phone, number, joining_date, education, certs, langs, specialty, trainee = False):
        super().__init__(title, first_name, last_name, given_name, birth_date, gender, address, phone, number, joining_date, education, certs, langs)
        self.specialty = specialty
        self.trainee = trainee

    def is_faculty(self):
        return True

    def isTrainee(self):
        if self.trainee == True:
            return True

class Doctors(Staff):
    def __init__(self, title, first_name, last_name, given_name, birth_date, gender, address, phone, number, joining_date, education, certs, langs, residency_year = False, degree = False, time_since_consult = False):
        super().__init__(title, first_name, last_name, given_name, birth_date, gender, address, phone, number, joining_date, education, certs, langs)
        self.residency_year = residency_year
        self.degree = degree
        self.time_since_consult = time_since_consult

    def is_faculty(self):
        return True

    def isResident(self):
        if self.residency_year != False:
            return True

    def isConsultant(self):
        if self.time_since_consult != False:
            return True

# Many more staffs, same method as above

class Department(Hospital):
    def __init__(self, name, address, phone_no, dpartment_name, department_location, department_number, staff_member):
        super().__init__(name, address, phone_no)
        self.dpartment_name = dpartment_name
        self.department_location = department_location
        self.department_number = department_number
        self.staff_member = staff_member

# Many more departments, same as above, time limitation to describe all of them.

# Person Entity example, all will be same as this: Patient, Doctor, Nurses, Consultant etc
patient = Patient('Zero', "Mr.Cruise", 'De Niro', 'AtaUllah', '01/01/2001', 'Male', 'Lahore', '090078601', '0528415123', 'No history', 'Nethromyzin', 'Water Allergy', 'Blood Infusions')
print("Patient: ", patient.first_name, patient.last_name, patient.number)

doctor = Doctors('Master', "Mr.Bond", 'Killue', 'Mubashir Khan', '01/01/2001', 'Male', 'Lahore', '090078601', '0528415123', '01/01/2003', 'FCPS', 'MRCP', 'English', 2004, 'MRCP')

department = Department("Jinnah", 'Canal', '03124421', 'Cardiology', 'East wing', '03', doctor)
print('Department: ', department.name, department.dpartment_name, department.department_location, department.staff_member.first_name, department.staff_member.degree)