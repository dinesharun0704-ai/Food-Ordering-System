class Cart:
    def __init__(self, choices, items):
        self.choices = choices
        self.fooditems = items
        self.items = self.add_to_cart(items)

    def add_to_cart(self, items):
        cartdic = {}
        for ch in self.choices:
            if ch > len(items):
                print("Invalid choice")
                continue
            if ch not in cartdic:
                cartdic[ch] = 1
            else:
                cartdic[ch] += 1
        return cartdic

    def processorder(self):
        total = 0
        print("\nYour Order:")
        for index, qty in self.items.items():
            food = self.fooditems[index - 1]
            subtotal = qty * food.Price
            print(f"{food.Name}: {qty} × {food.Price} = {subtotal}")
            total += subtotal

        print(f"Total: {total}\n")
        return total

    def payment(self):
        options = {1: "Card", 2: "COD", 3: "UPI"}

        for opt in options:
            print(f"{opt}: {options[opt]}")

        method = int(input("Enter payment method: "))
        getattr(self, options[method])()

    def Card(self):
        while True:
            number = input("Enter card number (16 digits): ")
            cvv = input("Enter CVV (3 digits): ")

            if len(number) == 16 and len(cvv) == 3:
                break
            print("Invalid card details")

        print("Payment Successful! Order Placed.")

    def COD(self):
        print("Order Placed with Cash on Delivery.")

    def UPI(self):
        while True:
            upi = input("Enter UPI ID: ")
            if "@" in upi:
                break
            print("Invalid UPI ID")

        otp = input("Enter OTP (4 digits): ")
        while len(otp) != 4:
            print("Invalid OTP")
            otp = input("Enter OTP again: ")

        print("Payment Successful! Order Placed.")
