import unittest
from user import User


class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("kenny","kenny","12345ke","kenny@moringaschool.com")

    

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"kenny")
        self.assertEqual(self.new_user.user_name,"kenny")
        self.assertEqual(self.new_user.password,"0123456789")
        self.assertEqual(self.new_user.email,"kenny@moringaschool.com")

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_name),3)



    def save_user(self):

        '''
        save_user method saves user objects into user_name
        '''

        User.user_name.append(self)


    def test_save_multiple_user(self):
            '''
            test_save_multiple_users to check if we can save multiple user
            objects to our user_name
            '''
            self.new_user.save_user()
            test_user = User("kenny","kenny","12345ke","kenny@moringaschool.com")
            test_user.save_user()
            self.assertEqual(len(User.user_name),2)


    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the user.
        '''

        self.new_user.save_user()
        test_user = User("vickie","vickie","12345ke","vickie@moringaschool.com")
        test_user.save_user()

        user_exists = User.user_exist("12345ke")

        self.assertTrue(user_exists)


    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''

        self.assertEqual(User.display_users(),User.user_name)



# if __name__ == '__main__':
#     unittest.main()