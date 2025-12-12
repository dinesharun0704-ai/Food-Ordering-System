from abc import ABC, abstractmethod


class abstractitem(ABC):
    def __init__(self, name, rating=None):
        self.Name = name
        self.Rating = rating


class restaurant(abstractitem):
    def __init__(self, name, rating, location):
        super().__init__(name, rating)
        self.Location = location
        self.__FoodMenu = []

    @property
    def FoodMenu(self):
        return self.__FoodMenu

    @FoodMenu.setter
    def FoodMenu(self, items):
        for item in items:
            if not isinstance(item, FoodMenu):
                print("Invalid food menu")
                return
        self.__FoodMenu = items


class FoodMenu(abstractitem):
    def __init__(self, name):
        super().__init__(name)
        self.__FoodItems = []

    @property
    def FoodItems(self):
        return self.__FoodItems

    @FoodItems.setter
    def FoodItems(self, items):
        for item in items:
            if not isinstance(item, FoodItems):
                print("Invalid food item")
                return
        self.__FoodItems = items


class FoodItems(abstractitem):
    def __init__(self, name, rating, price, desc):
        super().__init__(name, rating)
        self.Price = price
        self.Desc = desc
