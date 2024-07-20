class Order:
    def __init__(self, table):
        self.table = table
        self.items = []

    def add_item(self, menu_item, quantity):
        self.items.append((menu_item, quantity))

    def get_total(self):
        total = sum(item[0].price * item[1] for item in self.items)
        return total

    def __str__(self):
        order_summary = [f"{item[0].name} x {item[1]}" for item in self.items]
        return f"Order for Table {self.table.table_number}: " + ", ".join(order_summary)
