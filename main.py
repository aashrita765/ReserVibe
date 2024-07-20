from restaurant import Restaurant
from table import Table
from customer import Customer
from menu_item import MenuItem

def main():
    restaurant = Restaurant()

    # Adding tables
    restaurant.add_table(Table(1, 4))
    restaurant.add_table(Table(2, 2))

    # Adding menu items
    restaurant.add_menu_item(MenuItem("Biryani", "Basmati Rice with Chicken", 300))
    restaurant.add_menu_item(MenuItem("Chicken curry", "Fresh chicken cooked", 250))

    # Adding customers
    print("Enter customer details: ")
    customer_name = input("Name: ")
    customer_contact = input("Contact info: ")
    restaurant.add_customer(Customer(customer_name, customer_contact))


    # restaurant.add_customer(Customer("Laxman", "9432156788"))

    # Making reservations
    print("\nMaking a reservation:")
    print("Available tables:")
    for table in restaurant.tables:
        print(table)
    table_number = int(input("Enter table number: "))
    date = input("Enter reservation date (YYYY-MM-DD): ")
    time = input("Enter reservation time (HH:MM): ")    
    restaurant.make_reservation(customer_name, table_number, date, time)
    # restaurant.make_reservation("Laxman", 2, "2024-06-1", "19:30")

    # Creating orders
    print("\nCreating an order:")
    print("Menu items:")
    for item in restaurant.menu:
        print(item)
    table_number = int(input("Enter table number for order: "))
    order = restaurant.create_order(table_number)
    if order:
        while True:
            item_name = input("Enter menu item name to add (or 'done' to finish): ")
            if item_name.lower() == 'done':
                break
            item_quantity = int(input("Enter quantity: "))
            menu_item = next((item for item in restaurant.menu if item.name.lower() == item_name.lower()), None)
            if menu_item:
                order.add_item(menu_item, item_quantity)
            else:
                print("Menu item not found.")
        print("\nOrder summary:")
        print(order)
        print(f"Total: Rs.{order.get_total()}")
                
    # Reporting
    print("\nReporting reservations:")
    restaurant.report_reservations()
    print("\nReporting menu items:")
    restaurant.report_menu()
    print("\nReporting customers:")
    restaurant.report_customers()

if __name__ == "__main__":
    main()
