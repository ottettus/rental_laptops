from database.db import Database

class Laptop:
    def __init__(self, id: int, mark: str, model:str , spec:str, status:bool):
        self.id = id
        self.mark = mark
        self.model = model
        self.spec = spec
        self.status = status
        self.db = Database()

    def add_laptop(self):
        query = "INSERT INTO laptops(mark, model, spec, status) VALUES (%s, %s, %s, %s)"
        try:
            self.db.execute_query(query, (self.mark, self.model, self.spec, self.status))
            print(f"Laptop added successfully")
        except Exception as e:
            print(f"Error adding laptop: {e}")

    def delete_laptop(self):
        query = "DELETE FROM laptops WHERE id = %s"
        try:
            self.db.execute_query(query, (self.id,))
            print("Laptop deleted!")
        except Exception as e:
            print(f"Error deleting laptop: {e}")

    
    def update_laptop_rent_status(self, new_status:bool, laptop_id: int = None):
        query = "UPDATE laptops SET status = %s WHERE id = %s"
        try:
            self.db.execute_query(query,(new_status, laptop_id))
        except Exception as e:
            print("Error: {e}")

