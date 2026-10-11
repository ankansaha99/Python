#here we go

class root:

    print("Here is class 1")
    def __init__(self,name,region):
        self.name=name
        self.region=region

    def display(self):
        print(self.name,self.region)

class lvl1(root):
    def __init__(self, name, region,x):
        super().__init__(name,region)

        self.x=x

    def display(self):
        super().display()
        print(self.x)


c=lvl1("c","d","f")
c.display()
