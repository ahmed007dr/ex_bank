class bank :
    def __init__(self,name,age) -> None:
        print(f'welcome {name}')
        self.blance=0
        self.name = name
        self.age=age

    def deposit (self,amount):
        self.blance += amount
        print(self.blance)

    def withdrow(self,amout):
        if amout > self.blance:
            print('can not')
            return
        self.blance -=amout
        print(self.blance)

    def show_Details(self):
        print(f'Name {self.name}')
        print(f'age {self.age}')
        print(f'my blance {self.blance}')


c1=bank('ahmed',12)
c1.deposit(500)
c1.deposit(1000)
c1.withdrow(33)
c1.show_Details()


