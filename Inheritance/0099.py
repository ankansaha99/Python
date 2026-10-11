class ball:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight
    def display(self):
        print("Ball Name : ",self.name,"ball\nWeight of the ball : ",self.weight)

class miniball(ball):

    def __init__(self,name,weight,price):
        super().__init__(name,weight)
        self.price=price

    def display(self):
        super().display()
        print("Price : ",self.price,"BlockMoney")

tenis = miniball("Tenis","87 gram",799)
tenis.display()
