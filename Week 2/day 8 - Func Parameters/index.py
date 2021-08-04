def greet_with_name(name = 'User'):
  print(f"Hello {name}!")

greet_with_name('Eddie')
greet_with_name()

def greet_with(name, location):
  print(f"Hello {name}!")
  print(f"What is it like in {location}?")

greet_with('Eddie', 'New York') # same as :
greet_with(location='New York', name='Eddie')
