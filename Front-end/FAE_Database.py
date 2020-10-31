from tkinter import *

#Create home_page
def home_page(root, title):
    root.title(title)                                           # title = 'F.A.E. Database'
    root.geometry('750x500+300+100')                            # Open window in center of screen
    root.minsize(500, 350)
    


def table(root, data):           
        #Creates a table using Data ---> Puts on current Page
        total_rows = len(data)          # number of rows
        total_columns = len(data[0])    # number of columns
        for i in range(total_rows): 
            for j in range(total_columns):   
                e = Entry(root, width=10, fg='black', font=('Arial',16,'bold'), 
                        bd=2, justify="center")             
                e.grid(row=i, column=j, sticky="NSEW")
                root.grid_columnconfigure(j, weight=1)  # set scaling for columns
                root.grid_rowconfigure(i, weight=1)     # set scaling for rows
                e.insert(END, data[i][j]) 


data = [(1,'Raj','Mumbai',19), 
       (2,'Aaryan','Pune',18), 
       (3,'Vaishnavi','Mumbai',20), 
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21),
       (6, 'bob', 'builder', 23)] 

#Execute Code
master = Tk()
home_page(master, 'F.A.E. Database')
table(master, data)
master.mainloop()