class Customer:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.reservations = []

    def __str__(self):
        return f"Customer: {self.name}, Contact: {self.contact_info}"
    
    def add_reservation(self, reservation):
        self.reservations.append(reservation)