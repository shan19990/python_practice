import csv

class Item:
    discount = 0.8
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        assert price >= 0, f"Price cannot be less than 0, Your input is {price}"
        assert quantity >= 0, f"Quantity cannot be less than 0, Your input is {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.discount

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            print(item)

    def __repr__(self):
        return f"Item({self.name},{self.quantity},{self.price})"


# print(Item1.calculate_total_price())
# print(Item2.calculate_total_price())
# print(Item.__dict__)
# print(Item1.__dict__)

# print(Item1.price)
# Item1.apply_discount()
# print(Item1.price)

# print(Item2.price)
# Item2.discount = 0.9
# Item2.apply_discount()
# print(Item2.price)

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

Item.instantiate_from_csv()

# for instance in Item.all:
    # print(instance.name)

# print(Item.all)