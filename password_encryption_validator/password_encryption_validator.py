import bcrypt
from tkinter import *

class LoginRegistration:

    def __init__(self, option):
        self.option = option

    def first_step(self):
        if self.option=="registration":
            username = input("Enter username:")
            password = bytes(input("Enter password: "), encoding='utf-8')
            salt = bcrypt.gensalt()
            hashed_password = bcrypt.hashpw(password=password, salt=salt)
            # store hashed_password in database with username

        elif self.option=="login":
            username = input("Enter username:")
            password = bytes(input("Enter password:"), encoding='utf-8')
            #fetch hashed_password from database based on username
            # password = password and temp. password is hashed
            hashed_password = b'$2b$12$aA.JH9GdJyvqlOJZG57m1uNh1kVRbxIbDnuBGb/MLzg9seTX4DIQu'
            if bcrypt.checkpw(password, hashed_password):
                print("Login Successfully!!!")
            else:
                print("Login Unsuccessfully, please try again")

option = input("Please enter you choice:")
login_register=LoginRegistration(option)
login_register.first_step()