class skitto:
    def __init__(self,balance,owner):
        self.balance=balance
        self.owner=owner

    def show(self):
        print(self.balance,self.owner)


class gp:
    def __init__(self, mb, point):
        self.mb = mb
        self.point = point

    def sho(self):
        print(self.mb, self.point)


class bl:
    def __init__(self, bkashNo, bkashBal):
        self.bkashNo = bkashNo
        self.bkashBal = bkashBal

    def shw(self):
        print(self.bkashNo, self.bkashBal)

class vokta(skitto,gp,bl):
    def __init__(self,balance,owner, mb, point, bkashNo, bkashBal,Name):
        skitto.__init__(self,balance,owner)
        gp.__init__(self, mb, point)
        bl.__init__(self,bkashNo,bkashBal)
        self.Name=Name

    def show(self):
        super().show()
        super().sho()
        super().shw()
        print("Owner Name ",self.Name)

zahin=vokta("20 Taka","Mataji","1024","3333","017...","105 taka","Zahin")
zahin.show()




