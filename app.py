import tkinter as tk
from Habit_trac import Person
from Habit_trac import Habit
import time
def show_page(frame):
    frame.tkraise()
root=tk.Tk()
root.title("Habbit Tracker")
root.geometry("300x400")
container=tk.Frame(root)
container.pack(fill='both',expand=True)
container.grid_rowconfigure(0,weight=1)
container.grid_columnconfigure(0,weight=1)
#Page no 1
pg1=tk.Frame(container,bg='blue')
pg1.grid(row=0,column=0,sticky='nsew')
button_pg1=tk.Button(pg1,text='add_habbit',fg='white',bg='black',command=lambda: show_page(pg2))
button_pg1.pack(padx=20,pady=60)
#page 2
pg2=tk.Frame(container,bg='black')
pg2.grid(row=0,column=0,sticky='nsew')
button_pg2=tk.Button(pg2,text='del_habbit',fg='white',bg='green',command=lambda: show_page(pg1))
button_pg2.pack(padx=20,pady=60)
show_page(pg1)
root.mainloop()