from tkinter import*
window = Tk()
window.title  = ("Plz work")
a=0
int(a)
def bye():
    global a
    a=a+1
def finish():
    print(a)
my_label = Label(window, text="Button clicker")
my_label.grid(row=0, column=0)

my_button = Button(window, text="Add1",command=bye)
my_button.grid(row=1, column=0)

my_button = Button(window, text="Show how many clicks", command=finish)
my_button.grid(row=1, column=1)

window.mainloop()
