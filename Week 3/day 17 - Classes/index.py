class User:
  def __init__(self, id, username):
    self.id = id
    self.username = username
    self.followers = 0
    self.following = 0

  def follow(self, user):
    user.followers += 1
    self.following += 1


user_1 = User(111, 'eddie')
user_2 = User(112, 'eddie2')

user_1.follow(user_2)

print(user_1.followers)
