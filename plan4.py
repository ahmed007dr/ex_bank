class bank :
    def __init__(self,name,age) -> None:
        
        print(f'welcome {name}')
        self.blance=0
    def deposit (self,amount):
        self.blance += amount
        print(self.blance)


c1=bank('ahmed',12)
c1.deposit(500)
c1.deposit(1000)



