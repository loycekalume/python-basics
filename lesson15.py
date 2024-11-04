# inheritance
# error handling
# dates
from datetime import datetime, date


class Employee:
    def __init__(self, name, id_num, dob, gender):
        self.name = name
        self.id_num = id_num
        self.dob = dob
        self.gender = gender
        date_of_birth = datetime.strptime(dob, "%Y-%m-%d")
        self.age = date.today().year - date_of_birth.year

    def print_details(self):
        print(f"Name: {self.name}\n ID: {self.id_num}\nDOB: {self.dob}\nGender: {self.gender}\nAge: {self.age}")

class PermanentEmployee(Employee):
    def __init__(self, name, id_num, dob, gender,salary):
        super().__init__(name, id_num, dob, gender)
        self.salary = salary

    def print_salary(self):
        print(f"Salary is {self.salary}")

    def print_details(self):
        super().print_details()
        print(f"Salary is {self.salary}")

class TemporaryEmployee(Employee):
    def __init__(self, name, id_num, dob, gender,hourly_pay, end_date):
        super(). __init__(name, id_num, dob, gender)
        self.hourly_pay = hourly_pay
        self.end_date = end_date

    def print_hourly_pay(self):
        print(f"Hourly payment is {self.hourly_pay}")

    def print_end_date(self):
        print(f"End date is {self.end_date}")

p1 = PermanentEmployee(salary=10000,name="John Doe",id_num="123456",dob="2001-01-01",gender="Male")
p1.print_details()
p1.print_salary()

t1 = TemporaryEmployee("James","1234567","1997-03-06","Male",1000,"2080-11-12")
t1.print_details()
t1.print_hourly_pay()


