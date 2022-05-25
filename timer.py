from timeit import default_timer 
from tkinter import *
window = Tk()
def start():
    start=default_timer()
def end():
    end=default_timer
    ()

my_button = Button(window, text="Start", command=start)
my_button.grid(row=1, column=0)

my_button = Button(window, text="End", command=end)
my_button.grid(row=1, column=1)

window.mainloop()

print(end - start)
input()
