class Laptop:
    def __init__(self, id: int, mark: str, model: str, spec: str, status: bool):
        self.id = id
        self.mark = mark
        self.model = model
        self.spec  = spec
        self.status = status

    def change_status():
        pass

    def __str__(self):
        return(f"mark: {self.mark}, model: {self.model}, spec: {self.spec}, status: {self.status}")