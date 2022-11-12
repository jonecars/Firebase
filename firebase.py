import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def main():
    # Setup database connection
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()

    # Call the menu function
    menu(db)

def menu(db):
    """
    List of interactions the user can choose from that will interact with the database.
    """
    choice = 1
    # Loop until they choose to quit
    while choice != 0:
        # Display Menu
        print("=== INVENTORY MANAGER ===")
        print("0: Quit")
        print("1: Add new product")
        print("2: Update stock of product")
        print("3: Add or update price of product")
        print("4: View all product names")
        print("5: View Specific information on a product")
        print("6: Delete a product")
        # Ask for choice
        choice = input("Enter option: ")
        choice = int(choice)

        # Add Product
        if choice == 1:
            product = input("Please enter the name of the product: ")
            product_price = input("Please enter the price of the product: ")
            number = False
            while number == False:
                try:
                    product_price = float(product_price)
                    number = True
                except:
                    print("Please enter a valid number.")
                    product_price = input("Please enter the price of the product: ")
            stock = input("Please enter the stock amount of the item: ")
            number = False
            while number == False:
                try:
                    stock = int(stock)
                    number = True
                except:
                    print("Please enter a valid number.")
                    stock = input("Please enter the stock of the product: ")

            db.collection("Inventory").document(product).set({"name": product, "price": product_price, "Stock": stock})
        
        # Update stock
        elif choice == 2:
            product = input("Please enter the name of product you would like to update: ")
            stock = input("Please enter the stock of the product: ")
            number = False
            while number == False:
                try:
                    stock = int(stock)
                    number = True
                except:
                    print("Please enter a valid number.")
                    stock = input("Please enter the stock of the product: ")
            db.collection("Inventory").document(product).set({"Stock": stock}, merge = True)

        # Update Price
        elif choice == 3:
            product = input("Please enter the name of product you would like to update: ")
            product_price = input("Please enter the new price of the product: ")
            number = False
            while number == False:
                try:
                    product_price = float(product_price)
                    number = True
                except:
                    print("Please enter a valid number.")
                    product_price = input("Please enter the new price of the product: ")
            db.collection("Inventory").document(product).set({"price": product_price}, merge = True)

        # Get all products
        elif choice == 4:
            print("---------------")
            documents = db.collection("Inventory").get()
            for docs in documents:
                x = docs.to_dict()
                print(x["name"])
            print("---------------")
        
        # Information on Product
        elif choice == 5:
            product = input("Please enter the name of the product you would like to view: ")
            documents = db.collection("Inventory").where("name", "==", product).get()
            print("---------------")
            for docs in documents:
                print(docs.to_dict())
            print("---------------")

        # Remove Product
        elif choice == 6:
            product = input("Please enter the name of the product you would like to remove: ")
            db.collection("Inventory").document(product).delete()
        
        # Quit
        elif choice == 0:
            print()
        
        # Continue looping menu
        else:
            choice == 10
        
main()