from datetime import datetime
from database.db import Database

class Rental:
    def __init__(self, client_id: int, laptop_id: int, rental_date: datetime = None, return_date: datetime = None, status: bool = True, id: int = None):
        self.db = Database()
        self.id = id
        self.client_id = client_id
        self.laptop_id = laptop_id
        self.rental_date = rental_date if rental_date else datetime.now()
        self.return_date = return_date
        self.status = status

    def __str__(self):
        return f"id: {self.id}, client_id: {self.client_id}, laptop_id: {self.laptop_id}, rental_date: {self.rental_date}, return_date: {self.return_date}, status: {'Active' if self.status else 'Returned'}"

    def create_rental(self):
        query = "INSERT INTO rentals (client_id, laptop_id, rental_date, return_date, status) VALUES (%s, %s, %s, %s, %s)"
        try:
            self.db.execute_query(query, (self.client_id, self.laptop_id, self.rental_date, self.return_date, self.status))
        except Exception as e:
            print(f"Error: {e}")

    def return_rental(self):
        query = "UPDATE rentals SET return_date = %s, status = %s WHERE id = %s"
        try:
            self.return_date = datetime.now()
            self.status = False
            self.db.execute_query(query, (self.return_date, self.status, self.id))
            print(f"Rental {self.id} has been returned.")
        except Exception as e:
            print(f"Error returning rental: {e}")

            