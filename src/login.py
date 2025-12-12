from userdetails import User, UserData
from mainmenu import MainMenu
import sys


class LoginSys:

    def Login(self):
        while True:
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            user = UserData.UserVerify(email, password)
            if user:
                print("Login Successful\n")
                MainMenu().start()
            else:
                print("Invalid credentials")

    def Register(self):
        name = input("Enter Name: ")

        # phone validation
        while True:
            try:
                ph = int(input("Enter Phone (10 digits): "))
                if len(str(ph)) == 10:
                    break
                print("Invalid number")
            except:
                print("Invalid input")

        # email validation
        mail = input("Enter Email: ")
        while "@" not in mail:
            mail = input("Invalid Email. Try again: ")

        # password validation
        password = input("Enter Password (min 8 chars): ")
        while len(password) < 8:
            password = input("Too short. Enter again: ")

        user = User(name, ph, mail, password)
        UserData.AddDetails(user)

        print("Registration Successful\n")

    def Guest(self):
        MainMenu().start()

    def ExitApp(self):
        print("Thank you for using Food Ordering App!")
        sys.exit()

    def Validateopt(self, opt):
        getattr(self, opt)()
