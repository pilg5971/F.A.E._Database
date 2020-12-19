import tkinter as tk    
from tkinter import *
from tkinter import ttk 

#Create home_page
def home_page(root, title):
    root.title(title)                                           # title = 'F.A.E. Database'
    #root.iconbitmap('C:\\Users\\Taufiq\\Documents\\Projects\\F.A.E._Database\\Front-end\\league.jpg')
    root.geometry('750x500+300+100')                            # Open window in center of screen
    root.minsize(500, 350)

def createTabs(tabControl, tab1, tab2):
    tabControl.add(tab1, text='Tab 1')
    tabControl.add(tab2, text='Tab 2')
    tabControl.pack(expand = 1, fill="both")

def table(tab1, data):
    total_rows = len(data)          # number of rows
    total_columns = len(data[0])    # number of columns
    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(tab1, width=10, fg='black', font=('Arial',16,'bold'), 
                        bd=2, justify="center")         # bd = border size   
            e.grid(row=i, column=j, sticky="NSEW")
            tab1.grid_columnconfigure(j, weight=1)  # set scaling for columns
            tab1.grid_rowconfigure(i, weight=1)     # set scaling for rows
            e.insert(END, data[i][j])               # insert the data
            e.config(state="readonly")

# dummy data
data = [(1,'Raj','Mumbai',19), 
       (2,'Aaryan','Pune',18), 
       (3,'Vaishnavi','Mumbai',20), 
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21),
       (6, 'bob', 'builder', 23)] 


#Execute Code
master = Tk()
# create tabs
tabControl = ttk.Notebook(master)   
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# function calls
home_page(master, 'F.A.E. Database')
createTabs(tabControl, tab1, tab2)
table(tab1, data)
master.mainloop()