class product:
    def __init__(self,p_id):
        self.p_id=p_id
        print ("product")

class category(product):
    def __init__(self, p_id,p_category,p_name,price):
        super().__init__(p_id)
        self.p_category=p_category
        self.p_name=p_name
        self.price=price
        print("category")

class order(category):
    def __init__(self, p_id, p_category, p_name, price,qyt,payment_method):
        super().__init__(p_id, p_category, p_name, price)
        self.qyt=qyt
        self.payment_method=payment_method

        print ("order")

    def amount(self):
        print("order datails:")
        print(self.p_id, self.p_category,self.p_name,self.price,self.qyt,self.payment_method,sep="  ")
        return self.qyt*self.price

O1=order(101,"electronics","headphone",2000,2,"UPI")
O2=order(102,"computer","graphic_card",15000,1,"credit card")
O3=order(103,"computer","laptop",90000,1,"credit card")

orders=[O1,O2,O3]
total_amount=0
print ("total bill amount")
for i in orders:
    total_amount+=i.amount
print("total bill amount=",total_amount)