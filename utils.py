import tkinter as tk
from tkinter import ttk
import bcrypt,ast

class Util:
        
    def view_window(previous_window,now_window):#abrir la ventana anterior
        now_window.destroy()
        previous_window.deiconify()
        previous_window.state('zoomed')

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
       
       

       
    
    def add_placeholder(field,placeholder,is_password=False):#agregar los placeholder a los entries
        style=ttk.Style()
        style.configure('onFocusOut.TEntry',foreground='gray')
        style.configure('onFocusIn.TEntry',foreground='Black')
        def onFocusIn(e):
            if field.get()==placeholder:
                field.delete(0, tk.END)
                field.config(style='onFocusIn.TEntry')
                if is_password:
                    field.config(show='*')

        
        def onFocusOut(e):
            if field.get()=='':
                field.insert(0,placeholder)
                field.config(style='onFocusOut.TEntry')
                if is_password:
                    field.config(show='')
            else:
                field.config(style='onFocusIn.TEntry')
            
        field.insert(0, placeholder)
        field.config(style='onFocusOut.TEntry')
        if is_password:
            field.config(show='')
        field.bind("<FocusIn>",onFocusIn)
        field.bind("<FocusOut>",onFocusOut)
    
    def missing_fields(fields):#los campos deben estar llenos
        missing_field=[]
        for (field,name) in fields:
            if not field.get() or field.get()==name:
                missing_field.append(name)
        if missing_field:
            raise ValueError(f"Los campos '{', '.join(missing_field)}' son obligatorios")
    
    def clean_fields(fields):#limpiar los entries
        style=ttk.Style()
        style.configure("combo.TCombobox",font=('Verdana',15),foreground='gray')
        for (field,is_combobox) in fields:
           if is_combobox:
               field.set('Rol')
           else:
                field.delete(0,tk.END)
           
    def encryct_password(password):#encriptar la contraseña
        salt=bcrypt.gensalt()
        password_hash=bcrypt.hashpw(password.encode(),salt)
        return password_hash
    
    def verify_password(password,password_hash):#verificar la contraseña
        return bcrypt.checkpw(password.encode(),password_hash)
