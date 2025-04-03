import tkinter as tk
from tkinter import ttk
from ui.login_personal import Login
from ui.admin_panel import AdminPanel
from utils import Util
from style import Style

class Personal:
    def __init__(self,root):
        self.root=root
        # style=ttk.Style()
        # style.configure("personal.TFrame",background='Black')
        Style.styles()
        self.create_personal_panel()

    def create_personal_panel(self):
        personal_frame=ttk.Frame(self.root,width=400,height=600,style='personal.TFrame')
        personal_frame.pack_propagate(False)
        personal_frame.pack(padx=50,pady=30,ipadx=20,ipady=20)
        
        ttk.Label(personal_frame,text='PERSONAL',font=('Verdana',25)).pack(pady=50)
        ttk.Button(personal_frame,text='Personal Aministrativo',style='btn.TButton',width=30,command=lambda:self.open_login_window(True)).pack(padx=25,pady=(30,10),ipady=6)
        ttk.Button(personal_frame,text='Personal Cajero',style='btn.TButton',width=30,command=lambda:self.open_login_window(False)).pack(padx=25,pady=(30,10),ipady=6)

    def open_login_window(self,is_admin):
        try:
            self.root.withdraw()
            Login(self.root,is_admin)
            # AdminPanel(self.root)
        except Exception as e:
            Util.view_message(e,'red',self.root)
        
