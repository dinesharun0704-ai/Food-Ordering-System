from foodmanager import FoodManager
from cart import Cart


class MainMenu:

    options = {1: "ShowRestaurants", 2: "ShowFoodItems", 3: "SearchRestaurants"}

    def __init__(self):
        self.__foodmanager = FoodManager()

    def ShowRestaurants(self):
        for i, res in enumerate(self.__foodmanager.restaurants, 1):
            print(f"{i}. {res.Name} - Rating: {res.Rating}")

        choice = int(input("\nSelect Restaurant Number: "))
        restaurant = self.__foodmanager.restaurants[choice - 1]
        self.ShowFoodMenu(restaurant)

    def ShowFoodItems(self, menu=None):
        if menu is None:
            items = set()
            for res in self.__foodmanager.restaurants:
                for menu in res.FoodMenu:
                    for item in menu.FoodItems:
                        items.add(item.Name)

            for i, item in enumerate(items, 1):
                print(f"{i}. {item}")

            print("\nSelect a restaurant to order:")
            return self.ShowRestaurants()

        else:
            items = menu.FoodItems
            for i, item in enumerate(items, 1):
                print(f"{i}. {item.Name} - ₹{item.Price}")

            choices = list(map(int, input("Enter item numbers (1,2,3): ").split(",")))
            cart = Cart(choices, items)
            cart.processorder()
            cart.payment()

    def SearchRestaurants(self):
        name = input("Enter restaurant name: ")
        res = self.__foodmanager.searchres(name)

        if res:
            print("Restaurant found.")
            self.ShowFoodMenu(res)
        else:
            print("Not found!")
            self.ShowRestaurants()

    def ShowFoodMenu(self, res):
        print(f"\nMenu - {res.Name}")
        for i, cat in enumerate(res.FoodMenu, 1):
            print(f"{i}. {cat.Name}")

        choice = int(input("\nSelect a Category: "))
        self.ShowFoodItems(res.FoodMenu[choice - 1])

    def start(self):
        while True:
            for opt in MainMenu.options:
                print(f"{opt}: {MainMenu.options[opt]}")

            try:
                op = int(input("\nChoose Option: "))
                getattr(self, MainMenu.options[op])()
            except (ValueError, KeyError):
                print("Invalid option!")
