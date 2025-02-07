from database.db import Database


class Client:
    def __init__(self, id, name: str, surname: str, email: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.db = Database()

    def __str__(self):
        return(f"id: {self.id}, name: {self.name}, surname: {self.surname}, email: {self.email}")
    
    
    def add_new_client(self):
        query = "INSERT INTO clients(name, surname, email) VALUES(%s,%s,%s)"
        try:
            self.db.execute_query(query, (self.name, self.surname, self.email))
            print(f"Client added successfully")
        except Exception as e:
            print("Error: {e}")


    def delete_client(self):
        query = "DELETE FROM clients WHERE id = %s"
        try:
            self.db.execute_query(query, (self.id,))
        except Exception as e:
            print("Error: {e}")

        
    
    
    @classmethod
    def display_all_clients(cls, all_clients_list):
        for client in all_clients_list:
            print(client)