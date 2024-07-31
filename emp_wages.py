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
    str: A string indicating the employee's status, either 'Present' or 'Absent'.
  """

  status = random.randint(0, 1)

  if status == 0:
    return "Absent"
  else:
    return "Present"

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
  daily_wage = 0

  if check_employee_status()=="Present":
    daily_wage = full_day_hour*wage_per_hour

  return daily_wage



def main():
  print("Employee full time wage is :", daily_wage())

if __name__=="__main__":
  main()
