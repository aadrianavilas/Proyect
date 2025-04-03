import tkinter as tk
from tkinter import ttk,Toplevel
from utils import Util
from ui.registerPanel import Register
from ui.cashier_panel import CashierPanel
from ui.admin_panel import AdminPanel
from dao.manage_dao import ManageDAO
from models.activity_log import ActivityLog
from datetime import datetime
from style import Style
import socket


import ast
class Login:
    def __init__(self,root,is_admin=False):
        self.root=root
        self.is_admin=is_admin
        self.login_window=Toplevel(self.root)
        self.login_window.title('Iniciar Sesión')
        self.login_window.state('zoomed')
        self.login_window.configure(bg="#0f0f0f")
        Style.styles()
        self.login_window.protocol("WM_DELETE_WINDOW",lambda: Util.view_window(self.root, self.login_window))
        # style=ttk.Style()
        # style.configure("login.TFrame",background='Black')
        self.create_login_personal()
    
    def create_login_personal(self):
        login_frame=ttk.Frame(self.login_window,width=400,height=600,style='login.TFrame')
        login_frame.pack_propagate(False)
        login_frame.pack(padx=50,pady=30,ipadx=20,ipady=20)

        ttk.Label(login_frame,text='INICIAR SESION',font=('Verdana',20)).pack(padx=50,pady=(25,0))
        self.user=ttk.Entry(login_frame,style='entry.TEntry',width=30)
        self.user.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        Util.add_placeholder(self.user,'Usuario')

        self.password=ttk.Entry(login_frame,style='entry.TEntry',width=30,show='')
        self.password.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        Util.add_placeholder(self.password,'Password',True)

        if self.is_admin:
            registerLabel=ttk.Label(login_frame,text='¿No estás registrado?',style='register.TLabel')
            registerLabel.pack(padx=25,pady=(20,0))
            registerLabel.bind("<Button-1>",lambda e: self.open_register_personal(e))

        btn_login_frame=ttk.Frame(login_frame,width=300,style="custom.TFrame")
        btn_login_frame.pack_propagate(False)
        btn_login_frame.pack(padx=50,pady=10,ipadx=10,ipady=20)

        ttk.Button(btn_login_frame,text='Ingresar',style='btn.TButton',width=10,command=self.open_work_panel).grid(row=0,column=0,padx=25,pady=10,ipady=6)
        ttk.Button(btn_login_frame,text='Cancelar',style='btn.TButton',width=10,command=lambda: Util.view_window(self.root,self.login_window)).grid(row=0,column=1,padx=25,pady=10,ipady=6)
    
    def open_register_personal(self,e):
        self.login_window.withdraw()
        Register(self.login_window)

    def open_work_panel(self):

        function_name_rol=None
        try:
            if self.is_admin:
                function_name_rol='AdminPanel(self.root)'
                rol='Administrador'
            else:
                function_name_rol='CashierPanel(self.root)'
                rol='Cajero'

            password_hash=ManageDAO.select_register_user(self.user.get(),rol)

            if not Util.verify_password(self.password.get(),password_hash):
                raise ValueError('Contraseña incorrecta')
            self.login_window.withdraw()
            print('Hola12')
            self.save_activity_log()
            print('opas')
            eval(function_name_rol)
            
        except Exception as e:
            Util.view_message(e,'red',self.login_window)
            print(e)
        
    def save_activity_log(self):
            id_user= ManageDAO.get_values_with_condition('users',['id'],'username',self.user.get())
            id_user=id_user[0][0]
            print(id_user,type(id_user))
            ip=self.get_ip()
            log_date= datetime.now().strftime("%d-%m-%Y")
            log_time=datetime.now().strftime("%H:%M:%S")
            act_log=ActivityLog(id_user,ip,log_date,log_time)
            ManageDAO.insert_register('activity_log',['id_user','ip','log_date','log_time'],(act_log.id_user,act_log.ip,act_log.date,act_log.time))
    
    def get_ip(self):
        hostname= socket.gethostname()
        ip= socket.gethostbyname(hostname)
        return ip
