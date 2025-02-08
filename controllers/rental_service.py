
from models.clients import Client
from models.laptops import Laptop
from models.rental import Rental
from database.db import Database
from datetime import datetime

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


    def laptop_rent_ser(self, id_client, id_laptop):
        actualy_data = datetime.now()
        new_res = Rental(id=None, client_id=id_client, laptop_id=id_laptop, rental_date=actualy_data, return_date=None, status='Open')
        new_res.create_rental()

