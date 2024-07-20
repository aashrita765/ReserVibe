class Reservation:
    def __init__(self, customer, table, date, time):
        self.customer = customer
        self.table = table
        self.date = date
        self.time = time

    def __str__(self):
        return f"Reservation for {self.customer.name} on {self.date} at {self.time} for Table {self.table.table_number}"