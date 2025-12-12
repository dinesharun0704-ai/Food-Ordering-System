from login import LoginSys


class Home:

    options = {1: "Login", 2: "Register", 3: "Guest", 4: "ExitApp"}

    @staticmethod
    def init():
        print("\n===== Welcome to Food Ordering App =====\n")

        login = LoginSys()

        while True:
            for opt in Home.options:
                print(f"{opt}. {Home.options[opt]}")

            try:
                choice = int(input("\nChoose an option: "))
                login.Validateopt(Home.options[choice])
            except (ValueError, KeyError):
                print("Invalid option!")


if __name__ == "__main__":
    Home.init()
