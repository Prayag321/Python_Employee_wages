"""
  @Author: Prayag Bhoir
  @Date: 31-07-2024 
  @Last Modified by: Prayag Bhoir
  @Last Modified time: 31-07-2024 
  @Title : Employee Wage uc8
"""
import random
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4

class EmployeeWage:
  # MAX_HOUR = 100
  # MAX_DAYS = 20
  # WAGE_PER_HOUR = 20
  def __init__(self,wage,days,hours):
    self.WAGE_PER_HOUR=wage
    self.MAX_DAYS=days
    self.MAX_HOUR=hours

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

  def cal_daily_wage(self,FULL_TIME_HOUR,PART_TIME_HOUR):
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
        daily_wage = FULL_TIME_HOUR * self.WAGE_PER_HOUR
      case "Part-time":
        daily_wage = PART_TIME_HOUR * self.WAGE_PER_HOUR
      case _:
        daily_wage = 0
    return daily_wage

  def calculate_monthly_wage(self,FULL_TIME_HOUR,PART_TIME_HOUR):
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
      daily_wage = self.cal_daily_wage(FULL_TIME_HOUR,PART_TIME_HOUR)
      monthly_wage += daily_wage

      if daily_wage > 0:
        if daily_wage == FULL_TIME_HOUR * self.WAGE_PER_HOUR:
          hours += FULL_TIME_HOUR
        elif daily_wage == PART_TIME_HOUR * self.WAGE_PER_HOUR:
          hours += PART_TIME_HOUR
        days += 1

    # if hours == 104:  # rare case
    #   hours -= 4
    #   monthly_wage -= 4 * self.WAGE_PER_HOUR  # or 2000 it's the same

    return monthly_wage, days, hours

def main():
  apexon = EmployeeWage(100,20,100)
  monthly_wage, days, hours = apexon.calculate_monthly_wage(FULL_TIME_HOUR,PART_TIME_HOUR)
  print(f"Company name: Apexon")
  print(f"Days present: {days}\nHours: {hours}\nMonthly wage: {monthly_wage}")

  infostrech = EmployeeWage(1000,20,100)
  monthly_wage, days, hours = infostrech.calculate_monthly_wage(FULL_TIME_HOUR,PART_TIME_HOUR)
  print(f"\nCompany name: Infostrech")
  print(f"Days present: {days}\nHours: {hours}\nMonthly wage: {monthly_wage}")

if __name__ == "__main__":
  main()
