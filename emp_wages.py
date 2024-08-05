import random

class CompanyEmpWage:
  FULL_TIME_HOUR = 8
  PART_TIME_HOUR = 4

  def __init__(self, company_name, wage_per_hour, max_days, max_hours):
    """
    Initialize the CompanyEmpWage object with company-specific details.

    Parameters:
      company_name (str): The name of the company.
      wage_per_hour (int): The wage rate per hour.
      max_days (int): The maximum number of days to work in a month.
      max_hours (int): The maximum number of hours to work in a month.
    """
    self.company_name = company_name
    self.wage_per_hour = wage_per_hour
    self.max_days = max_days
    self.max_hours = max_hours
    self.employees = {}  # Dictionary to store employee details

  def add_employee(self, employee_name):
    """
    Adds an employee to the company.

    Parameters:
      employee_name (str): The name of the employee to be added.

    Returns:
      None
    """
    if employee_name not in self.employees:
      self.employees[employee_name] = {
        'days_present': 0,
        'hours_present': 0,
        'total_wage': 0
      }
    else:
      print(f"Employee '{employee_name}' already exists.")

  def remove_employee(self, employee_name):
    """
    Removes an employee from the company.

    Parameters:
      employee_name (str): The name of the employee to be removed.

    Returns:
      None
    """
    if employee_name in self.employees:
      del self.employees[employee_name]
    else:
      print(f"Employee '{employee_name}' does not exist.")

  def check_employee_status(self):
    """
    Simulates checking whether an employee is present or absent using a random number generator.
    The function randomly determines the employee's status as either 'Absent', 'Full-time', or 'Part-time'.

    Parameters:
      None

    Returns:
      str: A string indicating the employee's status
    """
    status = random.choice([0, 1, 2])

    if status == 0:
      return "Absent"
    elif status == 1:
      return "Full-time"
    elif status == 2:
      return "Part-time"

  def cal_daily_wage(self, status):
    """
    This function calculates the daily wage.

    Parameters:
      status (str): The status of the employee (e.g., 'Full-time', 'Part-time', 'Absent').

    Returns:
      int: The calculated daily wage based on the employee's status.
    """
    daily_wage = 0
    match status:
      case "Full-time":
        daily_wage = self.FULL_TIME_HOUR * self.wage_per_hour
      case "Part-time":
        daily_wage = self.PART_TIME_HOUR * self.wage_per_hour
      case _:
        daily_wage = 0
    return daily_wage

  def calculate_monthly_wage(self):
    """
    Calculates the monthly wage for all employees in the company.

    Parameters:
      None

    Returns:
      int: The total wage for all employees in the company.
    """
    total_wage = 0
    for employee in self.employees:
      hours = 0
      days = 0

      while days < self.max_days and hours < self.max_hours:
        status = self.check_employee_status()
        daily_wage = self.cal_daily_wage(status)
        total_wage += daily_wage

        if daily_wage > 0:
          if daily_wage == self.FULL_TIME_HOUR * self.wage_per_hour:
            hours += self.FULL_TIME_HOUR
          elif daily_wage == self.PART_TIME_HOUR * self.wage_per_hour:
            hours += self.PART_TIME_HOUR
          days += 1

        if hours > self.max_hours:
          hours = self.max_hours
          break

      # Update employee details
      self.employees[employee]['days_present'] = days
      self.employees[employee]['hours_present'] = hours
      self.employees[employee]['total_wage'] = total_wage

    return total_wage

  def display_wage_details(self):
    """
    Displays the wage details for the company, including the total days worked, total hours worked, and the total monthly wage.

    Parameters:
      None

    Returns:
      None
    """
    print(f"Company name: {self.company_name}")
    total_wage = self.calculate_monthly_wage()
    print(f"Total monthly wage for all employees: {total_wage}")

    for employee, details in self.employees.items():
      print(f"Employee: {employee}")
      print(f"  Days present: {details['days_present']}")
      print(f"  Hours present: {details['hours_present']}")
      print(f"  Monthly wage: {details['total_wage']}")
      print()


