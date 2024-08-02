"""
  @Author: Prayag Bhoir
  @Date: 2-07-2024 
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 2-07-2024 
  @Title : Employee Wage uc8
"""
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
    self.employees = {}  # dict to store employee details

  def add_employee(self, employee_name):
    """
    Description:
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
    Description:
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
    Description:
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
    Description:
      This function calculates the daily wage

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
    Description:
      This function calculates the monthly wage

    Parameters:
      None

    Returns:
      monthly_wage(int): Calculated monthly wage by formula
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
    Description:
      Displays the total wage details for the company, including the total days worked, total hours worked, and the total monthly wage.

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
    Description:
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
    return company

  def calculate_wages_for_all_companies(self):
    """
    Description:
      Calculates the monthly wage for all companies in the list.
      Calls the calculate_monthly_wage method for each CompanyEmpWage instance in the list.

    Parameters:
      None

    Returns:
      None
    """
    for company in self.company_list:
      company.calculate_monthly_wage()

  def display_all_wage_details(self):
    """
    Description:
      Displays the wage details for all companies in the list.
      Calls the display_wage_details method for each CompanyEmpWage instance in the list.

    Parameters:
      None

    Returns:
      None
    """
    for company in self.company_list:
      company.display_wage_details()

def main():
  emp_wage_builder = EmpWageBuilder()

  # adding companies to EmpWageBuilder
  apexon = emp_wage_builder.add_company("Apexon", 100, 20, 100)
  infostrech = emp_wage_builder.add_company("Infostrech", 1000, 20, 100)

  # adding employees
  apexon.add_employee("Alice")
  apexon.add_employee("Bob")
  infostrech.add_employee("Charlie")
  infostrech.add_employee("Diana")

  # removing an employee
  apexon.remove_employee("Bob")

  # calculate wages for all companies
  emp_wage_builder.calculate_wages_for_all_companies()

  # display wage details for all companies
  emp_wage_builder.display_all_wage_details()

if __name__ == "__main__":
  main()
