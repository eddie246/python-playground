import assets

print(assets.logo)

def add(n1, n2):
  """Take two numbers and adds them together"""
  return n1 + n2

def subtract(n1, n2):
  """Take one number and subtract second number"""
  return n1 - n2

def multiply(n1, n2):
  """Take two numbers and multiply them together"""
  return n1 * n2

def divide(n1, n2):
  """Take two numbers and divide them together"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  continue_calc = True

  num1 = float(input("What's the first number? "))
  num2 = float(input("What's the second number? "))

  while continue_calc:
    for key in operations:
      print(key)

    operation_symbole = input('Pick an operation from the line above: ')

    calc_function = operations[operation_symbole]
    answer = calc_function(num1, num2)

    print(f"{num1} {operation_symbole} {num2} = {answer}")

    if input('Do you want to continue calculating? Y or N: ') == 'N':
      continue_calc = False
      calculator()
    else:
      num1 = answer
      num2 = float(input("What's the new number? "))
      
calculator()