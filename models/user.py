from utils import Util

class User:
    def __init__(self,user,password,confirm_password,last_names,names,rol):

        self.user=self.validate_user(user)
        self.password=self.validate_password(password)
        self.confirm_password=self.validate_confirm_password(password,confirm_password)
        self.last_names=self.validate_last_names(last_names)
        self.names=self.validate_names(names)
        self.rol=rol

    
    def validate_user(self,user):
        if len(user)<6 and len(user)>20:
            raise ValueError('El usuario debe tener al menos 5 caracteres')
        return user.lower()
        
    def validate_password(self,password):
        if len(password)<6:
            raise ValueError('La contraseña debe tener al menos 5 caracteres')
        hash_password=Util.encryct_password(password)
        return hash_password
        
    def validate_confirm_password(self,password,confirm_password):
        if password!=confirm_password:
            raise ValueError('Las contraseñas no coinciden')
        return confirm_password

    def validate_last_names(self,last_names):
        if len(last_names)<3:
            raise ValueError('¿Hay apellidos muy cortitos?')

        return last_names.upper()
    
    def validate_names(self,names):
        if len(names)<2:
            raise ValueError('¿Hay apellidos muy cortitos?')

        return names.upper()


        
        