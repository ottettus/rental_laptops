class Client:
    def __init__(self, id: int, name: str, surname: str, email: str):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email

    def __str__(self):
        return(f"id: {self.id}, name: {self.name}, surname: {self.surname}, email: {self.email}")
    
    @classmethod
    def display_all_clients(all_clients_list):
        for client in all_clients_list:
            print(client)