
from models.clients import Client
from models.laptops import Laptop
from database.db import Database

import psycopg2


class RentalServices:
    def __init__(self):
        self.db = Database()

    def new_client(self, name: str, surname:str, email:str):
        client = Client(id = None, name = name, surname=surname, email=email)
        client.add_new_client()

    
    def delete_client(self, id:int):
        client_to_delete = Client(id=id, name=None, surname=None, email=None)
        client_to_delete.delete_client()


    def new_laptop(self, mark, model, spec):
        laptop = Laptop(id=None, mark=mark, model=model, spec=spec, status=False)
        laptop.add_laptop()


    def delete_laptop(self, id:int):
        laptop_to_delete = Laptop(id=id, mark=None, model= None, spec=None, status=None)
        laptop_to_delete.delete_laptop()


    def view_all_laptops(self):
        query = "SELECT * FROM laptops"
        try:
            results = self.db.fetch_query(query)
        except Exception as e:
            print("All laptops list Error: {e}")
        for result in results:
                print(result)

    
    def View_all_clients(self):
        query = "SELECT * FROM clients"
        try:
            result = self.db.fetch_query(query)
        except Exception as e:
            print("All clients list Error: {e}")
        for result in result:
            print(result)




    def update_laptop_status(self, id:str, new_status:str):
        query = "UPDATE laptops SET status = %s WHERE id = %s"
        try:
            self.db.execute_query(query, (new_status, id))
            print('Status Updated')
        except psycopg2.Error as e:
            print(f"Bad query!: Error: {e}")



    # def delete_laptop(self, id:int):
    #     query = "DELETE FROM laptops WHERE id=%s"
    #     try:
    #         self.db.execute_query(query, (id,))
    #         print(f"Laptop with id={id} was deleted")
    #     except psycopg2.Error as e:
    #         print(f"Bad fetch! Error: {e}")

    
    # def get_all_clients(self):
    #     query = "SELECT * FROM clients"
    #     try:
    #         clients_data = self.db.fetch_query(query)
    #         clients = [Client(id, name, surname, email) for id, name, surname, email in clients_data]
    #         return clients
    #     except psycopg2.Error as e:
    #         print(f"Bad fetch! Error: {e}")


    # def get_all_laptops(self):
    #     query = "SELECT * FROM laptops"
    #     try:
    #         laptops_data = self.db.fetch_query(query)
    #         laptops = [Laptop(id, mark, model, spec, status) for (id, mark, model, spec, status) in laptops_data]
    #         return laptops
    #     except psycopg2.Error as e:
    #         print(f"Bad fetch! Error: {e}")
