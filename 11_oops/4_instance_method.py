class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,STORAGE):
        self.RAM=RAM
        self.STORAGE=STORAGE

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.STORAGE} {self.storage_type}") # can access class attribute also

l1=Laptop(256,512)

l1.get_info()