class x:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def displayX(self):
        print(self.a, self.b)

class y(x):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d

    def displayY(self):
        super().displayX()
        print(self.c, self.d)

class z(y):
    def __init__(self, a, b, c, d, e, f):
        super().__init__(a, b, c, d)
        self.e = e
        self.f = f

    def displayZ(self):
        super().displayY()
        print(self.e, self.f)

class multipleCatcher(z):
    def __init__(self, a, b, c, d, e, f, k):
        super().__init__(a, b, c, d, e, f)
        self.k = k

    def display(self):
        super().displayZ()
        print(self.k)

kid = multipleCatcher(1, 2, 3, 4, 5, 6, 7)
kid.display()

baby = multipleCatcher("Siam", "Class Seven", "Single", "s", "s", "s", "$K")
baby.display()
