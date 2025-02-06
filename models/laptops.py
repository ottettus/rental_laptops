class Laptop:
    def __init__(self, id: int, mark: str, model: str, spec: str, status: bool):
        self.id = id
        self.mark = mark
        self.model = model
        self.spec  = spec
        self.status = status
        

    def __str__(self):
        return(f"id: {self.id}, mark: {self.mark}, model: {self.model}, spec: {self.spec}, status: {self.status}")
    
    @classmethod
    def display_all_laptops(laptops_list):
        for laptop in laptops_list:
            print(laptop)