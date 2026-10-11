#constructor
#use init

class demon():
    def __init__(self,magicName,personName):
        self.magicName=magicName
        self.personName=personName

    def display(self):
        print(self.magicName,self.personName)


vikings = demon("Valhala","Floki")
vikings.display()