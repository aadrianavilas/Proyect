import tkinter as tk
from tkinter import ttk,Toplevel
from utils import Util
from models.user import User
from dao.manage_dao import ManageDAO
from style import Style

class Register:
    def __init__(self,root):
        self.root=root
        self.personal_window=Toplevel(root)
        self.personal_window.title('Registrarse')
        self.personal_window.state('zoomed')
        self.personal_window.configure(bg="#0f0f0f")
        self.personal_window.protocol("WM_DELETE_WINDOW",lambda: Util.view_window(self.root, self.personal_window))
        Style.styles()
        self.create_register_panel()
        

    def create_register_panel(self):
        register_frame=ttk.Frame(self.personal_window,width=400,height=600,style='container.TFrame')
        register_frame.pack_propagate(False)
        register_frame.pack(padx=50,pady=30,ipadx=20,ipady=20)

        ttk.Label(register_frame,text='REGISTRARSE',font=('Verdana',20)).pack(padx=50,pady=(25,0))
        self.user=ttk.Entry(register_frame,style='entry.TEntry',width=30)
        self.user.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        Util.add_placeholder(self.user,'Usuario')

        self.password=ttk.Entry(register_frame,style='entry.TEntry',width=30,show='')
        self.password.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        Util.add_placeholder(self.password,'Password',True)

        self.confirm_password=ttk.Entry(register_frame,style='entry.TEntry',width=30,show='')
        self.confirm_password.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        Util.add_placeholder(self.confirm_password,'Confirmar Contraseña',True)

        self.last_names=ttk.Entry(register_frame,style='entry.TEntry',width=30)
        self.last_names.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        Util.add_placeholder(self.last_names,'Apellidos')

        self.names=ttk.Entry(register_frame,style='entry.TEntry',width=30)
        self.names.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        Util.add_placeholder(self.names,'Nombres')

        options=('Administrador','Cajero')
        self.type_personal=ttk.Combobox(register_frame,values=options,width=28,style='combo.TCombobox')
        self.type_personal.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        self.type_personal.set('Rol')
    
        btn_frame=ttk.Frame(register_frame,width=300,style="container.TFrame")
        btn_frame.pack_propagate(False)
        btn_frame.pack(padx=50,pady=10,ipadx=10,ipady=20)

        ttk.Button(btn_frame,text='Registrar',style='btn.TButton',width=10,command=self.configure_register).grid(row=0,column=0,padx=25,pady=10,ipady=6)
        ttk.Button(btn_frame,text='Cancelar',style='btn.TButton',width=10,command=lambda: Util.view_window(self.root,self.personal_window)).grid(row=0,column=1,padx=25,pady=10,ipady=6)
    

    def configure_register(self):
        try:
            fields=[(self.user,'Usuario'),(self.password,'Contraseña'),
                    (self.confirm_password,'Confirmar Contraseña'),(self.last_names,'Apellidos'),
                    (self.names,'Nombres'),(self.type_personal,'Rol')]
            Util.missing_fields(fields)
            user=User(self.user.get(),self.password.get(),self.confirm_password.get(),self.last_names.get()
                      ,self.names.get(),self.type_personal.get())
            result=ManageDAO.register_is_exists('users','username',user.user)
            if result[0]:
                raise ValueError('El usuario ya existe')
            
            ManageDAO.insert_register('users',['username','password','last_names','names','rol'],
                                     (user.user,user.password,user.last_names,user.names,user.rol))
            #ManageDAO.delete_table()
            
            Util.view_message('Se guardó correctamente','green',self.personal_window)

            Util.clean_fields([(self.user,'Usuario',False,False),(self.password,'Contraseña',False,True),
                               (self.confirm_password,'Confirmar Contraseña',False,True),
                               (self.last_names,'Apellidos',False,False),(self.names,'Nombres',False,False),
                               (self.type_personal,'Rol',True,False)])
        except Exception as e:
            Util.view_message(e,'red',self.personal_window)
            print(e)
            

    
        
