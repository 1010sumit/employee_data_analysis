from datetime import datetime

def parse_time(time_str):
    if time_str:
        return datetime.strptime(time_str, "%m/%d/%Y %I:%M %p")
    else:
        return None

def analyze_employee_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    header = lines[0].strip().split('\t')
    data = [line.strip().split('\t') for line in lines[1:]]

    # Find the index of relevant columns in the header
    position_id_index = header.index('Position ID')
    time_index = header.index('Time')
    time_out_index = header.index('Time Out')
    employee_name_index = header.index('Employee Name')

    employee_shifts = {}

    for row in data:
        position_id = row[position_id_index]
        time_in = parse_time(row[time_index])
        time_out = parse_time(row[time_out_index])
        employee_name = row[employee_name_index]

        if employee_name not in employee_shifts:
            employee_shifts[employee_name] = []

        if time_in and time_out:
            shift_duration = (time_out - time_in).seconds / 3600
            employee_shifts[employee_name].append({
                "position_id": position_id,
                "time_in": time_in,
                "time_out": time_out,
                "shift_duration": shift_duration
            })

    for employee_name, shifts in employee_shifts.items():
        print(f"\n{employee_name} has the following issues:")

        # Check for shifts longer than 14 hours
        for shift in shifts:
            if shift["shift_duration"] > 14:
                print(f"{employee_name} has worked for more than 14 hours in a single shift.")

        # ... (add other checks as needed)

# Example usage:
file_path = "employee_data.csv"
analyze_employee_data(file_path)
