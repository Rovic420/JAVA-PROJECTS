# IMPORTS
from datetime import datetime, timedelta

# DATABASE
employee_database = {}
timekeeping_entries = {}

# MAIN MENU
def main_menu():
    while True:
        print(Bar01)
        print(DateTimeIndicator)
        print("1. TIMEKEEPING")
        print("2. REGISTER EMPLOYEE")
        print("3. VIEW EMPLOYEE")
        print("4. EXIT")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            timekeeping_screen()
        elif choice == "2":
            register()
        elif choice == "3":
            view_employee(timekeeping_entries)
        elif choice == "4":
            print(Bar01)
            print(DateTimeIndicator)
            print(Bar03)
            print(Bar02)
            break
        else:
            print("Invalid input. Please select a valid option.")

# TIMEKEEPING SCREEN
def timekeeping_screen():
    print(Bar04)
    print(DateTimeIndicator)
    while True:
        employee_id = input("Enter Employee ID: ")
        if employee_id not in employee_database:
            print("Invalid Employee ID. Please register the employee first.")
            return

        start_date = input("Enter Start Date (YYYY-MM-DD): ")
        end_date = input("Enter End Date (YYYY-MM-DD): ")

        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

        if end_date < start_date:
            print("\nEnd Date cannot be prior to Start Date. Please try again.")
            return

        timekeeping_entries.setdefault(employee_id, {})
        
        period = f"{start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
        timekeeping_entries[employee_id].setdefault(period, {"entries": []})
    
        for single_date in (start_date + timedelta(n) for n in range((end_date - start_date).days + 1)):
            date_str = single_date.strftime("%Y-%m-%d")

            if date_str not in timekeeping_entries[employee_id][period]:
                attendance = input(f"\nIs the employee present on {date_str}? (yes/no): ")
                if attendance.lower() == "yes":
                    time_in = input(f"Enter Time-In for {date_str} (HH:MM): ")
                    time_out = input(f"Enter Time-Out for {date_str} (HH:MM): ")

                    if time_in > time_out:
                        print("\nTime-Out cannot be prior to Time-In. Please try again.")
                        return

                    timekeeping_entries[employee_id][period]["entries"].append({
                        "date": date_str,
                        "time_in": time_in,
                        "time_out": time_out,
                        "total_hours": calculate_total_hours(time_in, time_out),
                        "total_absences": 0,
                    })
                elif attendance.lower() == "no":
                    timekeeping_entries[employee_id][period]["entries"].append({
                        "date": date_str,
                        "time_in": "A",
                        "time_out": "A",
                        "total_hours": 0,
                        "total_absences": 1,
                    })
                else:
                    print("\nInvalid input. Please enter 'yes' or 'no'.")
                    return
            else:
                print(f"\nTime entries already exist for {date_str} in {period}.")

        another_transaction = input("\nDo another transaction? (yes/no): ")
        if another_transaction.lower() != "yes":
            return

def calculate_total_hours(time_in, time_out):
    if time_in.lower() == 'a' and time_out.lower() == 'a':
        return 0
    in_time = datetime.strptime(time_in, "%H:%M")
    out_time = datetime.strptime(time_out, "%H:%M")
    hours_worked = (out_time - in_time).total_seconds() / 3600
    return round(hours_worked, 2)

# REGISTER EMPLOYEE
def register():
    print(Bar05)
    print(DateTimeIndicator)
    while True:
        print(">> Employee Details")
        employee_id = input(" Enter New Employee ID: ")
            
        if employee_id not in employee_database:
            first_name = input(" Enter First Name: ")
            last_name = input(" Enter Last Name: ")

            while True:
                choice = input(" Enter Department (1)Faculty (2)Non-Faculty: ")
                if choice == "1":
                    department = "Faculty"
                    break
                elif choice == "2":
                    department = "Non-Faculty"
                    break
                else:
                    print("INCORRECT CHOICE! TRY AGAIN!")

            while True:
                choice2 = input(" Enter Position (1)Full-Time (2)Part-Time: ")
                if choice2 == "1":
                    job_position = "Full-Time"
                    break
                elif choice2 == "2":
                    job_position = "Non-Faculty"
                    break
                else:
                    print("INCORRECT CHOICE! TRY AGAIN!")
                
            employee_database[employee_id] = {
                "First Name": first_name,
                "Last Name": last_name,
                "Department": department,
                "Position": job_position,
            }
                
            print("\nEmployee registered successfully.")
        else:
            print("\nEmployee already registered.")

        another_transaction = input("\nDo you want to register another employee? (Y/N): ")
        print()
        if another_transaction.lower() != "y":
            break

# VIEW EMPLOYEE
def view_employee(timekeeping_entries):

    print(Bar06)
    print(DateTimeIndicator)
    while True:
        employee_id = input("Enter Employee ID: ")

        if employee_id in employee_database:    
            print("\n>> Employee Details")
            employee_info = employee_database[employee_id]
            print(f" First Name: {employee_info['First Name']}")
            print(f" Last Name: {employee_info['Last Name']}")
            print(f" Department: {employee_info['Department']}")
            print(f" Position: {employee_info['Position']}")
            
            print("\n>> TimeKeeping Entries")
            if employee_id in timekeeping_entries:
                for period, entries_info in timekeeping_entries[employee_id].items():
                    print(f"*Date Period: {period}")
                    total_hours = 0
                    total_absences = 0
                    for entry in entries_info["entries"]:
                        total_hours += entry['total_hours']
                        total_absences += entry['total_absences']
                    print(f" Total # of Hours Worked: {total_hours}")
                    print(f" Total # of Absences: {total_absences}")
            else:
                print("\nThere is no timekeeping data for this employee.")
        else:
            print("\nInvalid Employee ID. Please register the employee first.")

        another_transaction = input("\nDo you want to view another employee? (Y/N): ")
        print()
        if another_transaction.lower() != "y":
            break

# DESIGNS
Bar01 = ("====================== CC03 DAILY-TIME RECORD SYSTEM ======================")
Bar02 = ("===========================================================================")
Bar03 = ("                                 GOODBYE!                                  \n")
Bar04 = ("============================ TIMEKEEPING SCREEN ===========================")
Bar05 = ("============================ REGISTER EMPLOYEE ============================")
Bar06 = ("============================== VIEW EMPLOYEE ==============================")

# DATE AND TIME
current_datetime = datetime.now()
current_date = current_datetime.strftime("%Y/%m/%d")
current_time = current_datetime.strftime("%I:%M:%S %p")
DateTimeIndicator = (f"                                                     {current_date} {current_time}")

main_menu()