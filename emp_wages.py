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

def main():
  print("Employee is", check_employee_status())

if __name__=="__main__":
  main()
