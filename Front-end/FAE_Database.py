from tkinter import *

#Create home_page
def home_page(root, title):
    root.title(title)                                           # title = 'F.A.E. Database'
    root.geometry('750x500+300+100')                            # Open window in center of screen

def table(root, total_rows, total_columns, data):           
        #Creates a table using Data ---> Puts on current Page
        for i in range(total_rows): 
            for j in range(total_columns):   
                e = Entry(root, width=20, fg='black', 
                               font=('Arial',16,'bold'))                   
                e.grid(row=i, column=j) 
                e.insert(END, data[i][j]) 

data = [(1,'Raj','Mumbai',19), 
       (2,'Aaryan','Pune',18), 
       (3,'Vaishnavi','Mumbai',20), 
       (4,'Rachna','Mumbai',21), 
       (5,'Shubham','Delhi',21)] 

#Execute Code
master = Tk()
home_page(master, 'F.A.E. Database')
table(master, 5, 4, data)
master.mainloop()