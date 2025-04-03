from tkinter import ttk,Toplevel
import tkinter as tk
from utils import Util
from ui.registerPanel import Register
from style import Style
from dao.manage_dao import ManageDAO
from models.product import Product

class AdminPanel:
    def __init__(self,previous_window):
        self.previous_Window=previous_window
        self.admin_window=Toplevel(self.previous_Window)
        self.admin_window.title('Área de trabajo')
        self.admin_window.state('zoomed')
        self.show_content = True
        self.admin_window.configure(bg="#0f0f0f")
        Style.styles()
        self.create_panel_admin()

    def create_panel_admin(self):
        self.window_size={'width':self.admin_window.winfo_width(), 'height':  self.admin_window.winfo_height()}

        self.window_frame=ttk.Frame(self.admin_window,style='adminFrame.TFrame')
        self.window_frame.pack(fill="both",expand=True,padx=0,pady=0)

        self.sidebar=tk.Frame(self.window_frame,width=230,bg='#151515')
        self.sidebar.pack(side="left", fill="y", expand=False)
        self.sidebar.pack_propagate(False)
        self.content_sidebar()

        self.container_frame=ttk.Frame(self.window_frame,width=self.window_size['width']-230,height=self.window_size['height'],style='admin.TFrame')
        self.container_frame.pack(side="right", fill="both", expand=True)

        self.show_btn=tk.Label(self.container_frame,text='...',bd=2,relief='solid',bg='white')
        self.show_btn.pack_forget()

        self.content_option_menu=ttk.Frame(self.container_frame,width=self.window_size['width']-230,height=self.window_size['height'],style='admin.TFrame')
        self.content_option_menu.pack(side="right", fill="both", expand=True,pady=(20,10))
        self.content_home(None)
        
        Util.view_message("Bienvenido, está todo preparado para ti",'green',self.window_frame)

    
    def content_sidebar(self):
        self.hide_btn=tk.Label(self.sidebar,text='...',bd=2,relief='solid',bg='white')
        self.hide_btn.pack(padx=5,pady=(3,20),ipadx=5,ipady=5,side="top",anchor='e')
        self.hide_btn.bind("<Button-1>",lambda e:self.update_size_sidebar(e))

        self.home=tk.Label(self.sidebar,text='Inicio',bd=1,relief='solid',bg='#1E1E1E',fg='white',cursor='hand2')
        self.home.pack(padx=5,pady=(5,10),ipadx=200,ipady=10)
        self.home.bind("<Button-1>",lambda e:self.content_home(e))

        self.view_stock=tk.Label(self.sidebar,text='Ver Stock',bd=1,relief='solid',bg='#1E1E1E',fg='white',cursor='hand2')
        self.view_stock.pack(padx=5,pady=(5,10),ipadx=200,ipady=10)
        self.view_stock.bind("<Button-1>",lambda e:self.content_view_stock(e))

        self.manage_product=tk.Label(self.sidebar,text='Administrar producto',bd=1,relief='solid',bg='#1E1E1E',fg='white',cursor='hand2')
        self.manage_product.pack(padx=5,pady=(5,10),ipadx=200,ipady=10)
        self.manage_product.bind("<Button-1>",lambda e:self.content_manage_stock(e))

        self.add_new_user=tk.Label(self.sidebar,text='Agregar usuarios',bd=1,relief='solid',bg='#1E1E1E',fg='white',cursor='hand2')
        self.add_new_user.pack(padx=5,pady=10,ipadx=200,ipady=10)
        self.add_new_user.bind("<Button-1>",lambda e:self.register_user(e))

        self.view_activity_login=tk.Label(self.sidebar,text='Ver actividad ',bd=1,relief='solid',bg='#1E1E1E',fg='white',cursor='hand2')
        self.view_activity_login.pack(padx=5,pady=(5,10),ipadx=210,ipady=10)
        self.view_activity_login.bind("<Button-1>",lambda e:self.content_view_activity(e))

        self.view_sales=tk.Label(self.sidebar,text='Ver Ventas',bd=1,relief='solid',bg='#1E1E1E',fg='white',cursor='hand2')
        self.view_sales.pack(padx=5,pady=(5,10),ipadx=200,ipady=10)
        self.view_sales.bind("<Button-1>",lambda e:self.content_view_sales(e))


    def register_user(self,e):
        try:
            self.admin_window.withdraw()
            Register(self.admin_window)
            self.content_home(None)
        except Exception as e:
            Util.view_message(e,'red',self.window_frame)

    def content_home(self,e):
        self.clear_content_option_menu()
        tk.Label(self.content_option_menu,text='INICIO',font=('Verdana',20)).pack(padx=50,pady=(25,0))

    def content_view_stock(self,e):
        self.clear_content_option_menu()
        tk.Label(self.content_option_menu,text='Productos',font=('Verdana',20)).pack(padx=50,pady=(25,0))
        self.create_widget_filter()
        self.create_treeview()
        registers=ManageDAO.get_all_values('products',['code','name','price','quantity','unit_quantity','unit'])
        Util.charge_registers_treeview(self.productsTree,registers)
        
    #usuario,rol,hora,fecha,ip
    #id,id_usuario,rol,ip,
    def content_view_activity(self,e):
        try:
            self.clear_content_option_menu()
            self.activity_tree=ttk.Treeview(self.content_option_menu,columns=('id_user','user','rol','ip','date','time'),show='headings')
            for column,text in [('id_user','Id Usuario'),('user','Usuario'),('rol','Rol'),('ip','IP'),('date','Fecha'),('time','Hora')]:
                self.activity_tree.heading(column,text=text)
                self.activity_tree.column(column,width=150,anchor='center')

            self.activity_tree.pack(pady=(20,10))
        
            registers=ManageDAO.get_values_activity_log()
            print(registers)
            if registers is None:
                raise ValueError('No existen registros')
            Util.charge_registers_treeview(self.activity_tree,registers)
        except Exception as e:
            Util.view_message(e,'red',self.window_frame)
            print(e)

    def content_view_sales(self,e):
        pass


    def content_manage_stock(self,e):
        self.clear_content_option_menu()
        ttk.Label(self.content_option_menu,text='ADMINISTRAR STOCK',font=('Verdana',20)).pack(padx=50,pady=(25,0))

        self.create_widget_filter()
        self.create_treeview()
        
        try:
            self.result_products=ManageDAO.get_all_values('products',['code','name','price','quantity','unit_quantity','unit'])
            Util.charge_registers_treeview(self.productsTree,self.result_products)
        except Exception as e:
            Util.view_message(e,'red',self.window_frame)

        
        btn_frame=ttk.Frame(self.content_option_menu,style="admin.TFrame")
        btn_frame.pack(anchor='center',pady=(20,10))
        
        ttk.Button(btn_frame,text='Agregar',style='btn.TButton',width=10,command=self.content_add_product).grid(row=0,column=0,padx=25,pady=(30,10),ipady=6)
        ttk.Button(btn_frame,text='Editar',style='btn.TButton',width=10,command=self.content_edit_product).grid(row=0,column=1,padx=25,pady=(30,10),ipady=6)
        ttk.Button(btn_frame,text='Eliminar',style='btn.TButton',width=10,command=self.content_delete_product).grid(row=0,column=2,padx=25,pady=(30,10),ipady=6)
        

    def content_add_product(self):
        self.clear_content_option_menu()
        ttk.Label(self.content_option_menu,text='NUEVO PRODUCTO',font=('Verdana',20)).pack(padx=50,pady=(25,0))
        self.create_treeview()
        self.productsTree.pack_forget()
        self.create_widget_to_product()
        self.unit_combobox.set('Unidad de medida')
        Util.add_placeholder(self.description_product,'Nombre')
        Util.add_placeholder(self.price_product,'Precio')
        Util.add_placeholder(self.quantity_product,'Cantidad')
        Util.add_placeholder(self.unit_quantity,'Unidad cantidad')
        

        btn_frame=ttk.Frame(self.content_option_menu,style="admin.TFrame")
        btn_frame.pack(anchor='center',pady=(20,10))

        ttk.Button(btn_frame,text='Registrar',style='btn.TButton',width=10,command=self.register_new_product).grid(row=0,column=0,padx=25,pady=(30,10),ipady=6)
        ttk.Button(btn_frame,text='Cancelar',style='btn.TButton',width=10,command=lambda:self.content_manage_stock(None)).grid(row=0,column=1,padx=25,pady=(30,10),ipady=6)
    
    
    def register_new_product(self):
        try:
            Util.missing_fields([(self.description_product,'Nombre'),(self.price_product,'Precio'),(self.quantity_product,'Cantidad'),
                                 (self.unit_quantity,'Unidad cantidad'),(self.unit_combobox,'Unidad de medida')])
            product=Product(self.code_product.get(),self.description_product.get(),self.price_product.get(),
                            self.quantity_product.get(),self.unit_quantity.get(),self.unit_combobox.get())
            
            result=ManageDAO.register_is_exists('products','code',product.code)
            if result[0]>1:
                raise ValueError('Error, código repetido')
            ManageDAO.insert_register('products',['code','name','price','quantity','unit_quantity','unit'],((product.code,product.name,product.price,product.quantity,
                                                     product.unit_quantity,product.unit)))

            Util.add_register_treeview(self.productsTree,(product.code,product.name,product.price,product.quantity))
            ManageDAO.view_register('products')#temporal
            Util.clean_fields([(self.description_product,'Nombre',False,False),(self.price_product,'Precio',False,False),
                           (self.quantity_product,'Cantidad',False,False),(self.unit_quantity,'Unidad cantidad',False,False),
                           (self.unit_combobox,'Unidad de medida',True,False)])
            Util.view_message('Se guardó correctamente','green',self.window_frame)

            self.code_product.config(state="normal")
            self.code_product.insert(0,self.generate_code())
            self.code_product.config(state="disabled")
            # ManageDAO.delete_table()
            # ManageDAO.view_register()
        except Exception as e:
            Util.view_message(e,'red',self.window_frame)
            print(e)
    

    def content_edit_product(self):
        try:
            values=()
            values=Util.selection_register_treeview(self.productsTree)
            if not values:
                raise ValueError('No se ha seleccionado un producto')
            self.clear_content_option_menu()
            self.create_treeview()
            self.productsTree.pack_forget()
            print(values)
            result={
                'code':values[0],
                'name':values[1],
                'price':values[2],
                'quantity':values[3],
                'unit_quantity':values[4],
                'unit':values[5]
            }
            self.create_widget_to_product(True,False,result)
            Util.add_placeholder(self.price_product,'Precio',is_normal=False)
            Util.add_placeholder(self.quantity_product,'Cantidad',is_normal=False)
            Util.add_placeholder(self.unit_quantity,'Unidad cantidad',is_normal=False)

            btn_frame=ttk.Frame(self.content_option_menu,style="admin.TFrame")
            btn_frame.pack(anchor='center',pady=(20,10))

            ttk.Button(btn_frame,text='Editar',style='btn.TButton',width=10,command=self.edit_product).grid(row=0,column=0,padx=25,pady=(30,10),ipady=6)
            ttk.Button(btn_frame,text='Cancelar',style='btn.TButton',width=10,command=lambda:self.content_manage_stock(None)).grid(row=0,column=1,padx=25,pady=(30,10),ipady=6)

            
        except Exception as e:
            Util.view_message(e,'red',self.window_frame)
            print(e)
        

    def edit_product(self):
       try:
            Util.missing_fields([(self.price_product,'Precio'),(self.quantity_product,'Cantidad'),
                                 (self.unit_quantity,'Unidad cantidad'),(self.unit_combobox,'Unidad de medida')])
            
            product=Product(self.code_product.get(),self.description_product.get(),self.price_product.get(),
                            self.quantity_product.get(),self.unit_quantity.get(),self.unit_combobox.get())
            
            ManageDAO.update_register('products',['price','quantity','unit_quantity','unit'],'code',(product.price,product.quantity,product.unit_quantity,product.unit),product.code)
            registers=ManageDAO.get_all_values('products',['code','name','price','quantity','unit_quantity','unit'])

            Util.charge_registers_treeview(self.productsTree,registers)

            self.content_manage_stock(None)

            Util.view_message('Cambios guardados correctamente','green',self.window_frame)
       except Exception as e:
           Util.view_message(e,'red',self.window_frame)

    def generate_code(self):
        self.code_product.config(state="normal")
        self.code_product.delete(0,tk.END)
        return ManageDAO.generate_code_product()

    

    def content_delete_product(self):
        try:

            values=()
            values=Util.selection_register_treeview(self.productsTree)
            print(values)
            if not values:
                raise ValueError('No se ha seleccionado un producto')
            self.clear_content_option_menu()
            self.create_treeview()
            self.productsTree.pack_forget()
            result={
                'code':values[0],
                'name':values[1],
                'price':values[2],
                'quantity':values[3],
                'unit_quantity':values[4],
                'unit':values[5]
            }
            self.create_widget_to_product(False,True,result)
            btn_frame=ttk.Frame(self.content_option_menu,style="admin.TFrame")
            btn_frame.pack(anchor='center',pady=(20,10))

            ttk.Button(btn_frame,text='Eliminar',style='btn.TButton',width=10,command=self.delete_product).grid(row=0,column=0,padx=25,pady=(30,10),ipady=6)
            ttk.Button(btn_frame,text='Cancelar',style='btn.TButton',width=10,command=lambda:self.content_manage_stock(None)).grid(row=0,column=1,padx=25,pady=(30,10),ipady=6)

        except Exception as e:
            Util.view_message(e,'red',self.window_frame)
        
    
    def delete_product(self):
        try:    
            ManageDAO.delete_register('products','code',self.code_product.get())
            registers=ManageDAO.get_all_values('products',['code','name','price','quantity','unit_quantity','unit'])

            Util.charge_registers_treeview(self.productsTree,registers)

            self.content_manage_stock(None)

            Util.view_message('Cambios guardados correctamente','green',self.window_frame)
        except Exception as e:
           Util.view_message(e,'red',self.window_frame)

    def create_widget_filter(self):
        filter_frame=ttk.Frame(self.content_option_menu,style="admin.TFrame")
        filter_frame.pack(anchor='center',pady=(20,10))
        options=('Código','Nombre')
        filter_combobox=ttk.Combobox(filter_frame,values=options,width=28,style='combo.TCombobox')
        filter_combobox.grid(row=0,column=0,padx=25,pady=(30,10),ipadx=60,ipady=10)
        filter_combobox.set('Buscar por')

        find_filter=ttk.Entry(filter_frame,width=40,style='entry-normal.TEntry')
        find_filter.grid(row=0,column=1,padx=25,pady=(30,10),ipadx=60,ipady=10)
        # Util.add_placeholder(find_filter,'Buscar')
        find_filter.bind("<FocusIn>",lambda e:self.admin_window.after(1000,lambda:Util.verify_entry(e,self.productsTree,
                                                                find_filter,'products',['code','name','price','quantity','unit_quantity','unit'])))

        column_mapping={
            'Código':'code',
            'Nombre':'name',
            'Precio':'price',
            'Cantidad':'quantity'
        }
        ttk.Button(filter_frame,text='Buscar',style='btn.TButton',width=7,
                   command=lambda:Util.filter_register_treeview(self.productsTree,filter_combobox,find_filter,
                    column_mapping,'products',self.window_frame)).grid(row=0,column=2,padx=25,pady=(30,10),ipady=5)
        
    def create_treeview(self):
        self.productsTree=ttk.Treeview(self.content_option_menu,columns=('code','name','price','quantity','unit_quantity','unit'),show='headings')

        for column,text in [('code','Código'),('name','Nombre'),('price','Precio'),('quantity','Cantidad'),('unit_quantity','Unidad Cantidad'),('unit','Unidad medida')]:
            self.productsTree.heading(column,text=text)
            if column!='name':
                self.productsTree.column(column,width=150,anchor='center')
        self.productsTree.column('name',width=300,anchor='center')
        
        self.productsTree.pack(pady=(20,10))

    def update_size_sidebar(self,e):
        def hide_sidebar(i):    
             if i>0:
                 self.sidebar.config(width=i-10)
                 self.admin_window.after(5,hide_sidebar,i-10)
             else:
                 self.sidebar.config(width=1)
                 self.show_btn.pack(padx=5,pady=5,ipadx=5,ipady=5,side="left",anchor='ne')
                 self.show_btn.bind("<Button-1>",lambda e:self.update_size_sidebar(e))
                 

        def show_sidebar(i):
             if i<230:
                 self.sidebar.config(width=i+10)
                 self.admin_window.after(5,show_sidebar,i+10)
             
        width=self.sidebar.winfo_width()
        if width==230:
            self.admin_window.after(5,hide_sidebar,230)
        else:
            self.show_btn.pack_forget()
            self.admin_window.after(5,show_sidebar,0)

    
    def clear_content_option_menu(self):
        for widget in self.content_option_menu.winfo_children():
            widget.destroy()
   
    def create_widget_to_product(self,is_edit=False,is_delete=False,result=None):
        self.code_product=ttk.Entry(self.content_option_menu,width=40,style='entry.TEntry')
        self.code_product.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        if is_edit or is_delete:
            self.code_product.insert(0,result['code'])
        else: 
            self.code_product.insert(0,self.generate_code())
        self.code_product.config(state="disabled")

        self.description_product=ttk.Entry(self.content_option_menu,width=40,style='entry.TEntry')
        self.description_product.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        if is_edit or is_delete:
            self.description_product.insert(0,result['name'])
            self.description_product.config(state="disabled")
        
        
        self.price_product=ttk.Entry(self.content_option_menu,width=40,style='entry.TEntry')
        self.price_product.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        if is_edit or is_delete:
            self.price_product.insert(0,result['price'])
            self.price_product.config(foreground='black')
        if is_delete:
            self.price_product.config(state="disabled")

        self.quantity_product=ttk.Entry(self.content_option_menu,width=40,style='entry.TEntry')
        self.quantity_product.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        if is_edit or is_delete:
            self.quantity_product.insert(0,result['quantity'])
            self.quantity_product.config(foreground='black')
        if is_delete:
            self.quantity_product.config(state="disabled")

        self.unit_quantity=ttk.Entry(self.content_option_menu,width=40,style='entry.TEntry')
        self.unit_quantity.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        if is_edit or is_delete:
            self.unit_quantity.insert(0,result['unit_quantity'])
            self.unit_quantity.config(foreground='black')
        if is_delete:
            self.unit_quantity.config(state="disabled")

        if is_delete:
            self.unit_entry=ttk.Entry(self.content_option_menu,width=40,style='entry.TEntry')
            self.unit_entry.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
            self.unit_entry.insert(0,result['unit'])
            self.unit_entry.config(foreground='black')
            self.unit_entry.config(state="disabled")
            return

        options=('kilogramos','gramos','miligramos','litros','libras')
        self.unit_combobox=ttk.Combobox(self.content_option_menu,values=options,width=37,style='combo.TCombobox')
        self.unit_combobox.pack(padx=25,pady=(30,10),ipadx=60,ipady=10)
        if is_edit:
            self.unit_combobox.set(result['unit'])
            self.unit_combobox.config(foreground='black')
        