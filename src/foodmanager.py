from objcreator import restaurant, FoodItems, FoodMenu


class FoodManager:
    def __init__(self):
        self.__restaurants = self.prepare_restaurants()

    @property
    def restaurants(self):
        return self.__restaurants

    def prepare_fooditems(self):
        return [
            FoodItems("Veg Biryani", 4.3, 120, "Mushroom and veggies added"),
            FoodItems("Chicken Biryani", 4.7, 200, "Served with fresh chicken"),
            FoodItems("Parotta", 4.8, 60, "Soft Malabar Parotta"),
            FoodItems("Dosa", 4.2, 50, "Fresh ghee added"),
            FoodItems("Noodles", 4.4, 100, "Fresh and tasty")
        ]

    def prepare_foodmenu(self):
        fooditems = self.prepare_fooditems()

        veg = FoodMenu("Veg")
        veg.FoodItems = [fooditems[0], fooditems[3]]

        nonveg = FoodMenu("Non-Veg")
        nonveg.FoodItems = [fooditems[1], fooditems[2]]

        chinese = FoodMenu("Chinese")
        chinese.FoodItems = [fooditems[4]]

        return [veg, nonveg, chinese]

    def prepare_restaurants(self):
        menus = self.prepare_foodmenu()

        r1 = restaurant("A2B", 4.6, "Chennai")
        r1.FoodMenu = [menus[0], menus[2]]

        r2 = restaurant("Muniyandi Vilas", 4.7, "Coimbatore")
        r2.FoodMenu = [menus[0], menus[1]]

        r3 = restaurant("AM Fastfood", 4.5, "Erode")
        r3.FoodMenu = [menus[2]]

        return [r1, r2, r3]

    def searchres(self, resname):
        for r in self.restaurants:
            if r.Name.lower() == resname.lower():
                return r
        return None
