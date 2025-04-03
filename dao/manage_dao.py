import sqlite3
from db import DataBase
class ManageDAO:
    @staticmethod
    def get_all_values(table,columns):
        try:
            query=f"SELECT {','.join(columns)} FROM {table}"
            return DataBase.fetch_all(query)
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")
  
    @staticmethod
    def get_values_with_condition(table,columns,column_condition,value_condition):
        try:
            query=f"SELECT {','.join(columns)} FROM {table} WHERE {column_condition}=?"
            result=DataBase.fetch_all(query,(value_condition,))
            if not result:
                raise ValueError('No existe registro')
            return result
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")
  
    @staticmethod
    def insert_register(table,columns_insert,values_insert):
        try:
            query=f'''INSERT INTO {table} ({','.join(columns_insert)})
                     VALUES ({','.join(['?' for _ in values_insert])})
                   '''
            DataBase.execute_query(query,values_insert)
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")


    @staticmethod
    def delete_table(table):
        try:
            query=f"DELETE FROM {table}"
            DataBase.execute_query(query)
        except sqlite3.Error as e:
            raise ValueError(f"Error en la base de datos: {e}")
    
    @staticmethod
    def get_values_activity_log():
        try:
           
            query=f'''SELECT activity_log.id_user,users.username,users.rol,activity_log.ip,activity_log.log_date,activity_log.log_time
                      FROM activity_log
                      JOIN users ON activity_log.id_user=users.id
                   '''
            result=DataBase.fetch_all(query)
            return result
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")

        
    
    @staticmethod
    def register_is_exists(table,condition_column,value_condition):
        try:
            query=f"SELECT COUNT(*) FROM {table} WHERE {condition_column}==?"
            return DataBase.fetch_one(query,(value_condition,))
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")
        
    @staticmethod
    def select_register_user(username,rol):
        try:
            query="SELECT password FROM users WHERE username=? AND rol=?"
            result=DataBase.fetch_one(query,(username,rol))
            if not result:
                raise ValueError(f"El usuario '{username}' no existe o el rol es incorrecto")
            return result[0]
        
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")

    @staticmethod
    def delete_register(table,column_condition,value_condition):
        try:
            query=f"DELETE FROM {table} WHERE {column_condition}=?"
            DataBase.execute_query(query,(value_condition,))
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")
        


    @staticmethod
    def view_register(table):
        try:
            query=f"SELECT * FROM {table}"
            result=DataBase.fetch_all(query)
            for register in result:
                print(register)

        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")
        
    @staticmethod
    def generate_code_product():
        try:
            query=f"SELECT MAX(id) FROM products"
            max_id=DataBase.fetch_one(query)[0]

            if max_id is None:
                max_id=0

            return f"P{max_id+1:04d}"
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}")
    
    @staticmethod
    def update_register(table,columns_update,column_condition,values_update,value_condition):
        try:          
            query=f'''UPDATE {table}
                   SET {','.join(f"{col}=?" for col in columns_update)}
                   WHERE {column_condition}=?
                '''
            DataBase.execute_query(query,(*values_update,value_condition))
        except sqlite3.Error as e:
            raise ValueError(f"Error: {e}" )


    @staticmethod
    def delete_table_2():
        try:
            conn=DataBase.connect()
            cursor=conn.cursor()
            # cursor.execute("DELETE FROM products")
            # cursor.execute("DELETE FROM sqlite_sequence WHERE name='products'") 
            cursor.execute("DROP TABLE IF EXISTS activity_log")
        except sqlite3.Error as e:
            raise ValueError(f"Error en la base de datos: {e}")
        finally:
            conn.commit()
            conn.close()