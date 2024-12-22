class ShoppingCart:
    def __init__(self, total_cost=0):
        self.__total_cost = total_cost
        self.items = []

    def get_total_cost(self):
        return self.__total_cost

    def add_item(self, item_name, price):
        if price > 0:
            self.items.append((item_name, price))
            self.__total_cost += price
            print(f"Total cost: ${self.__total_cost:.2f}")
        else:
            print("Invalid item price")

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                self.__total_cost -= item[1]
                print(f"After removing & Total cost: ${self.__total_cost:.2f}")
                return
        print("Item not found in the cart")

    def view_cart(self):
        print("Items in your cart:")

        for item in self.items:
            print(f" - {item[0]}: ${item[1]:.2f}")
        print(f"Total cost: ${self.get_total_cost():.2f}")


# Create an instance of the ShoppingCart class and test the methods
cart1 = ShoppingCart()
cart1.add_item("Phone", 3500)
cart1.add_item("Laptop", 3000)
cart1.view_cart()

cart1.remove_item("Laptop")
cart1.view_cart()
