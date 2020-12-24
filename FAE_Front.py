import tkinter as tk    
from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk

#----------------------------------------Customization Methods-------------------------------------------# 

# Splash Transition --> Main Window
def main():   
    splash_root.destroy()
    root = Tk()
    root.title('FAE Database')                                           # title = 'F.A.E. Database'
    root.geometry('750x500+300+100')                                     # Open window in center of screen
    root.minsize(500, 350)

    # Create Tabs
    tabControl = ttk.Notebook(root)   
    tab1 = ttk.Frame(tabControl)
    tab2 = ttk.Frame(tabControl) 
    tab3 = ttk.Frame(tabControl) 
    createTabs(tabControl, tab1, tab2, tab3)

# Create Tabs --> Main Window
def createTabs(tabControl, tab1, tab2, tab3):
    tabControl.add(tab1, text='Picks & Bans')
    tabControl.add(tab2, text='Champion Stats')
    tabControl.add(tab3, text='Upload New Information')
    tabControl.pack(expand = 1, fill="both")

#----------------------------------------Execution Phase--------------------------------------------------# 

# Splash Screen Creation  
splash_root = Tk()  
splash_root.title('FAE Database') 
splash_root.geometry('750x500+300+100')
splash_root.minsize(500, 350) 

load = Image.open("SplashImage.JPG")                                       # Splash Image
render = ImageTk.PhotoImage(load)
splash_label = Label(splash_root,image=render) 

splash_label.pack() 

# Splash Screen Timer
splash_root.after(2500, main)

# Start --> Main Window  
mainloop()