class Bank:
    def __init__(self,b_name,bank_balance):
        self.bank_name=b_name
        self.__bank_balance=bank_balance
        self.users={}
        self.admin=[]
        self.total_loan=0


    def add_admin(self,admin):
        self.admin.append(admin)

    def find_admin(self,email,password):
        for admin in self.admin:
            if admin.email==email and admin.password==password:
                return admin
        return None
    
    def find_user(self,account_nm,user_pass):
        if account_nm in self.users:
            if self.users[account_nm].password==user_pass:
                return self.users[account_nm]
            else:
                # print('----Wrong Password')
                return None
        
        return None
        

    def create_account(self,user):
        if user.account_number not in self.users:
            self.users[user.account_number]=user
            print(f'Congratulations ! Account Created Successfully')
            print(f'AccountNumber : {user.account_number},Password : {user.password}')
        else:
            print('Already Exist')
    def delete_user(self,account_number):
        if account_number in self.users:
            print(f'{self.users[account_number].name} is deleted successfully!!!')
            del self.users[account_number]
            # print(f'Account is deleted successfully')
        else:
            print('Invalid Account Number')

        
    def see_all_account_list(self):
        print(f'Name\t\tEmail\t\t\tAddress\t\tAccountNumber\t\tAccountType')
        for value in self.users.values():
            print(f'{value.name}\t\t{value.email}\t{value.address}\t\t{value.account_number}\t\t{value.account_type}')
    def total_available_balance(self):
        print(f'Total Balance is : {self.__bank_balance}')
    @property
    def total_balance(self):
        return self.__bank_balance
    @total_balance.setter
    def total_balance(self,value):
        self.__bank_balance-=value

    def check_loan(self):
        print(f'Total loan amount is : {self.total_loan}')