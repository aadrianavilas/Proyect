from tkinter import ttk,Toplevel
import tkinter as tk
from utils import Util
class AdminPanel:
    def __init__(self,previousWindow):
        self.previousWindow=previousWindow
        self.admin_window=Toplevel(self.previousWindow)
        self.admin_window.title('Área de trabajo')
        self.admin_window.state('zoomed')
        self.admin_window.configure(bg="#0f0f0f")

        self.admin_window.update_idletasks()
        self.window_size={'width':self.admin_window.winfo_width(), 'height':  self.admin_window.winfo_height()}
        self.admin_window.bind("<Configure>", lambda e: self.update_size_window(e))

        style=ttk.Style()
        style.configure("adminFrame.TFrame",background='#0f0f0f')
        style.configure("admin.TFrame",background='gray')

        self.window_frame=ttk.Frame(self.admin_window,style='adminFrame.TFrame')
        self.window_frame.pack(fill="both",expand=True,padx=0,pady=0)

        self.frame_menu=tk.Frame(self.window_frame,width=230,bg='White')
        self.frame_menu.pack(side="left", fill="y")
        # self.view_product=tk.Label(self.frame_menu,text='Ver productos',bd=2,relief='solid')
        # self.view_product.pack(padx=5,pady=5)

        self.container_frame=ttk.Frame(self.window_frame,width=self.window_size['width']-230,height=self.window_size['height'],style='admin.TFrame')
        self.container_frame.pack(side="right", fill="both", expand=True)

        Util.view_message("Bienvenido, está todo preparado para ti",'green',self.window_frame)
        tk.Label(self.container_frame,text='hola',fg='red').pack()


    def update_size_window(self,e):
        self.admin_window.update_idletasks()#actualiza la ventana
        width=self.admin_window.winfo_width()
        height=self.admin_window.winfo_height()

        self.window_size = {'width': width, 'height': height}  # Guardar las dimensiones de la ventana
        
        self.window_frame.config(width=self.window_size['width'], height=self.window_size['height'])

        self.frame_menu.config(width=230,height=self.window_size['height'])
 
        self.container_frame.config(width=self.window_size['width']-230, height=self.window_size['height'])
 
        print(self.window_size)