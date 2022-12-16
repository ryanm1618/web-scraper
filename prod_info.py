class prod_info:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        #Create a numerized decimal for arithmetic operations 
    
    def print(self):
        print("DESCRIPTION: " + self.name)
        print("***************************************************************************************")
        print("PRICE: "+ self.price)
        print("========================================================================================")
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price

    