class EmpWageBuilder:
  def __init__(self):
    """
    Initialize the EmpWageBuilder with an empty list of CompanyEmpWage instances.
    """
    self.company_list = []

  def add_company(self, company_name, wage_per_hour, max_days, max_hours):
    """
    Adds a new company's wage details to the builder.

    Parameters:
      company_name (str): The name of the company.
      wage_per_hour (int): The wage rate per hour.
      max_days (int): The maximum number of days to work in a month.
      max_hours (int): The maximum number of hours to work in a month.

    Returns:
      CompanyEmpWage: The created CompanyEmpWage object.
    """
    company = CompanyEmpWage(company_name, wage_per_hour, max_days, max_hours)
    self.company_list.append(company)
    print(f"Company '{company_name}' added.")
    return company

  def remove_company(self, company_name):
    """
    Removes a company from the builder.

    Parameters:
      company_name (str): The name of the company to be removed.

    Returns:
      None
    """
    company_exists = any(company.company_name == company_name for company in self.company_list)
    if company_exists:
      self.company_list = [company for company in self.company_list if company.company_name != company_name]
      print(f"Company '{company_name}' removed.")
    else:
      print(f"Company '{company_name}' does not exist.")
  def get_company(self, company_name):
    """
    Retrieves a company by name.

    Parameters:
      company_name (str): The name of the company.

    Returns:
      CompanyEmpWage: The CompanyEmpWage object if found, otherwise None.
    """
    for company in self.company_list:
      if company.company_name == company_name:
        return company
    print(f"Company '{company_name}' does not exist.")
    return None

  def display_all_wage_details(self):
    """
    Displays the wage details for all companies in the list.

    Parameters:
      None

    Returns:
      None
    """
    
    for company in self.company_list:
      company.display_wage_details()


def main():
  emp_wage_builder = EmpWageBuilder()

  while True:
    print("\n1. Add Company")
    print("2. Remove Company")
    print("3. Add Employee")
    print("4. Remove Employee")
    print("5. Display All Wages")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
      case "1":
        company_name = input("Enter company name: ")
        try:
          wage_per_hour = int(input("Enter wage per hour: "))
          max_days = int(input("Enter maximum number of days: "))
          max_hours = int(input("Enter maximum number of hours: "))
          emp_wage_builder.add_company(company_name, wage_per_hour, max_days, max_hours)
        except:
          print("Invalid Input")
        # print(f"Company '{company_name}' added.")
        
      case "2":
        if len(emp_wage_builder.company_list) == 0:
          print("Number of company is zero. Add new company first.")
        else:
          print("Registered companies: ",[company.company_name for company in emp_wage_builder.company_list]) 
          company_name = input("Enter company name to remove: ")
          emp_wage_builder.remove_company(company_name)
        # print(f"Company '{company_name}' removed.")
        
      case "3":
        company_name = input("Enter company name to add employee to: ")
        company = emp_wage_builder.get_company(company_name)
        try:
          num_employees = int(input("Enter number of employees to add: "))
          if num_employees < 0:
              print("Number of employees must be a non-negative integer.")
              continue
          
          for _ in range(num_employees):
              employee_name = input("Enter employee name: ")
              company.add_employee(employee_name)
              print(f"Employee '{employee_name}' added to company '{company_name}'.")
        except ValueError:
            print("Invalid number of employees. Please enter a valid integer.")
        
      case "4":
        company_name = input("Enter company name to remove employee from: ")
        company = emp_wage_builder.get_company(company_name)
        if company:
          employee_name = input("Enter employee name to remove: ")
          company.remove_employee(employee_name)
          print(f"Employee '{employee_name}' removed from company '{company_name}'.")
        
      case "5":
        emp_wage_builder.display_all_wage_details()
        
      case "6":
        print("Exiting...")
        break
        
      case _:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
  main()
