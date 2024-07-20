from customer import Customer
from reservation import Reservation
from menu_item import MenuItem
from order import Order
from table import Table


class Restaurant:
    def __init__(self):
        self.tables = []
        self.customers = []
        self.menu = []
        self.reservations = []

    def add_table(self, table):
        self.tables.append(table)

    def add_customer(self, customer):
        self.customers.append(customer)

    def add_menu_item(self, menu_item):
        self.menu.append(menu_item)

    def find_table(self, table_number):
        for table in self.tables:
            if table.table_number == table_number:
                return table
        return None

    def find_customer(self, name):
        for customer in self.customers:
            if customer.name == name:
                return customer
        return None

    def make_reservation(self, customer_name, table_number, date, time):
        customer = self.find_customer(customer_name)
        if not customer:
            print("Customer not found.")
            return

        table = self.find_table(table_number)
        if not table or table.is_reserved:
            print("Table not available.")
            return

        reservation = Reservation(customer, table, date, time)
        self.reservations.append(reservation)
        customer.add_reservation(reservation)
        table.is_reserved = True
        print("Reservation made successfully.")

    def create_order(self, table_number):
        table = self.find_table(table_number)
        if not table or not table.is_reserved:
            print("Table not reserved.")
            return None

        return Order(table)

    def report_reservations(self):
        for reservation in self.reservations:
            print(reservation)

    def report_menu(self):
        for item in self.menu:
            print(item)

    def report_customers(self):
        for customer in self.customers:
            print(customer)
