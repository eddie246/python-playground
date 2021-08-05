def my_func():
  result = 3 * 2
  return result

print(my_func())


def format_name(f_name, l_name):
  """Take first and last name and format it and returns title version"""
  name = ''
  name += f_name.title()
  name += ' '
  name += l_name.title()

  return name

print(format_name('eddie', 'wang'))

