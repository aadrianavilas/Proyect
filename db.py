import sqlite3


class DataBase:
    def __init__(self,db_name='facturacion'):
        self.db_name=db_name
        self.create_table()

    @staticmethod
    def connect(db_name='facturacion'):
        return sqlite3.connect(db_name)
    

    def create_table(self):
        try:
            conn=self.connect()
            cursor=conn.cursor()
            cursor.execute("PRAGMA foreign_keys = ON;")
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    username TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    last_names TEXT NOT NULL,
                    names TEXT NOT NULL,
                    rol TEXT NOT NULL  
                )            
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS products(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    price REAL NOT NULL,
                    quantity INTEGER NOT NULL,
                    unit_quantity INTEGER NOT NULL,
                    unit TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS activity_log(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_user INTEGER NOT NULL,
                    ip TEXT NOT NULL,
                    log_date TEXT NOT NULL,
                    log_time TEXT NOT NULL,
                    FOREIGN KEY (id_user) REFERENCES users (id) ON DELETE CASCADE  
                )

            ''')
        except sqlite3.Error as e:
            raise ValueError(f"Error en la base de datos: {e}")
        finally:
            conn.commit()
            conn.close()
    @staticmethod
    def execute_query(query,params=()):
        try:
            conn=DataBase.connect()
            cursor=conn.cursor()
            cursor.execute(query,params)
        except sqlite3.Error as e:
            raise ValueError(e)
        finally:
            conn.commit()
            conn.close()

    def fetch_all(query,params=()):
        try:
            conn=DataBase.connect()
            cursor=conn.cursor()
            cursor.execute(query,params)
            result=cursor.fetchall()
            return result
        except sqlite3.Error as e:
            raise ValueError(e)
        finally:
            conn.close()

    def fetch_one(query,params=()):
        try:
            conn=DataBase.connect()
            cursor=conn.cursor()
            cursor.execute(query,params)
            result=cursor.fetchone()
            return result
        except sqlite3.Error as e:
            raise ValueError(e)
        finally:
            conn.close()


   
