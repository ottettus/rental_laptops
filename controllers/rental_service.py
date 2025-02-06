
from models.clients import Client
from models.laptops import Laptop
from database.db import Database

import psycopg2


class RentalServices:
    def __init__(self):
        self.db = Database()


    def update_laptop_status(self, id:str, new_status:str):
        query = "UPDATE laptops SET status = %s WHERE id = %s"
        try:
            self.db.execute_query(query, (new_status, id))
            print('Status Updated')
        except psycopg2.Error as e:
            print(f"Bad query!: Error: {e}")


    def new_client(self, name:str, surname:str, email:str):
        query = "INSERT INTO clients(name, surname, email) VALUES (%s, %s, %s)"
        try:
            self.db.execute_query(query,(name, surname, email))
            print("New client addded")
        except psycopg2.Error as e:
            print(f"Bad fetch! Error: {e}")

    
    def delete_client(self, id:int):
        query = "DELETE FROM clients WHERE id=%s"
        try:
            self.db.execute_query(query, (id,))
            print(f"Client with id={id} was deleted")
        except psycopg2.Error as e:
            print(f"Bad fetch! Error: {e}")

    
    def get_all_clients(self):
        query = "SELECT * FROM clients"
        try:
            clients_data = self.db.fetch_query(query)
            clients = [Client(id, name, surname, email) for id, name, surname, email in clients_data]
            return clients
        except psycopg2.Error as e:
            print(f"Bad fetch! Error: {e}")


    def get_all_laptops(self):
        query = "SELECT * FROM laptops"
        try:
            laptops_data = self.db.fetch_query(query)
            laptops = [Laptop(id, mark, model, spec, status) for (id, mark, model, spec, status) in laptops_data]
            return laptops
        except psycopg2.Error as e:
            print(f"Bad fetch! Error: {e}")
