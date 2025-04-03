class Product:
    def __init__(self,code,name,price,quantity,unit_quantity,unit):
        self.code=code
        self.name=self.validate_name(name)
        self.price=self.validate_price(price)
        self.quantity=self.validate_quantity(quantity)
        self.unit_quantity=self.validate_unit_quantity(unit_quantity)
        self.unit=self.validate_unit(unit)
    

    def validate_name(self,name):
        if len(name)<4 and len(name)>21 or name.isdigit(): 
            raise ValueError('Nombre inválido')
        return name.lower()
    
    def validate_price(self,price):#3
        if not price.replace('.','',1).isdigit():
            raise ValueError('Precio no válido')
        return float(price)

    def validate_quantity(self,quantity):
        if not quantity.isdigit():
            raise ValueError('Cantidad no válida')
        return int(quantity)
    
    def validate_unit_quantity(self,unit_quantity):
        if not unit_quantity.isdigit():
            raise ValueError('Cantidad no válida')
        return int(unit_quantity)
    def validate_unit(self,unit):
        unit=unit.lower()
        if not (unit=='kilogramos' or unit=='gramos'or unit=='mililitros' or unit=='litros' or unit=='libras'):
            raise ValueError('Unidad de medida no válida')
        return unit