import tkinter as tk
from tkinter import ttk
import bcrypt,ast
from dao.manage_dao import ManageDAO

class Util:
    @staticmethod
    def view_window(previous_window,now_window):#abrir la ventana anterior
        now_window.destroy()
        previous_window.deiconify()
        previous_window.state('zoomed')

    @staticmethod
    def view_message(e,color,window):   #ver mensaje de error o confimacion
       style=ttk.Style()
       def update_progress(i):
            if i>=0:
                canvas.coords(progress,0,0,i*3,30)
                window.update_idletasks()
                window.after(30,update_progress,i-1)
            else:
                message_frame.destroy()
       style.configure('cont.TFrame',background='White')
       message_frame=ttk.Frame(window,style='cont.TFrame',width=300,height=100)
       message_frame.pack_propagate(False)
       message_frame.place(relx=0.99,y=10,anchor='ne')
       tk.Label(message_frame,text=e,fg=color,bg='White',wraplength=200,font=('Verdana',10,'bold')).pack(padx=10,pady=15)
       canvas=tk.Canvas(message_frame,width=300,height=10,bg='White',highlightthickness=0)
       canvas.pack(side='bottom',padx=0,pady=(10,0))
       progress=canvas.create_rectangle(0,0,0,30,fill=color,outline=color)
       window.after(30,update_progress,100)
       
       

       
    @staticmethod
    def add_placeholder(field,placeholder,is_password=False,is_normal=True):#agregar los placeholder a los entries
        style=ttk.Style()
        style.configure('onFocusOut.TEntry',foreground='gray')
        style.configure('onFocusIn.TEntry',foreground='Black')
        def onFocusIn(e):
            print('Hola1')
            if field.get()==placeholder:
                field.delete(0, tk.END)
                field.config(foreground='black')
                if is_password:
                    field.config(show='*')

        
        def onFocusOut(e):
            if field.get()=='':
                field.insert(0,placeholder)
                field.config(foreground='gray')
                if is_password:
                    field.config(show='')
            else:
                field.config(foreground='black')
            
        if is_normal:
            field.insert(0, placeholder)
            field.config(foreground='gray')

        if is_password:
            field.config(show='')
        field.bind("<FocusIn>",onFocusIn)
        field.bind("<FocusOut>",onFocusOut)
    
    @staticmethod
    def missing_fields(fields):#los campos deben estar llenos
        missing_field=[]
        for (field,name) in fields:
            if not field.get().strip() or field.get()==name:
                missing_field.append(name)
        if missing_field:
            raise ValueError(f"Los campos '{', '.join(missing_field)}' son obligatorios")
    
    # def clean_fields(fields):#limpiar los entries
    #     # style=ttk.Style()
    #     # style.configure("combo.TCombobox",font=('Verdana',15),foreground='gray')
    #     for (field,is_combobox) in fields:
    #        if is_combobox:
    #            field.set('Rol')
    #        else:
    #             field.delete(0,tk.END)

    @staticmethod
    def clean_fields(fields):#limpiar los entries
        for field,placeholder,is_combobox,is_password in fields:
           if is_combobox:
               field.set(placeholder)
           else:
                field.delete(0,tk.END)
           if not is_combobox:
               Util.add_placeholder(field,placeholder,is_password)

    @staticmethod       
    def encryct_password(password):#encriptar la contraseña
        salt=bcrypt.gensalt()
        password_hash=bcrypt.hashpw(password.encode(),salt)
        return password_hash
    
    @staticmethod
    def verify_password(password,password_hash):#verificar la contraseña
        print('Hola')
        return bcrypt.checkpw(password.encode(),password_hash)
    
    @staticmethod
    def add_register_treeview(tree,tuple_values):
        tree.insert("",tk.END,values=(tuple_values))


    @staticmethod
    def charge_registers_treeview(tree,registers):
        tree.delete(*tree.get_children())
        for register in registers:
            tree.insert("",tk.END,values=register)

    @staticmethod
    def filter_register_treeview(tree,combobox,field,columns_mapping,table,window):
        try:
            selection=combobox.get()
            print(selection)
            if selection=="Buscar por":
                raise ValueError('Debe seleccionar una opción')
            column=columns_mapping.get(selection)
            value=field.get()

            if not value.strip():
                raise ValueError('Debe ingresar el nombre o codigo')
            result=ManageDAO.get_values_with_condition(table,columns_mapping.values(),column,value)
            Util.charge_registers_treeview(tree,result)
            Util.view_message('Para cargar todos los registros limpie el campo','orange',window)
        except Exception as e:
            Util.view_message(e,'red',window)
            print(e)

    @staticmethod
    def verify_entry(e,tree,field,table,columns):
        if not field.get().strip():
            result=ManageDAO.get_all_values(table,columns)
            Util.charge_registers_treeview(tree,result)

    @staticmethod
    def selection_register_treeview(tree):
        values=()
        selection_id=tree.selection() 
        for id in selection_id:
            values=tree.item(id,'values')
        return values