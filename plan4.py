class user:
    def __init__(self,name,age) -> None:
        print(f'welcome {name}')
        self.name = name
        self.age=age


    def show_Details(self):
        print(f'Name {self.name}')
        print(f'age {self.age}')
        print(f'my blance {self.blance}')


class bank(user) :
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        self.blance=0


    def deposit (self,amount):
        self.blance += amount
        print(self.blance)

    def withdrow(self,amout):
        if amout > self.blance:
            print('can not')
            return
        self.blance -=amout
        print(self.blance)


c1=bank('ahmed',12)
c1.deposit(500)
c1.deposit(1000)
c1.withdrow(33)
c1.show_Details()


