class socialMedia :
    def __init__(self,name,subscriber):
        self.name=name
        self.subscriber=subscriber
    def display(self):
        print("Social media Name : ",self.name)
        print("Total Subscriber : ",self.subscriber)

facebook=socialMedia("Facebook",4500000)
facebook.display()