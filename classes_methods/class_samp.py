import datetime


class Employee:

    num_employees = 0
    role = 'worker'
    raise_amount = 1.04

    def __init__(self, first_name, last_name, salary, department):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.salary_int = int(self.salary.split(' ')[0])
        self.department = department
        self.organization = 'xcompany.com.au'
        self.email = f"{self.first_name}.{self.last_name}@{self.organization}"

        Employee.num_employees += 1
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_annual_salary(self):
        if 'month' in self.salary:
            salary = self.salary_int * 12
        elif 'week' in self.salary:
            salary = self.salary_int * 52.1429
        elif 'day' in self.salary:
            salary = self.salary_int * 260
        else:
            salary = self.salary

        return salary

    def apply_raise(self):
        updated_salary = self.salary_int * self.raise_amount
        return updated_salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        frst_nm, lst_nm, sal, dept = emp_str.split('|')
        return cls(frst_nm, lst_nm, sal, dept)

    @staticmethod
    def is_workday(day):
        if day.weekday() in [5, 6]:
            return False
        return True


def show_basic_emp(emp_list):
    if emp_list:
        print("showing employee basic details")
        for emp in emp_list:
            employee = Employee(emp[0], emp[1], emp[2], emp[3])
            print(f"Basic employee details: name: {employee.full_name()}, email: {employee.email}, department: {employee.department}")
    else:
        raise Exception("input list is empty")


emp_1 = Employee('Marie', 'Ong', '800 per day', 'Educators')
emp_2 = Employee('Jose', 'Diaz', '2800 per month', 'Packaging')
emp_3 = Employee.from_string('Julie|Ong|5400 per month|Accounting')

print(emp_1.salary)
# print(Employee.role)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
#emp_2.raise_amount = 0.05
# print(emp_2.raise_amount)
print(emp_1.get_annual_salary())
print(emp_1.apply_raise())

emp_1.set_raise_amount(1.08)
print(emp_2.raise_amount)
print(emp_3.full_name())
print(emp_3.email)
print(emp_3.get_annual_salary())
print(emp_2.is_workday(datetime.date.today()))


curl "http://canva-interview.com/image.png"




