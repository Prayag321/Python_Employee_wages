"""
  @Author: Prayag Bhoir
  @Date: 31-07-2024 
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 31-07-2024 
  @Title : Employee Wage
"""
import random

class EmployeeWage:
  MAX_HOUR = 100
  MAX_DAYS = 20
  FULL_TIME_HOUR = 8
  PART_TIME_HOUR = 4
  WAGE_PER_HOUR = 20


  def check_employee_status(self):
    """
    Description:
      Simulates checking whether an employee is present or absent using a random number generator.
      The function randomly determines the employee's status as either 'Present' or 'Absent'.

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

  def cal_daily_wage(self):
    """
    Description:
      This function calculates the daily wage

    Parameters:
      None

    Returns:
      daily_wage(int): Calculated daily wage by formula
    """
    daily_wage = 0
    status = self.check_employee_status()
    match status:
      case "Full-time":
        daily_wage = self.FULL_TIME_HOUR * self.WAGE_PER_HOUR
      case "Part-time":
        daily_wage = self.PART_TIME_HOUR * self.WAGE_PER_HOUR
      case _:
        daily_wage = 0
    return daily_wage

  def calculate_monthly_wage(self):
    hours = 0
    days = 0
    monthly_wage = 0

    """
    Description:
      This function calculates the monthly wage

    Parameters:
      None

    Returns:
      monthly_wage(int): Calculated monthly wage by formula
    """
    while days < self.MAX_DAYS and hours < self.MAX_HOUR:
      daily_wage = self.cal_daily_wage()
      monthly_wage += daily_wage

      if daily_wage > 0:
        if daily_wage == self.FULL_TIME_HOUR * self.WAGE_PER_HOUR:
          hours += self.FULL_TIME_HOUR
        elif daily_wage == self.PART_TIME_HOUR * self.WAGE_PER_HOUR:
          hours += self.PART_TIME_HOUR
        days += 1

    if hours == 104:  # rare case
      hours -= 4
      monthly_wage -= 4 * self.WAGE_PER_HOUR  # or 2000 it's the same

    return monthly_wage, days, hours

def main():
  employee_wage = EmployeeWage()
  monthly_wage, days, hours = employee_wage.calculate_monthly_wage()
  print(f"Days present: {days}\nHours: {hours}\nMonthly wage: {monthly_wage}")

if __name__ == "__main__":
  main()
