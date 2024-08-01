"""
    @Author: Prayag Bhoir
    @Date: 31-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 31-07-2024 
    @Title : Employee Wage
"""
import random

def check_employee_status():
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
    # print("Employee is Absent")
    return "Absent"
  elif status == 1:
    # print("Employee is full time")
    return "Full-time"
  elif status == 2:
    # print("Employee is part time")
    return "Part-time"

    print("Employee is full time")
def daily_wage():
  """
  Description:
    This function calculat daily wage

  Parameters:
    None

  Returns:
    daily_wage(int):calculated daily wage by formula
  """

  wage_per_hour = 20
  full_day_hour = 8
  part_day_hour = 4
  daily_wage = 0

  status = check_employee_status()
  match status:
    case "Full-time":
      daily_wage = full_day_hour * wage_per_hour
    case "Part-time":
      daily_wage = part_day_hour * wage_per_hour
    case _:
      daily_wage = 0
  return daily_wage

def calculate_monthly_wage():
  """
  Description:
    This function calculat monthly wage

  Parameters:
    None

  Returns:
    monthly_wage(int):calculated daily wage by formula
  """
  month_days = 20 #20 days
  monthly_wage = 0
  for _ in range(month_days):
    monthly_wage+=daily_wage()
  return monthly_wage

def main():
  print("Employee monthly wage is : ",calculate_monthly_wage())

if __name__=="__main__":
  main()
