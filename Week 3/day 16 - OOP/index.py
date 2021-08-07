# import turtle

# timmy = turtle.Turtle()
# my_screen = turtle.Screen()

# timmy.shape('turtle')
# timmy.color('green')

# for _ in range(20):
#   timmy.forward(100)
#   timmy.right(15)

# my_screen.exitonclick()

import prettytable

table = prettytable.PrettyTable()

table.add_column('Pokemon Name', ['Pickachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

table.align = 'l'

print(table)