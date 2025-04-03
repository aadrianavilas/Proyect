from tkinter import ttk

class Style:
    def styles():
        style=ttk.Style()
        style.configure("entry.TEntry",font=('Verdana',15),foreground='gray')
        style.configure("entry-normal.TEntry",font=('Verdana',15),foreground='black')
        style.configure("container.TFrame",background='Black')
        style.configure("combo.TCombobox",font=('Verdana',15),foreground='gray')
        style.configure("TCombobox", font=('Verdana', 15))  
        style.configure("TCombobox.listbox", font=("Verdana", 18))
        style.configure("adminFrame.TFrame",background='#0f0f0f')
        style.configure("admin.TFrame",background='#1E1E1E')
        style.configure("login.TFrame",background='Black')
        style.configure("register.TLabel",background='Black',font=('Verdana',13),foreground='White')
        style.configure("custom.TFrame",background='Black')
        style.configure("personal.TFrame",background='Black')
        style.configure("btn.TButton",font=('Verdana',13),cursor='hand2')

