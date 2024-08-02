"""
  @Author: Prayag Bhoir
  @Date: 31-07-2024 
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 2-07-2024 
  @Title : Employee Wage uc9+uc10
"""
import random

class EmployeeWage:
  FULL_TIME_HOUR = 8
  PART_TIME_HOUR = 4

  def __init__(self, company_name, wage_per_hour, max_days, max_hours):
    self.company_name = company_name
    self.wage_per_hour = wage_per_hour
    self.max_days = max_days
    self.max_hours = max_hours
    self.total_wage = 0
    self.total_days = 0
    self.total_hours = 0

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
      None
    """
    hours = 0
    days = 0
    monthly_wage = 0

    while days < self.max_days and hours < self.max_hours:
      status = self.check_employee_status()
      daily_wage = self.cal_daily_wage(status)
      monthly_wage += daily_wage

      if daily_wage > 0:
        if daily_wage == self.FULL_TIME_HOUR * self.wage_per_hour:
          hours += self.FULL_TIME_HOUR
        elif daily_wage == self.PART_TIME_HOUR * self.wage_per_hour:
          hours += self.PART_TIME_HOUR
        days += 1

      if hours > self.max_hours:
        hours = self.max_hours
        break

    self.total_wage = monthly_wage
    self.total_days = days
    self.total_hours = hours

    # return monthly_wage, days, hours

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
    print(f"Days present: {self.total_days}")
    print(f"Hours: {self.total_hours}")
    print(f"Monthly wage: {self.total_wage}")

class EmpWageBuilder:
  def __init__(self):
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
      None
    """
    company = EmployeeWage(company_name, wage_per_hour, max_days, max_hours)
    self.company_list.append(company)

  def calculate_wages_for_all_companies(self):
    """
    Description:
      Calculates the monthly wage for all companies in the list.
      Calls the calculate_monthly_wage method for each EmployeeWage instance in the list.

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
      Calls the display_wage_details method for each EmployeeWage instance in the list.

    Parameters:
      None

    Returns:
      None
    """
    for company in self.company_list:
      company.display_wage_details()

def main():
  emp_wage_builder = EmpWageBuilder()

  emp_wage_builder.add_company("Apexon", 100, 20, 100)
  emp_wage_builder.add_company("Infostrech", 1000, 20, 100)

  emp_wage_builder.calculate_wages_for_all_companies()

  emp_wage_builder.display_all_wage_details()

if __name__ == "__main__":
  main()
