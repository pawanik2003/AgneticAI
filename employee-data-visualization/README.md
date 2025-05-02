# Employee Data Visualization Project

This project generates and visualizes employee data using Python. It includes scripts to create a CSV file with sample employee data and to visualize that data using popular libraries.

## Project Structure

```
employee-data-visualization
├── src
│   ├── create_employee_data.py
│   ├── visualize_employee_data.py
├── data
│   └── employee_data.csv
├── requirements.txt
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd employee-data-visualization
   ```

2. **Create a virtual environment (optional but recommended):**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Generate Employee Data:**
   Run the following script to create the `employee_data.csv` file:
   ```
   python src/create_employee_data.py
   ```

2. **Visualize Employee Data:**
   After generating the data, run the visualization script:
   ```
   python src/visualize_employee_data.py
   ```

## Visualizations

The visualizations will include:
- Bar charts representing employee distribution by department.
- Pie charts showing salary ranges.

## License

This project is licensed under the MIT License.