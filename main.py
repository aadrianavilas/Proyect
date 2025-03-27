import tkinter as tk
from tkinter import ttk

from ui.personalPanel import Personal
from ui.admin_panel import AdminPanel

root=tk.Tk()
root.title('Home')
#Personal(root)
root.state('zoomed')
root.configure(bg="#0f0f0f")
AdminPanel(root)
root.mainloop()