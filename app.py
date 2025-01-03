import tkinter as tk
from tkinter import messagebox
from Habit_trac import User,Habit
def show_page(frame):
    frame.tkraise()
def habit_form():
    def create_habit():
        global user
        name=name_box.get()
        frequency=freq_box.get()
        desc=description_box.get("1.0", "end-1c")
        habit=Habit(name,frequency,desc)
        user.add_habit(habit)
        refresh()
        refresh_checklist()
        form.destroy()
    form=tk.Toplevel(root)
    form.title("Adding Habit form")
    for i in range(6):
        form.grid_rowconfigure(i,weight=1)
    for i in range(3):
        form.grid_columnconfigure(i,weight=1) 
    title=tk.Label(form,text="Habit Entry Form")
    name=tk.Label(form,text="Habit Name")
    name_box=tk.Entry(form,width=30)
    freq=tk.Label(form,text="Frequency")
    freq_box=tk.Entry(form,width=30)
    description=tk.Label(form,text="Notes")
    description_box=tk.Text(form,width=30,height=5)
    submit=tk.Button(form,text="Submit!",command=create_habit)
    name.grid(row=1,column=0,padx=5,pady=5)
    name_box.grid(row=1,column=1,padx=5,pady=5)
    freq.grid(row=2,column=0,padx=5,pady=5)
    freq_box.grid(row=2,column=1)
    description.grid(row=3,column=0,padx=5,pady=5)
    description_box.grid(row=3,column=1,padx=5,pady=5)
    title.grid(row=0,column=1,padx=5,pady=5)
    submit.grid(row=4,column=1,padx=5,pady=5)    
root=tk.Tk()
root.title("Habit app")
container=tk.Frame(root)
container.grid(row=0,column=0,sticky="nsew")
container.grid_rowconfigure(0,weight=1,minsize=5)
container.grid_columnconfigure(0,weight=1,minsize=5)

#login real
login1=tk.Frame(container)
login1.grid(row=0,column=0,sticky="nsew")
for i in range(3):
    login1.grid_rowconfigure(i,weight=1,minsize=5)
    login1.grid_columnconfigure(i,weight=1,minsize=5)
username1=tk.Label(login1,text="Enter username") 
u_entry1=tk.Entry(login1)
password1=tk.Label(login1,text="Enter password")  
p_entry1=tk.Entry(login1)  
user=User("abc",123)
def create_user():
    global user
    user=User(u_entry1.get(),p_entry1.get())
    show_page(welcome)
login_bt1=tk.Button(login1,text="Login",command=create_user)   
username1.grid(row=0,column=0)
u_entry1.grid(row=0,column=1)
password1.grid(row=1,column=0)
p_entry1.grid(row=1,column=1)
login_bt1.grid(row=2,column=1)

#login page
login=tk.Frame(container)
login.grid(row=0,column=0,sticky="nsew")
for i in range(3):
    login.grid_rowconfigure(i,weight=1,minsize=5)
    login.grid_columnconfigure(i,weight=1,minsize=5)
username=tk.Label(login,text="username") 
u_entry=tk.Entry(login)
password=tk.Label(login,text="password")  
p_entry=tk.Entry(login)
def login_event(switch):
    global user
    user.check_authorized(u_entry.get(),p_entry.get())
    if(user.authorized_status):
        show_page(switch)
    else:
        messagebox.showerror("login failed","Invalaid username or password")
        print(user)
login_bt=tk.Button(login,text="Login",command=lambda: login_event(main))   
username.grid(row=0,column=0)
u_entry.grid(row=0,column=1)
password.grid(row=1,column=0)
p_entry.grid(row=1,column=1)
login_bt.grid(row=2,column=1)

#welcome page
welcome=tk.Frame(container)
welcome.grid(row=0,column=0,sticky="nsew")
welcome.grid_columnconfigure(0,weight=1,minsize=5)
for i in range(3):
    welcome.grid_rowconfigure(i,weight=1,minsize=5)
start_wel=tk.Label(welcome,text="Welcome to Habit tracer lets build together")
def show_which():
    if user.authorized_status==True:
        show_page(main)
    else:
        show_page(login)    
st_bt=tk.Button(welcome,text="Start",command=lambda: show_which())
exit_bt=tk.Button(welcome,text="Exit",command=root.destroy)
start_wel.grid(row=0,column=0,padx=5,pady=5)
st_bt.grid(row=1,column=0,padx=5,pady=5)
exit_bt.grid(row=2,column=0,padx=5,pady=5)

#Main page
main=tk.Frame(container)
main.grid(row=0,column=0,sticky="nsew")
for i in range(3):
    main.grid_columnconfigure(i,weight=1,minsize=5)
    main.grid_rowconfigure(i,weight=1,minsize=5)  
habit_frame=tk.Frame(main)   
habit_frame.grid(row=3,column=0,sticky="nsew") 
add_habit=tk.Button(main,text="Add Habit",command=habit_form) 
habit_label=tk.Label(habit_frame,text="No Habits Yet")
habit_label.pack()

def refresh():
    for widgt in habit_frame.winfo_children():
        a=1
        if len(user.habits)!=0:
            a=2
            widgt.destroy()
    for i,habit in  enumerate(user.habits):
        if habit.status==False:
            habit_label=tk.Label(habit_frame,text=f"{habit.name}")
            habit_label.pack()

    #if there are no habits to add then calling mark will not destroy window      
    if all(habit.status for habit in user.habits) and a==2:    
        no_hb_lbl=tk.Label(habit_frame,text="All Done!")
        no_hb_lbl.pack()   
done_mark=tk.Button(main,text="mark_done",command=lambda: show_page(done))  
add_habit.grid(row=0,column=1)
done_mark.grid(row=1,column=1)

#Mark habits done
#refresh the list when new habit is added
def refresh_checklist():
    def checkbox_event(index):
        if checkvar[index].get()==1:
            user.habits[index].status=True
        else:
            user.habits[index].status=False 
        refresh()          
    for widgt in done.winfo_children():
        widgt.destroy() 
    checkvar=[]    
    for i,habit in  enumerate(user.habits):
        var=tk.IntVar(value=1 if habit.status else 0)
        checkvar.append(var)
        check=tk.Checkbutton(done,text=habit.name,variable=var,command=lambda x=i: checkbox_event(x))
        check.grid(row=i,column=0)
    ok=tk.Button(done,text="Done",command=lambda: show_page(main)) 
    ok.grid(row=i+1,column=2)

#no habit screen
done=tk.Frame(container)
done.grid(row=0,column=0,sticky="nsew")
lbl=tk.Label(done,text="No Habits Yet")
lbl.grid(row=0,column=0)

ok=tk.Button(done,text="Done",command=lambda: show_page(main)) 
ok.grid(row=1,column=2)
show_page(login1)
root.mainloop()


