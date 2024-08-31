# Kyle Stewart CIS261 Course Project Phase 4

class Login:
    def __init__(self, user_id, password, authorization):
        self.user_id = user_id

        self.password = password
        self.authorization = authorization

def open_file(file_name):
    try:
        with open(file_name, 'a+') as file:
            file.seek(0)
            return [line.strip().split('|') for line in file.readlines()]
    except Exception as e:
        print(f"Error opening file: {e}")
        return []

def add_user(file_name, user_data):
    try:
        with open(file_name, 'a') as file:
            while True:
                user_id = input("Enter User ID (or type 'End' to finish): ")
                if user_id.lower() == 'end':
                    break
                if any(user[0] == user_id for user in user_data):
                    print("User ID already exists. Please enter a different User ID.")
                    continue
                password = input("Enter Password: ")
                auth_code = input("Enter Authorization Code (Admin/User): ")
                if auth_code not in ['Admin', 'User']:
                    print("Invalid Authorization Code. Please enter 'Admin' or 'User'.")
                    continue
                file.write(f"{user_id}|{password}|{auth_code}\n")
                user_data.append([user_id, password, auth_code])
    except Exception as e:
        print(f"Error writing to file: {e}")

def display_users(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                user_id, password, auth_code = line.strip().split('|')
                print(f"User ID: {user_id}, Password: {password}, Authorization Code: {auth_code}")
    except Exception as e:
        print(f"Error reading file: {e}")

def login(file_name):
    user_data = open_file(file_name)
    user_id = input("Enter User ID: ")
    password = input("Enter Password: ")
    user = next((user for user in user_data if user[0] == user_id), None)
    if not user:
        print("User ID does not exist.")
        return None
    if user[1] != password:
        print("Incorrect password.")
        return None
    return Login(user[0], user[1], user[2])

def get_input(prompt, cast_func=str):
    return cast_func(input(prompt))

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    return gross_pay, income_tax, gross_pay - income_tax

def display_employee_info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net):
    print(f"{from_date} {to_date} {name} {hours:.2f} {rate:.2f} {gross:.2f} {tax_rate:.1%} {tax:.2f} {net:.2f}")

def display_totals(totals):
    print(f"\nTotal Number of Employees: {totals['employees']}")
    print(f"Total Hours Worked: {totals['hours']:.2f}")
    print(f"Total Gross Pay: {totals['gross']:.2f}")
    print(f"Total Income Tax: {totals['tax']:.2f}")
    print(f"Total Net Pay: {totals['net']:.2f}")

def write_employee_information(employee):
    with open("employee_data.txt", "a") as file:
        file.write('|'.join(map(str, employee)) + "\n")

def read_employee_information(fromdate):
    EmpDetailList = []
    with open("employee_data.txt", "a+") as file:
        file.seek(0)
        data = file.readlines()
    condition = fromdate.upper() != 'ALL'
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition or fromdate == employee[0]:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList

def main():
    file_name = 'users.txt'
    print("Create users here:")
    user_data = open_file(file_name)
    add_user(file_name, user_data)
    display_users(file_name)
    print("\nPlease log in:")
    login_user = login(file_name)
    if login_user:
        if login_user.authorization == 'Admin':
            print("Admin access granted.")
            EmpDetailList = []
            EmpTotals = {'employees': 0, 'hours': 0.0, 'gross': 0.0, 'tax': 0.0, 'net': 0.0}
            while True:
                empname = get_input("Enter employee name (or 'END' to finish): ")
                if empname.upper() == "END":
                    break
                fromdate, todate = get_input("Enter Start Date (mm/dd/yyyy): "), get_input("Enter End Date (mm/dd/yyyy): ")
                hours, hourlyrate, taxrate = get_input('Enter amount of hours worked: ', float), get_input("Enter hourly rate: ", float), get_input("Enter tax rate: ", float) / 100
                grosspay, incometax, netpay = calculate_pay(hours, hourlyrate, taxrate)
                EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
                write_employee_information(EmpDetail)
                display_employee_info(fromdate, todate, empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
                EmpTotals['employees'] += 1
                EmpTotals['hours'] += hours
                EmpTotals['gross'] += grosspay
                EmpTotals['tax'] += incometax
                EmpTotals['net'] += netpay
            fromdate = get_input("Enter From Date (mm/dd/yyyy) or 'ALL': ")
            EmpDetailList = read_employee_information(fromdate)
            display_totals(EmpTotals)
        else:
            print("User access granted.")
            # Users can only view employee data
            EmpDetailList = read_employee_information('ALL')
            for EmpList in EmpDetailList:
                fromdate, todate, empname, hours, hourlyrate, taxrate = EmpList
                grosspay, incometax, netpay = calculate_pay(hours, hourlyrate, taxrate)
                display_employee_info(fromdate, todate, empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)

if __name__ == "__main__":
    main()
