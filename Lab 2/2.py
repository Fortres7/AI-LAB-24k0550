class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def calculate_salary(self):
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, hours_worked, hourly_rate):
        super().__init__(name, emp_id)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

E1 = FullTimeEmployee("Omer", 11, 70000)
E2 = PartTimeEmployee("Ahmed", 22, 50, 400)
print("Employee:", E1.name, "Salary:", E1.calculate_salary())
print("Employee:", E2.name, "Salary:", E2.calculate_salary())
