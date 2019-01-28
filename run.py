#!/usr/bin/env python3.6
from user import User
from credential import Credential
import random 

def create_user(user_name,password):
    """
    Function to create a new users
    """
    new_user= User(user_name,password)
    return new_user


def save_user():
    """
     saving the user
     """
    user.save_user()

def display_users():
    return User.display_users()

def check_existing_users(user_name):
    """
    checking if the user account exists by the user_name
    """
    return User.user_exist(user_name)
def add_credential(account_name,account_password):
    
    new_credential=Credential(account_name,account_password)
    return new_credential
def save_credential(self):

        User.credential.append(self)
def display_credential():
    
    return Credential.display_credentials()


def main():
    print(' ')
    print('Hello  Welcome to passwordLocker ')
    while True:
        print(' ')
        print("-"*10)
        print('try out this: \n ca \n li \n ex')
        short_code = input('choose any of the above: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-"*10)
            print(' ')
            print('create new account:')
            account_name = input('user_name').strip()
            account_password = input('password').strip()
            save_account(create_account(account_name,account_password))
            print(" ")
            print(f'New  account created for: {account_name} ')
        elif short_code == 'li':
            print("-"*15)
            print(' ')
            print('To login, enter your new accounts:')
            account = input('account name: ').strip()
            password = str(input('password: '))
            user_exist = user_authentication(account,password)
            if user_exists == account:
                print(" ")
                print(f'you are almost there {account}. choose an accout or create a new one.')
                print(' ')
                while True:
                    print("\n cl, dl, sl, ex")
                    short_code = input().lower()
                    if short_code=='ex':
                        print(" ")
                        print(f"late us{account}")
                        break
                    elif short_code == 'cl':
                        print("logins created below")
                        print("="*15)
                        print ("Account name facebook")
                        social_acc = input()
                        print("Account username")
                        acc_username = input()
                        while True:
                            print(' ')
                            print("-" * 15)
                            print(
                                '\n ep\n gp\n ex')
                            password_options = input('choose from the above: ').lower().strip()
                            print("-" * 15)
                            if password_options == 'ep':
                                print(" ")
                                social_account_password = input('password: ').strip()
                                break
                            elif password_options == 'gp':
                                social_account_password = generate_acc_password()
                                break
                            elif password_options == 'ex':
                                break
                            else:
                                print('invalid')
                        save_account(create_account(acc_username,account_password))
                        print ('\n')
                        print(f" {social_acc} you alresdy in")
                        print ('\n')

                    elif short_code == 'sl':
                        print("enter search facebook")
                        search_account = input()
                        if check_existing_accounts(search_account):
                            search_account = find_account(search_account)
                        print(f"{search_account.account} {search_account.account_username}")
                        print('-' * 15)
                        print(f"Account: {search_account.social_account}")
                        print(f"Username: {search_account.account_username}")
                    elif short_code == 'dl':
                        if display_all_social_accounts():
                            print("your logins below")
                        print('\n')
                        for social_accounts in display_all_social_accounts():
                                print(f"account: {accounts.social_account}, User_name: {accounts.account_username}, Password: {accounts.account_password}")
                        print('\n')
                    else:
                        print('\n')
                        print("got now logins yet")
                        print('\n')

                else:
                        print("invalid")
                        print(' ')
        else:
                        print('sorry! follow instructions above.')

    
if __name__ == '__main__':
    main()