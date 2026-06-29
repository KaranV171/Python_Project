class Employee:
    
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary
    
    def calculate_hra(self):
        return self.basic_salary * 0.20
    
    def calculate_da(self):
        return self.basic_salary * 0.10
    
    def calculate_gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()
    
    def calculate_tax(self):

        return self.calculate_gross_salary() * 0.12
    
    def calculate_net_salary(self):
        return self.calculate_gross_salary() - self.calculate_tax()
    
    def display_salary(self):
        print(f"\n--- Salary Details for {self.name} (ID: {self.emp_id}) ---")
        print(f"Basic Salary:    ₹{self.basic_salary:,.2f}")
        print(f"HRA (20%):       ₹{self.calculate_hra():,.2f}")
        print(f"DA (10%):        ₹{self.calculate_da():,.2f}")
        print(f"Gross Salary:    ₹{self.calculate_gross_salary():,.2f}")
        print(f"Tax (12%):       ₹{self.calculate_tax():,.2f}")
        print(f"Net Salary:      ₹{self.calculate_net_salary():,.2f}")


emp1 = Employee(101, "Rajesh Kumar", 50000)
emp2 = Employee(102, "Priya Sharma", 60000)
emp3 = Employee(103, "Amit Patel", 45000)


emp1.display_salary()
emp2.display_salary()
emp3.display_salary()


print("\n" + "="*50)
print("PAYROLL SUMMARY")
print("="*50)
employees = [emp1, emp2, emp3]
total_net = sum(emp.calculate_net_salary() for emp in employees)
print(f"Total Employees: {len(employees)}")
print(f"Total Net Salary: ₹{total_net:,.2f}")
print("="*50)