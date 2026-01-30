class Product:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        Product.count +=1

    def get_info(self):
        print(f"price of {self.name} is rs.{self.price}")

    @classmethod
    def product_count(cls):
        print(f"total manufactured product is {cls.count}")
    
    @staticmethod
    def cal_disc(price,disc):
        final_price=price-(disc*price/100)
        print(f"discounted price will be {final_price}")

l1=Product("phone",10_000)
l2=Product("laptop",50000)

l1.get_info()
Product.product_count()

l1.cal_disc(1000,10)