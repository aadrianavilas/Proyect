class ActivityLog:
    def __init__(self,id_user,ip,date,time):
        self.id_user=self.validate_id_user(id_user)
        self.ip=self.validate_ip(ip)
        self.date=self.validate_date(date)
        self.time=self.validate_time(time)

    def validate_id_user(self,id_user):
        if not id_user:
            raise ValueError('Id no válida')
        return int(id_user)
    
    def validate_ip(self,ip):
        if not ip:
            raise ValueError('Ip no válida')
        return str(ip)
    
    def validate_date(self,date):
        if not date:
            raise ValueError('Fecha no válida')
        return str(date)
    
    def validate_time(self,time):
        if not time:
            raise ValueError('Hora no válida')
        return str(time)


