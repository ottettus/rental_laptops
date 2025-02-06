from database.db import Database


class Laptop:
    def __init__(self, id: int, mark: str, model: str, spec: str, status: bool):
        self.db = Database()
        self.id = id
        self.mark = mark
        self.model = model
        self.spec  = spec
        self.status = status
        

    def __str__(self):
        return(f"id: {self.id}, mark: {self.mark}, model: {self.model}, spec: {self.spec}, status: {self.status}")
    
    def add_new_laptop(self, mark, model, spec, status):
        query = "INSERT INTO laptops(mark, model, spec, status) VALUES(%s, %s, %s, False)"
        try:
            self.db.execute_query(query(mark, model, spec, status))
        except Exception as e:
            print("Error: {e}")
    
    @classmethod
    def display_all_laptops(cls, laptops_list):
        for laptop in laptops_list:
            print(laptop)