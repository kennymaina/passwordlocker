import pyperclip
import random

class User:

    
    user_name = []
    def save_user(self):

        '''
        save_user method saves user objects into user_name
        '''

        User.user_name.append(self)
    

    def __init__(self,first_name,user_name,password,email):

    

        self.first_name = first_name
        self.user_name = user_name
        self.password = password
        self.email = email

    def save_user(self):
        """
        save_user method saves user objects into the user_names
        """
        User.user_name.append(self)


    @classmethod
    def user_exist(cls,password):
        '''
        Method that checks if a user exists from the user name.
        Args:
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_name:
            if user.password == password:
                    return True

        return False


    @classmethod
    def display_users(cls):
        '''
        method that returns the user name
        '''
        return cls.user_name