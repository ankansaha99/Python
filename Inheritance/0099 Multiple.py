class x:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def displayX(self):
        print(self.a,self.b)

class y:
    def __init__(self,c,d):
        self.c=c
        self.d=d

    def displayY(self):
        print(self.c,self.d)

class z:
    def __init__(self, e, f):
        self.e = e
        self.f = f

    def displayZ(self):
        print(self.e, self.f)

class multipleCatcher (x,y,z):
    def __init__(self,a,b,c,d,e,f):
        x.__init__(self,a,b)
        y.__init__(self,c,d)
        z.__init__(self,e,f)
    def display(self):
        super().displayX()
        super().displayY()
        super().displayZ()

kid = multipleCatcher(1,2,3,4,5,6)
kid.display()

baby= multipleCatcher("Siam","Class Seven","Single","s","s","s")
baby.display()