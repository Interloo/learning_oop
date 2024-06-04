from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'

class Account:
    def __init__(self, name, balance):
        # pass
        self.name = name
        self.__balance = balance
        self._history = []

    @staticmethod
    def _get_local_time():
        return pytz.utc.localize(datetime.now())

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount,self._get_local_time()])

    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} units')
            self.show_balance()
            self._history.append([-amount,self._get_local_time()])
        else:
            print('Not money')
            self.show_balance()

    def show_balance(self):
        print(f'Balance: {self.__balance}')

    def show_history(self):
        for amount, data  in self._history:
            if amount > 0:
                transation = "deposited"
                color = GREEN
            else:
                transation = "withdrawn"
                color = RED

            print(f"{color} {amount} {WHITE} {transation} {data.astimezone()}")


# class Person:
#     __name = "Ivan"

# p = Person()

# p.__name

a = Account("Roman", 0) 
print(a.name)

 
a.deposit(100)

a.show_balance()
a.show_history()

#!!!
a.__balance = 10000  

print(a.__dict__)
a.show_balance()