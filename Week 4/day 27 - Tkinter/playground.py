class Car:
  def __init__(self, **kw):
    self.make = kw.get('make')
    self.model = kw.get('model')

my_car = Car(make='nissan')

print(my_car.make, my_car.model)

# unlimited args (similar to ... in js)
def add(*args):
  print(sum(args))

add(1, 2, 3)

def calc(n, **kwargs):
  n += kwargs['add']
  n *= kwargs['multiply']
  print(n)

calc(2, add=3, multiply= 4)