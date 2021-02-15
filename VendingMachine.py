class VendingMachine():

    def __init__(self, items, money):
        self.items = items
        self.money = money

    def vend(self, selection, given_money):
        print(self.money)
        item = next((item for item in self.items if item["code"] == selection), None)
        if item is None:
            return f"Invalid selection! : Money in vending machine = {self.money:.2f}"

        if item["price"] > given_money:
            return "Not enough money!"

        if item["quantity"] == 0:
            return "{}: Out of stock!".format(item["name"])

        change = given_money - item["price"]
        item["quantity"] -= 1
        self.money += item["price"]
        
        if change == 0:
            return "Vending {}".format(item["name"])
        print(self.money)
        return "Vending {} with {:.2f} change.".format(item["name"], change)
