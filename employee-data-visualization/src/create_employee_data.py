import pandas as pd
import random

def create_employee_data(num_employees=100):
    names = [f'Employee {i}' for i in range(1, num_employees + 1)]
    ages = [random.randint(22, 60) for _ in range(num_employees)]
    departments = random.choices(['HR', 'IT', 'Finance', 'Marketing'], k=num_employees)
    salaries = [random.randint(30000, 120000) for _ in range(num_employees)]

    employee_data = pd.DataFrame({
        'Name': names,
        'Age': ages,
        'Department': departments,
        'Salary': salaries
    })

    employee_data.to_csv('../data/employee_data.csv', index=False)

if __name__ == "__main__":
    create_employee_data()