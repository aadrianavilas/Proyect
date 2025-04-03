import tkinter as tk
from ui.personalPanel import Personal
from db import DataBase
from dao.manage_dao import ManageDAO

root=tk.Tk()
root.title('Home')
root.state('zoomed')
root.configure(bg="#0f0f0f")

db = DataBase() 
personal=Personal(root)
root.mainloop()