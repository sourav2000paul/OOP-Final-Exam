from admin import Admin
from bank import Bank
from user import User
bangladesh_bank=Bank('Bangladesh Bank',200000000)


def admin_menu(admin):
    while True:
        print('Wellcome Admin')

        print('1 : Create Account')
        print('2 : Delete Account')
        print('3 : View All Account List')
        print('4 : Check Available Balance of the Bank')
        print('5 : Check Total Loan Amount')
        print('6 : Exit')
        cho=int(input('Enter Your Choice :'))

        if cho==1:
            name=input('Enter User Name : ')
            email=input('Enter User Email : ')
            ad=input('Enter User Adderess : ')
            a_type=input('Enter User Account Type : ')
            pss=input('Create a strong Password')
            # admin=Admin(name,email,pss)
            user=User(name=name,email=email,address=ad,acount_type=a_type,password=pss)
            bangladesh_bank.create_account(user)
            # admin.create_account(bangladesh_bank,admin)
            print('Crated Account Successfully')
            
        elif cho==2:
            acont_nm=input('Enter Account Number : ')
            admin.delete_user(bangladesh_bank,acont_nm)
        elif cho==3:
            admin.see_all_account_list(bangladesh_bank)
        elif cho==4:
            admin.total_available_balance(bangladesh_bank)
        elif cho==5:
            admin.check_loan(bangladesh_bank)
        elif cho==6:
            break
        else:
            print('Invalid Index')




def user_menu(user):
    while True:
        print('1 : Deposit ')
        print('2 : Withdraw ')
        print('3 : Check Balance ')
        print('4 : Transation History ')
        print('5 : Take Loan')
        print('6 : Send Money')
        print('7 : Exit')
        ch=int(input('Enter Your Choice : '))
        if ch==1:
            amount=int(input('Enter deposit amount : '))
            user.deposit(amount)
        elif ch==2:
            with_amount=int(input('Enter your withdraw Amount : '))
            user.withdraw(with_amount)
        elif ch==3:
            user.check_available_balance()
        elif ch==4:
            user.check_transation_history()
        elif ch==5:
            loan_amount=int(input('Enter amount of Loan : '))

            user.take_loan(bangladesh_bank,loan_amount)
        elif ch==6:
            acc_nm=input('Enter Account Number : ')
            send_money_amount=int(input('Enter Send Money Amount : '))
            user.send_money(bangladesh_bank,acc_nm,send_money_amount)
        elif ch==7:
            break





        
        
while True:

    print('1 : Admin')
    print('2 : User')
    print('3 : Exit')
    chs=int(input('Enter choice : '))
    if chs==1:
        print('1 : Sign Up')
        print('2 : Log in')
        chi=int(input('Enter your choice : '))
        if chi==1:
            ad_name=input('Enter Your Name : ')
            ad_email=input('Enter Your Email : ')
            password=input('Create a Password : ')
            admin=Admin(ad_name,ad_email,password)
            bangladesh_bank.add_admin(admin)
            print('Sign Up Successfully')
            admin_menu(admin)
        elif chi==2:
            ad_email_login=input('Enter Your Email : ')
            password_login=input('Create a Password')
            admin_login=bangladesh_bank.find_admin(ad_email_login,password_login)
            if admin_login:
                print(f'Welcome {admin_login.name}')
                admin_menu(admin)
    elif chs==2:
        print('1 : Sign Up')
        print('2 : Log in')
        c=int(input('Enter your choice : '))
        if c==1:
            user_name=input('Enter Your Name : ')
            user_email=input('Enter Your Email : ')
            user_address=input('Enter Your Address : ')
            account_type=input('Enter Your Account Type (Savings or Current) : ')
            user_password=input('Create a Password : ')
            user=User(user_name,user_email,user_address,account_type,user_password)
            bangladesh_bank.create_account(user)
            # print('Signed Up Successfully')
            user_menu(user=user)

        elif c==2:
            account_nmb=input('Enter Your Account Number : ')
            user_pass=input('Enter Your Password : ')
            user_object=bangladesh_bank.find_user(account_nm=account_nmb,user_pass=user_pass)
            if user_object:
                print(f'Welcome {user_object.name}')
                user_menu(user=user_object)
            else:
                print('Invalid Account Number or Password !!')
            

         





     

   