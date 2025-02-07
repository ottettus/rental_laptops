from datetime import datetime
from database.db import Database

class Rental:
    def __init__(self, id=None, client_id=None, laptop_id=None, rental_date=None, return_date=None, status=True):
        self.id = id
        self.client_id = client_id
        self.laptop_id = laptop_id
        self.rental_date = rental_date if rental_date else datetime.now()
        self.return_date = return_date
        self.status = status
        self.db = Database()


    def create_rental(self):
        query = "INSERT INTO rental(client_id, laptop_id, rental_date, return_date, status) VALUES (%s, %s, %s, %s, %s) RETURNING id"
        try:
            self.id = self.db.execute_query(query, (self.client_id, self.laptop_id, self.rental_date, self.return_date, self.status), fetch_one=True)
            print(f"Rental created successfully with ID: {self.id}")
        except Exception as e:
            print(f"Error creating rental: {e}")


    def return_rental(self):
        query = "UPDATE rental SET return_date = %s, status = %s WHERE id = %s"
        try:
            self.return_date = datetime.now()
            self.status = False
            self.db.execute_query(query, (self.return_date, self.status, self.id))
            print(f"Rental {self.id} returned successfully")
        except Exception as e:
            print(f"Error returning rental: {e}")

    def __str__(self):
        return f"Rental {self.id}: Client {self.client_id}, Laptop {self.laptop_id}, Rental Date: {self.rental_date}, Return Date: {self.return_date}, Status: {'Active' if self.status else 'Returned'}"