# class Credential:
#     """
#     Class that generates new instances of Credential
#     """
    class Account:
        account_list = []
    def __init__(self,account_name,account_password):
       
        self.account_name = account_name
        self.account_password = account_password

    credential_list = []



    def generate_acc_password():
        '''
        Function to generate random passwords for social media accounts
        '''
        pass_length = ''.printable
        length = int(input('0123456789: '))
        auto_password = ''
        for char in range(length):
            auto_password += random.choice(pass_length)
        return auto_password


    def save_credential(self):
        
        Credential.credential_list.append(self)

    @classmethod
    def account_exists(cls,account):
       
        for account in cls.account_list:
            if account == account:
                    return True
        return False


    @classmethod
    def display_credential(cls):
        
        return cls.credential_list