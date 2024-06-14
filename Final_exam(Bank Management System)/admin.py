from bank import Bank
class Admin:
    def __init__(self,name,email,password):
        self.name=name
        self.email=email
        self.password=password   


    def create_account(self,bank,admin):
        bank.create_account(user)
        bank.add_admin(admin)



    def delete_user(self,bank,account_number):
        bank.delete_user(account_number)

    def see_all_account_list(self,bank):
        bank.see_all_account_list()

    def total_available_balance(self,bank):
        bank.total_available_balance()
    def check_loan(self,bank):
        bank.check_loan()


        