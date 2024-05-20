from cal_fun import do_add,do_div,do_mul,do_sub
from power import do_power

def main():
  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  # Get the operation from the user.
  operation = input("Enter the operation (+, -, *, /, **): ")

  # Perform the operation and print the result.
  if operation == "+":
    result=do_add(num1,num2)
  elif operation == "-":
    result=do_sub(num1,num2)
  elif operation == "*":
    result=do_mul(num1,num2)
  elif operation == "/":
    result=do_div(num1,num2)
  elif operation == "**":
    result=do_power(num1,num2)


  print("Result: ",result)


if __name__ == "__main__":
  main()
