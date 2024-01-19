import csv
from datetime import datetime, timedelta

def read_csv(file_path):
    """
    Reads data from a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file.
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]
    return data

def find_consecutive_days_employees(data):
    """
    Finds employees who have worked for 7 consecutive days.
    """
    consecutive_days_employees = set()
    
    for employee in set(row['Employee Name'] for row in data):
        consecutive_days_count = 0
        last_date = None
        
        for row in data:
            if row['Employee Name'] == employee:
                current_date = datetime.strptime(row['Date'], '%Y-%m-%d')
                
                if last_date is not None and (current_date - last_date).days == 1:
                    consecutive_days_count += 1
                else:
                    consecutive_days_count = 1
                
                last_date = current_date
                
                if consecutive_days_count == 7:
                    consecutive_days_employees.add(employee)
                    break
    
    return consecutive_days_employees

def find_short_time_between_shifts_employees(data):
    """
    Finds employees who have less than 10 hours of time between shifts but greater than 1 hour.
    """
    short_time_between_shifts_employees = set()
    
    for employee in set(row['Employee Name'] for row in data):
        shifts = [datetime.strptime(row['Date'], '%Y-%m-%d') for row in data if row['Employee Name'] == employee]
        shifts.sort()
        
        for i in range(1, len(shifts)):
            time_between_shifts = shifts[i] - shifts[i - 1]
            
            if timedelta(hours=1) < time_between_shifts < timedelta(hours=10):
                short_time_between_shifts_employees.add(employee)
                break
    
    return short_time_between_shifts_employees

def find_long_single_shift_employees(data):
    """
    Finds employees who have worked for more than 14 hours in a single shift.
    """
    long_single_shift_employees = set()
    
    for row in data:
        hours_worked = float(row['Hours Worked'])
        
        if hours_worked > 14:
            long_single_shift_employees.add(row['Employee Name'])
    
    return long_single_shift_employees

if __name__ == "__main__":
    # Assume the input file is named "employee_data.csv"
    file_path = "employee_data.csv"
    
    # Read data from the CSV file
    data = read_csv(file_path)
    
    # Find and print employees who meet the specified conditions
    print("Employees who have worked for 7 consecutive days:", find_consecutive_days_employees(data))
    print("Employees with less than 10 hours between shifts but greater than 1 hour:", find_short_time_between_shifts_employees(data))
    print("Employees who have worked for more than 14 hours in a single shift:", find_long_single_shift_employees(data))
