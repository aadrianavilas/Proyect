# import tkinter as tk
# from tkinter import ttk,Toplevel

# class funcion_prueba:
#     def __init__(self,root):
#         self.admin_window=Toplevel(root)
#         self.admin_window.title('Área de trabajo')
#         self.window_size={'width': 0, 'height': self.admin_window.winfo_height()}
#         self.admin_window.bind("<Configure>", lambda e: self.update_size_window(e))
#         self.admin_window.state('zoomed')
#         self.canvas=tk.Canvas(self.admin_window,width=230,height=self.window_size['height'],bg='Black')
#         self.canvas.pack(padx=0,pady=3)
#     def update_size_window(self,e):
#         self.admin_window.update_idletasks()
#         width=self.admin_window.winfo_width()
#         height=self.admin_window.winfo_height()
#         self.window_size = {'width': width, 'height': height}
#         self.canvas.config(height=self.window_size['height'])
#         print(self.window_size)
# price=input('Ingrese: ')
# # print(price.isdigit())
# # print(price.replace('.','',1).isdigit())
# # if not price.isdigit() or price.replace('.','',1).isdigit():
# #             print('Precio no válido')
# if not price:
#     print('Vacio')
print(','.join(f"{col}=?" for col in ['code','name','price','quantity','unit_quantity','unit']))