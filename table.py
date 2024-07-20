class Table:
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.is_reserved = False

    def __str__(self):
        status = "Available" if not self.is_reserved else "Reserved"
        return f"Table {self.table_number} (Capacity: {self.capacity}) - {status}"
