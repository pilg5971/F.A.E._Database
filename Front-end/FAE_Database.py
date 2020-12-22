import tkinter as tk    
from tkinter import *
from bs4 import BeautifulSoup
import requests
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

def populateTable(tab1, data):
    total_rows = len(data)          # number of rows
    total_columns = len(data[0])    # number of columns
    print(data)
    print(total_rows)
    print(total_columns)
    total_rows = 20
    total_columns = 10

    for i in range(total_rows):
        for j in range(total_columns):
            e = Entry(tab1, width=4, fg='black', font=('Arial',9,'bold'), 
                        bd=2, justify="center")         # bd = border size   
            e.grid(row=i, column=j, sticky="NSEW")
            tab1.grid_columnconfigure(j, weight=1)  # set scaling for columns
            tab1.grid_rowconfigure(i, weight=1)     # set scaling for rows
            e.insert(END, data[i][j])               # insert the data
            e.config(state="readonly")

def getPickBanData(pickAndBanOrder):
    url1 = requests.get("https://lol.gamepedia.com/Special:RunQuery/PickBanHistory?PBH%5Bpage%5D=Worlds+2020+Main+Event&PBH%5Btextonly%5D=Yes&pfRunQueryFormName=PickBanHistory")
    soup = BeautifulSoup(url1.content, 'html.parser')   # BeautifulSoup is used for web scraping
    #text-version url
    table = soup.find(class_='wikitable')
    table_rows = table.find("tbody").find_all('tr')
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.get_text() for tr in td]
        pickAndBanOrder.append(row)

    # delete empty rows
    pickAndBanOrder = [nested for nested in pickAndBanOrder if nested]
    return pickAndBanOrder

# dummy data
data = [[1,'Raj','Mumbai',19], 
       [2,'Aaryan','Pune',18], 
       [3,'Vaishnavi','Mumbai',20], 
       [4,'Rachna','Mumbai',21],
       [5,'Shubham','Delhi',21],
       [6, 'bob', 'builder', 23]]


#Execute Code
master = Tk()
# create tabs
tabControl = ttk.Notebook(master)   
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
# TODO make the url "year" dynamic
pickAndBanOrder = []

# function calls
pickAndBanOrder = getPickBanData(pickAndBanOrder)
home_page(master, 'F.A.E. Database')
createTabs(tabControl, tab1, tab2)
populateTable(tab1, pickAndBanOrder)
master.mainloop()