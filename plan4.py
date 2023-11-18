class bank :
    def __init__(self,name,age) -> None:
        
        print(f'welcome {name}')
        self.blance=0
    def deposit (self,amount):
        self.blance += amount
        print(self.blance)

    def withdrow(self,amout):
        if amout < self.blance:
            self.blance -=amout
            print(self.blance)
        else:
            print('can not')



c1=bank('ahmed',12)
c1.deposit(500)
c1.deposit(1000)
c1.withdrow(1600)



