FILE_NAME = "sales_log.txt"

def display_menu():
    print("\n============================================ ")
    print("          SALES RECORD MANAGEMENT SYSTEM        ")
    print("============================================= ")
    print("1.  Add Sale Record")
    print("2.  View All Records & Summary  Statistics")
    print("3.  Clear All Sales Data")
    print("4.  Exit System")
    print("============================================= ")

def add_sale_record():
    print("\n Add Sale Record ")

    item_name = input("Item Name: ").strip()

    try:
        quantity = int(input("Quantity Sold: "))
    except ValueError:
        print("Invalid Input. Must be an Integer")
        return

    try:
        price_per_unit = float(input("Price Per Unit: "))
    except ValueError:
        print("Invalid Input. Must be a number")
        return

    total_amount = quantity * price_per_unit

    try:
        with open(FILE_NAME, "a") as file:
            file.write(
                f"{item_name}, {quantity}, {price_per_unit:.2f},"
                f"{total_amount:.2f}\n"
            )

        print("Sale record saved successfully")

    except OSError:
        print("Error.")

def main():
    while True:
        display_menu()

        try:
            choice = int(input("Select an option (1-4): "))
        except ValueError:
            print("Invalid Input")