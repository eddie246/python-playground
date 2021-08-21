import tkinter

window = tkinter.Tk()

window.title('First Gui program')
window.minsize(width = 800, height = 600)

# label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.pack(side = 'left')

# unlimited args (similar to ... in js)
def add(*args):
  print(sum(args))

add(1, 2, 3)


# keeps window open
window.mainloop()
# 