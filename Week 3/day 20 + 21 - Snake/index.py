class Animal:
  def __init__(self):
    self.num_of_eyes = 2
  
  def breathe(self):
    print('breathing')

class Fish(Animal):
  def __init__(self):
    super().__init__()

  def swim(self):
    print('swimming')

nemo = Fish()
nemo.breathe()
nemo.swim()