from tkinter import ttk,Toplevel
from style import Style
class CashierPanel:
    def __init__(self,previousWindow):
        self.previousWindow=previousWindow
        self.admin_window=Toplevel(self.previousWindow)
        self.admin_window.title('Área de trabajo')
        self.admin_window.state('zoomed')
        self.admin_window.configure(bg="#0f0f0f")
        Style.styles()
        self.create_cashier_panel()
    
    def create_cashier_panel(self):
        print()