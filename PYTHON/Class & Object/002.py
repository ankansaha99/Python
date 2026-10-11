class room :
    def __init__(self,name,id):
        self.name=name
        self.id=id

    def display(self):
        print(self.name)
        print(self.id)

r1= room(3112,5)
r1.display()