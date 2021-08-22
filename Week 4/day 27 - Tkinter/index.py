import tkinter
from tkinter.constants import END

window = tkinter.Tk()

window.title('First Gui program')
window.minsize(width = 800, height = 600)

# label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.grid( 0,0)

def handle_click():
  my_label['text'] = input.get()

button = tkinter.Button(text="Click Me", command=handle_click)
button.grid(1,1)

new_button = tkinter.Button(text="New One")
new_button.grid(0, 2)

# entry
input = tkinter.Entry(width=20)
input.insert(END, 'Some default text')
input.grid(3, 2)



# keeps window open
window.mainloop()
