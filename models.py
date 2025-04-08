class Task:
    def __init__(self, name, status="Pending"):
        self.name = name
        self.status = status

    def to_csv(self):
        return f"{self.name},{self.status}\n"
