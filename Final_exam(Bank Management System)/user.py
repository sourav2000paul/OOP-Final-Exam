import random    
def unique_id(name,email):
    id=''
    # id+=(for ch in random.sample(name,2)) 
    # id+=str(ch for ch in random.sample(name,2))
    for ch in random.sample(name,4):
        id+=ch
    for ch in random.sample(email,4):
        id+=ch
    return id

class User:
    
    def __init__(self,name,email,address,acount_type,password):
        self.name=name
        self.email=email
        self.address=address
        self.account_number=unique_id(name,email)
        self.history=''
        self.account_type=acount_type
        self.loan=0
        self.password=password
        self.__balance=0

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f'{amount} Taka is Deposited Successfully')
            self.history+=f'Deposit---- {amount} taka\n'
        else:
            print('Invalid Amount')
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
            print(f'{amount} taka is withdrawn successfully!!')
            self.history+=f'Withdrawn---- {amount} taka\n'

        else:
            print('Withdrawal amount exceeded')
    def check_available_balance(self):
        print(f'{self.__balance}')
    
    def check_transation_history(self):
        print(self.history)
    
    def take_loan(self,bank,amount):
        if self.loan<2:
            self.__balance+=amount
            self.loan+=1
            self.history+=f'Took loan ----- {amount} taka\n'
            bank.total_loan+=amount
            bank.total_balance=amount
        else:
            print('Already taken loan maximum 2 times ')
            

    def send_money(self,bank,accont_number,amount):
        if accont_number in bank.users:
            if self.account_number!=accont_number:
                if self.__balance>=amount:
                    bank.users[accont_number].__balance+=amount
                    self.__balance-=amount
                    print(f'{amount} is sent Successfully')
                    self.history+=f'Send Money ---- {amount}\n'
                    bank.users[accont_number].history+=f'Recieved Money----{amount}\n'
                else:
                    print('Insufucent Balance')
            else:
                print("You can't send money to your own account")
        else:
            print('Account does not exist')


