class Laptop:
    storage_type="ssd"

    def __init__(self,RAM,STORAGE):
        self.RAM=RAM
        self.STORAGE=STORAGE

    @classmethod     # it makes this function like class attribute we access with class Name also known as decorator
    def get_storage_type(self):
        print(f"storage type is {self.storage_type}")

    @staticmethod #decorder normal can't access instance & class attribute
    def get_discount(price,discount):
        final_price=price-((price*discount)/100)
        print(f"final price will be: {final_price}")

    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.STORAGE} {self.storage_type}") # can access class attribute also

l1=Laptop("16gb","256gb")
print(l1.RAM)
l1.get_discount(40000,10)