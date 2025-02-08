from datetime import datetime
from database.db import Database
from models.laptops import Laptop

class Rental:
    def __init__(self, id=None, client_id=None, laptop_id=None, rental_date=None, return_date=None, status="Open"):
        self.id = id
        self.client_id = client_id
        self.laptop_id = laptop_id
        self.rental_date = rental_date if rental_date else datetime.now()
        self.return_date = return_date
        self.status = status
        self.db = Database()


    def check_laptop_avaliablity(self, laptop_id):
        query = "SELECT status FROM laptops WHERE id = %s"
        result = self.db.fetch_query(query,(laptop_id,))
        if result and result[0][0] == True:
            return True
        else:
            print("Laptop is not avariable for rent")
            return False



    def create_rental(self):
        query = "INSERT INTO rentals(client_id, laptop_id, rental_date, return_date, status) VALUES (%s, %s, %s, %s, %s)"
        try:
            if self.check_laptop_avaliablity(self.laptop_id):
                self.db.execute_query(query, (self.client_id, self.laptop_id, self.rental_date, self.return_date, self.status))
                laptop = Laptop(id=self.laptop_id, mark='', model='', spec='', status=False)
                laptop.update_laptop_rent_status(new_status=False, laptop_id=self.laptop_id)
                print(f"Rental created successfully")
            else:
                print("Rental creation failed")
        except Exception as e:
            print(f"Error creating rental: {e}")


    def update_rental_return_status(self):
        query = "UPDATE rentals SET return_date = %s, status = %s WHERE laptop_id = %s"
        try:
            self.db.execute_query(query, (self.return_date, self.status, self.laptop_id))
            laptop = Laptop(id=self.laptop_id, mark='', model='', spec='', status=True)
            laptop.update_laptop_rent_status(new_status=True, laptop_id=self.laptop_id)
            print(f"Update rental returned successfully")
        except Exception as e:
            print(f"Error returning rental: {e}")


    def __str__(self):
        return f"Rental {self.id}: Client {self.client_id}, Laptop {self.laptop_id}, Rental Date: {self.rental_date}, Return Date: {self.return_date}, Status: {'Active' if self.status else 'Returned'}"