from datetime import datetime
from database.db import Database



class Rental:
    def __init__(self,id:int, client_id: int, laptop_id: int, rental_date: datetime, return_date: datetime, status:bool ):
        self.db = Database()
        self.id = id
        self.client_id = client_id
        self.laptop_id = laptop_id
        self.rental_date = datetime.now()
        self.return_date = return_date
        self.status = status

    def __str__(self):
        print(f"id: {self.id}, client_id: {self.client_id}, laptop_id: {self.laptop_id}, return_date: {self.return_date} status: {'Active' if self.status else 'Returned'}")


    def create_rental(self):
        query = "INSERT INTO rental(client_id, laptop_id, rental_date, return_date, status) VALUES (%s,%s,%s,%s,True)"
        try:
            self.db.execute_query(query,(self.client_id, self.laptop_id, self.rental_date,self.return_date))
            print("Added")
        except Exception as e:
            print(f"Error: {e}")

rn = Rental(client_id=1,laptop_id=1,return_date=(2025,2,10))
            