"""
    @Author: Prayag Bhoir
    @Date: 31-07-2024 
    @Last Modified by: Prayag Bhoir
    @Last Modified time: 31-07-2024 
    @Title : Employee Wage
"""
import random

MAX_HOUR = 100
MAX_DAYS = 20
FULL_TIME_HOUR = 8
PART_TIME_HOUR = 4
WAGE_PER_HOUR = 20



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
def cal_daily_wage():
  """
  Description:
    This function calculat daily wage

  Parameters:
    None

  Returns:
    daily_wage(int):calculated daily wage by formula
  """


  daily_wage = 0

  status = check_employee_status()
  match status:
    case "Full-time":
      daily_wage = FULL_TIME_HOUR * WAGE_PER_HOUR
    case "Part-time":
      daily_wage = PART_TIME_HOUR * WAGE_PER_HOUR
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
  hours = 0
  days = 0 
  monthly_wage = 0
  while days<MAX_DAYS and hours<MAX_HOUR:
    daily_wage = cal_daily_wage()
    monthly_wage+=daily_wage

    if daily_wage>0:
      if(daily_wage == FULL_TIME_HOUR * WAGE_PER_HOUR):
        hours+=FULL_TIME_HOUR
      elif(daily_wage == PART_TIME_HOUR * WAGE_PER_HOUR):
        hours+=PART_TIME_HOUR
      days+=1

  if hours==104:#rare case
    hours-=4
    monthly_wage-=4*WAGE_PER_HOUR #or 2000 its same

  return monthly_wage,days,hours

def main():
  monthly_wage,days,hours = calculate_monthly_wage()
  print(f"Days present : {days}\nHours :{hours}\nMonthly wage :{monthly_wage}")

if __name__=="__main__":
  main()
