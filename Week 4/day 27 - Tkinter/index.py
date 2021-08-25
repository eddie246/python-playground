import tkinter
from tkinter.constants import END

window = tkinter.Tk()

window.title('First Gui program')
window.minsize(width = 800, height = 600)
window.config(padx=100, pady=100)

# label
my_label = tkinter.Label(text='I am a label', font=('Arial', 24, 'bold'))
my_label.grid(column=0, row=0)

def handle_click():
  my_label['text'] = input.get()

button = tkinter.Button(text="Click Me", command=handle_click)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="New One")
new_button.grid(column=0, row=2)

# entry
input = tkinter.Entry(width=20)
input.insert(END, 'Some default text')
input.grid(column=3, row=2)



# keeps window open
window.mainloop()
# wdaw