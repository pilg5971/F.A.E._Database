import tkinter as tk    
from tkinter import *
#from bs4 import BeautifulSoup
#import requests
from tkinter import ttk 

#Create home_page
def home_page(root, title):
    root.title(title)                                           # title = 'F.A.E. Database'
    #root.iconbitmap('C:\\Users\\Taufiq\\Documents\\Projects\\F.A.E._Database\\Front-end\\league.jpg')
    root.geometry('750x500+300+100')                            # Open window in center of screen
    root.minsize(500, 350)

def createTabs(tabControl, tab1, tab2):
    tabControl.add(tab1, text='Picks & Bans')
    tabControl.add(tab2, text='Champion Stats')
    tabControl.pack(expand = 1, fill="both")

def populateTable(tab1, data):
    total_rows = len(data)          # number of rows
    total_columns = len(data[0])    # number of columns
    print(data)
    print(total_rows)
    print(total_columns)
    #total_rows = 20
    #total_columns = 10
    print("Number of widgets: ", total_rows * total_columns)
    area=('Phase', 'Blue', 'Red', 'Score', 'Patch', 'BB1', 'RB1', 'BB2', 'RB3', 'BP1', 'RP1-2', 'BP2-3', 'RP3', 'RB4', 'BB4', 'RB5', 'BB5', 'RP4', 'BP4-5', 'RP5')
    ac=('all','n','o','s','ne','nw','sw','m', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l')
    tv=ttk.Treeview(tab1,columns=ac,show='headings', height=50)
    for i in range(len(area)):
        #print(area[i])
        if area[i] == 'Score':
            tv.column(ac[i],width=50,anchor='e')
            
        elif area[i] == 'Patch':
            tv.column(ac[i],width=50,anchor='e')
        else:
            tv.column(ac[i],width=95,anchor='e')
        tv.heading(ac[i],text=area[i])
    tv.pack()

    for i in range(76):
        tv.insert('','end',values=data[i])

    # for i in range(total_rows):
    #     for j in range(total_columns):
    #         e = Entry(tab1, width=10, fg='black', font=('Arial',9,'bold'), 
    #                     bd=2, justify="center")         # bd = border size   
    #         e.grid(row=i, column=j, sticky="NSEW")
    #         #tab1.grid_columnconfigure(j, weight=1)  # set scaling for columns
    #         #tab1.grid_rowconfigure(i, weight=1)     # set scaling for rows
    #         e.insert(END, data[i][j])               # insert the data
    #         e.config(state="readonly")

#Execute Code
master = Tk()
# create tabs
tabControl = ttk.Notebook(master)   
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
# TODO make the url "year" dynamic

# function calls
home_page(master, 'F.A.E. Database')
createTabs(tabControl, tab1, tab2)
master.mainloop()