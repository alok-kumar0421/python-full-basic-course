class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,STORAGE):
        self.RAM=RAM
        self.STORAGE=STORAGE

    @classmethod     # it makes this function like class attribute we access with class Name also known as decorator
    def get_storage_type(self):
        print(f"storage type is {self.storage_type}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.STORAGE} {self.storage_type}") # can access class attribute also

l1=Laptop(256,512)

l1.get_info()

Laptop.get_storage_type()