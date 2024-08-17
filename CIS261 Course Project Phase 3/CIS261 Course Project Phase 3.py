# Kyle Stewart CIS261 Course Project Phase 3

total_employees = 0
total_hours = 0.00
total_gross_pay = 0.00
total_tax = 0.00
total_net_pay = 0.00

employee_data = []

def get_date(prompt):
    date = input(prompt)
    return date

def get_employee_name():
    employee_name = input("Enter the employee's name (or 'END' to finish): ")
    return employee_name

def get_total_hours():
    total_hours = float(input("Enter the total hours: "))
    return total_hours

def get_hourly_rate():
    hourly_rate = float(input("Enter the hourly rate: "))
    return hourly_rate

def get_income_tax_rate():
    income_tax_rate = float(input("Enter the income tax rate: "))
    return income_tax_rate / 100  # Convert percentage to decimal

def calculate_pay(hours, rate, tax_rate):
    gross_pay = hours * rate
    income_tax = gross_pay * tax_rate
    net_pay = gross_pay - income_tax
    return gross_pay, income_tax, net_pay

def display_employee_info(from_date, to_date, name, hours, rate, gross, tax_rate, tax, net):
    print(f"{from_date} {to_date} {name} {hours:.2f} {rate:.2f} {gross:.2f} {tax_rate:.1%} {tax:.2f} {net:.2f}")

def display_totals(totals):
    print()
    print(f"Total Number of Employees: {totals['employees']}")
    print(f"Total Hours Worked: {totals['hours']:.2f}")
    print(f"Total Gross Pay: {totals['gross']:.2f}")
    print(f"Total Income Tax: {totals['tax']:.2f}")
    print(f"Total Net Pay: {totals['net']:.2f}")

def write_to_file(data):
    with open("employee_data.txt", "a") as file:
        file.write("|".join(map(str, data)) + "\n")

def read_from_file():
    with open("employee_data.txt", "r") as file:
        return file.readlines()

def get_emp_name():
    empname = input("Enter employee name (or 'END' to finish): ")
    return empname

def get_dates_worked():
    fromdate = input("Enter Start Date (mm/dd/yyyy): ")
    todate = input("Enter End Date (mm/dd/yyyy): ")
    return fromdate, todate

def get_hours_worked():
    hours = float(input('Enter amount of hours worked: '))
    return hours

def get_hourly_rate():
    hourlyrate = float(input("Enter hourly rate: "))
    return hourlyrate

def get_tax_rate():
    taxrate = float(input("Enter tax rate: "))
    return taxrate / 100  # Convert percentage to decimal

def calc_tax_and_net_pay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def print_info(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[2]
        hours = EmpList[3]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        grosspay, incometax, netpay = calc_tax_and_net_pay(hours, hourlyrate, taxrate)
        display_employee_info(fromdate, todate, empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay

def print_totals(EmpTotals):
    print()
    print(f"Total Number of Employees: {EmpTotals['TotEmp']}")
    print(f"Total Hours Worked: {EmpTotals['TotHrs']:.2f}")
    print(f"Total Gross Pay: {EmpTotals['TotGrossPay']:.2f}")
    print(f"Total Income Tax: {EmpTotals['TotTax']:.2f}")
    print(f"Total Net Pay: {EmpTotals['TotNetPay']:.2f}")

def write_employee_information(employee):
    with open("employee_data.txt", "a") as file:
        file.write('{}|{}|{}|{}|{}|{}\n'.format(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))

def get_from_date():
    valid = False
    fromdate = ""
    while not valid:
        fromdate = input("Enter From Date (mm/dd/yyyy) or 'ALL': ")
        if (len(fromdate.split('/')) != 3 and fromdate.upper() != 'ALL'):
            print("Invalid Date Format: ")
        else:
            valid = True
    return fromdate

def read_employee_information(fromdate):
    EmpDetailList = []
    with open("employee_data.txt", "r") as file:
        data = file.readlines()
    condition = True
    if fromdate.upper() == 'ALL':
        condition = False
    for employee in data:
        employee = [x.strip() for x in employee.strip().split("|")]
        if not condition:
            EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
        else:
            if fromdate == employee[0]:
                EmpDetailList.append([employee[0], employee[1], employee[2], float(employee[3]), float(employee[4]), float(employee[5])])
    return EmpDetailList

if __name__ == "__main__":
    EmpDetailList = []
    EmpTotals = {}
    while True:
        empname = get_emp_name()
        if (empname.upper() == "END"):
            break
        fromdate, todate = get_dates_worked()
        hours = get_hours_worked()
        hourlyrate = get_hourly_rate()
        taxrate = get_tax_rate()
        print()
        EmpDetail = [fromdate, todate, empname, hours, hourlyrate, taxrate]
        write_employee_information(EmpDetail)
        print()
        print()
    fromdate = get_from_date()  # User is prompted to enter the specific date or "ALL" here
    EmpDetailList = read_employee_information(fromdate)
    print()
    print_info(EmpDetailList)
    print()
    print_totals(EmpTotals)
