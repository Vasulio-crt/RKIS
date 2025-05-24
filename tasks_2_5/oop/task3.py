class BankAccount:
    __balance = 0

    def deposit(self, amout):
        if amout > 0:
            self.__balance += amout
            print("Депозит внесён усппешно.")
        else:
            print("Сумма внесения должна быть положительной.")
    
    def withdraw(self, amout):
        if amout > 0:
            if self.__balance >= amout:
                self.__balance -= amout
                print("Снятие с депозита усппешно.")
            else:
                print("Недостаточно средств на счету.")
        else:
            print("Сумма снятия должна быть положительной.")
    
    def cheak_balance(self):
        print("Ваш баланс:", self.__balance)


people = BankAccount()

people.deposit(1500)
people.cheak_balance()
people.withdraw(887)
people.cheak_balance()