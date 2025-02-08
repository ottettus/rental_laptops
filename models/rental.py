from datetime import datetime
from database.db import Database

class Rental:
    def __init__(self, id=None, client_id=None, laptop_id=None, rental_date=None, return_date=None, status="Open"):
        self.id = id
        self.client_id = client_id
        self.laptop_id = laptop_id
        self.rental_date = rental_date if rental_date else datetime.now()
        self.return_date = return_date
        self.status = status
        self.db = Database()


    def create_rental(self):
        query = "INSERT INTO rentals(client_id, laptop_id, rental_date, return_date, status) VALUES (%s, %s, %s, %s, %s)"
        try:
            self.db.execute_query(query, (self.client_id, self.laptop_id, self.rental_date, self.return_date, self.status))
            print(f"Rental created successfully")
        except Exception as e:
            print(f"Error creating rental: {e}")


    def update_rental_return_status(self):
        query = "UPDATE rentals SET return_date = %s, status = %s WHERE id = %s"
        try:
            self.return_date = datetime.now()
            self.status = False
            self.db.execute_query(query, (self.return_date, self.status, self.id))
            print(f"Update rental returned successfully")
        except Exception as e:
            print(f"Error returning rental: {e}")

    def __str__(self):
        return f"Rental {self.id}: Client {self.client_id}, Laptop {self.laptop_id}, Rental Date: {self.rental_date}, Return Date: {self.return_date}, Status: {'Active' if self.status else 'Returned'}"