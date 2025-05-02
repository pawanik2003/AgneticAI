import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the employee data from the CSV file
data = pd.read_csv('..\data\employee_data.csv')

# Function to visualize employee distribution by department
def visualize_department_distribution():
    plt.figure(figsize=(10, 6))
    sns.countplot(data=data, x='department', palette='viridis')
    plt.title('Employee Distribution by Department')
    plt.xlabel('Department')
    plt.ylabel('Number of Employees')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to visualize salary distribution
def visualize_salary_distribution():
    plt.figure(figsize=(10, 6
    sns.histplot(data['salary'], bins=10, kde=True, color='blue')
    plt.title('Salary Distribution of Employees')
    plt.xlabel('Salary')
    plt.ylabel('Frequency')
    plt.tight_layout()
    plt.show()

# Main function to run visualizations
if __name__ == "__main__":
    visualize_department_distribution()
    visualize_salary_distribution()