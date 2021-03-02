#each method within a class automatically takes in instance as first parameter


class Employee:

    raise_amount = 2
    no_of_employee = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        Employee.no_of_employee += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

    @staticmethod
    def is_work_day(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

import datetime
my_date=datetime.date(2016,7,11)
print(Employee.is_work_day(my_date))


#print(Employee.no_of_employee)
emp_1 = Employee("John", "Doe", 500000)
emp_2 = Employee("Monney", "Penny", 60000)
#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'Steve-Smith-30000'
#emp_str_3 = 'Jane-Doe-90000'
#new_emp_1=Employee.from_string(emp_str_1)
#print(new_emp_1.email)
#print(new_emp_1.pay)
#print(new_emp_1.first)
#Employee.set_raise(10)
#emp_2.set_raise(6)
#print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
#print(Employee.no_of_employee)
#emp_1.raise_amount=5
#print(emp_1.__dict__)
#print(Employee.__dict__)
#emp_1.apply_raise()
#emp_2.apply_raise()
#print(emp_1.pay)
#print(emp_2.pay)
#print(emp_1.email)
#print(emp_2.email)
#print(emp_1.fullname())
#print(Employee.fullname(emp_2))
