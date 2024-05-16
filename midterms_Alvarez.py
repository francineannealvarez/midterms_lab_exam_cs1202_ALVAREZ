#dictionary to store game library with their quantities and rental costs
#used numbers to lessen errors in typing names of games
game_library = {
        1: {"Donkey Kong": {"quantity": 3, "rental cost": 2}},
        2: {"Super Mario Bros": {"quantity": 5, "rental cost": 3}},
        3: {"Tetris": {"quantity": 2, "rental cost": 1}}
        }

#dictionary to store user accounts with their balance and points
user_accounts = {}

#Admin account details
admin_username = "admin"
admin_password = "adminpass"

#Function to display available games with their numbers and rental costs
def display_available_games():
    print("\nAVAILABLE GAMES:")
    for index, games in game_library.items():
        game_name = list(games.keys())[0]
        quantity = games[game_name]["quantity"]
        rental_cost = games[game_name]["rental cost"]
        print(f"{index}. {game_name} - Quantity: {quantity}, Rental Cost: {rental_cost}")
        
#Function to register a new user
def register_user():
    print("\nRegister Page ")
    username = input("Enter username: ")
    if username in user_accounts:
        print(f"{username} already exists. Please enter another username.")
    else:
        password = input("Enter password (password must be 8 characters long): ")
        if len(password) < 8:
            print("Password must be 8 characters long.")
        else:
            print("Registered successfully.")
            user_accounts[username] = {
                "username": username,
                "password": password,
                "balance": 0.0, #float
                "points": 0, #int
                "inventory": [] 
            }
            main()
            
#Function for logging in
def log_in_user():
    print("\nLog in Page")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in user_accounts and user_accounts[username]["password"] == password:
        print(f"Logged in successfully. Welcome {username}!")
        logged_in_menu(username)
    else:
        print("Invalid username or password.")

#Function to handle user's logged in menu
def logged_in_menu(username):
    while True:
        print("\nUsers Menu Page")
        print(f"Logged in as {username}.")
        print("1. Rent a Game")
        print("2. Return a Game")
        print("3. Top-up Account")
        print("4. Display Inventory")
        print("5. Redeem a Free Game Rental")
        print("6. Logged out")
        user_choice = input("Enter the number corresponding to your choice: ")
        try:
            if user_choice == "1":
                rent_game(username)
            elif user_choice == "2":
                return_game(username)
            elif user_choice == "3":
                top_up_account(username)
            elif user_choice == "4":
                display_inventory(username)
            elif user_choice == "5":
                redeem_free_game_rental(username)
            elif user_choice == "6":
                print(f"Logged out as {username} successfully.")
                main()
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error occured: {e}.")

#Function to rent a game 
def rent_game(username, free=False):
    display_available_games()
    try:
        game_choice = input("Enter the number corresponding to the game you want to rent: ")
        if not game_choice.strip():  # Check if input is blank
            print("Canceled.")
            logged_in_menu(username)
            return
        game_choice = int(game_choice)
        if game_choice in game_library:
            game_name = list(game_library[game_choice].keys())[0]
            game_quantity_cost = game_library[game_choice][game_name]
            balance = user_accounts[username]["balance"]
            if game_quantity_cost["quantity"] > 0:
                rental_cost = 0 if free else game_quantity_cost["rental cost"]
                if balance >= rental_cost:
                    game_quantity_cost["quantity"] -= 1
                    user_accounts[username]["balance"] -= rental_cost
                    balance = user_accounts[username]["balance"]
                    print(f"{game_name} rented successfully.")
                    user_accounts[username]["inventory"].append(game_name)
                    print(f"Your current balance is ${balance}.")

                    if not free:
                        if int(rental_cost) >= 2:
                            user_accounts[username]["points"] += 1
                            print("You have earned 1 point.")
                            logged_in_menu(username)
                        else:
                            print("No added points. Need to spend at least $2 to gain 1 point.")
                            logged_in_menu(username)
                else:
                    print(f"You do not have enough balance tp rent {game_name}.")
            else: 
                print("Sorry, no copies available.")
        else:
            print("Your choice isn't included in the provided selection.")
    except ValueError:
        print("Error occured. Note that only numbers will be accepted.")
    except Exception as e:
        print(f"Error occured: {e}.")
                        
#Function to return a game
def return_game(username):
    inventory = user_accounts[username].get("inventory", [])
    print("\nRented Games:")
    for index, game_name in enumerate(inventory, 1):
        print(f"{index}. {game_name}")
    
    try:
        game_choice = input("Enter the number corresponding to the game you want to return: ")
        if not game_choice.strip():  # Check if input is blank
            print("Canceled.")
            logged_in_menu(username)
            return
        game_choice = int(game_choice)
        if 1 <= game_choice <= len(inventory):
            game_name = inventory[game_choice - 1]
            for game_info in game_library.items():
                if game_name in game_info:
                    game_info[game_name]["quantity"] += 1
                    break
            
            inventory.remove(game_name)
            print(f"{game_name} has been returned successfully.")
            logged_in_menu(username)
        else:
            print("Your choice isn't included in your inventory.")
    except ValueError:
        print("Error occured. Note that only numbers will be accepted.")
    except Exception as e:
        print(f"Error occured: {e}.")

#Function to top_up user account
def top_up_account(username):
    try:
        print("\n")
        amount = input("Enter the desired top-up amount: ")
        if not amount.strip():  # Check if input is blank
            print("Canceled.")
            logged_in_menu(username)
            return
        amount = float(amount)
        if amount > 0:
            user_accounts[username]["balance"] += amount
            balance = user_accounts[username]["balance"]
            print(f"Successfully topped up. Your new balance is ${balance}.")
            logged_in_menu(username)
        else:
            print("Amount must be greater than 0.")
    except ValueError:
        print("Error occured. Note that only numbers will be accepted.")

#function to display user's inventory
def display_inventory(username):
    inventory = user_accounts[username].get('inventory', [])
    print("\nYOUR INVENTORY")
    if inventory:
        for index, game_name in enumerate(inventory, 1):
            print(f"{index}. {game_name}")
    else:
        print("There are currently no games rented under your account.")

    balance = user_accounts[username]['balance']
    print(f"Account Balance: ${balance}")
    logged_in_menu(username)

#Function for users to redeem points for a free game rental
def redeem_free_game_rental(username):
    rental_points = user_accounts[username]["points"]
    if rental_points >= 3:
        user_accounts[username]["points"] -= 3
        print("\nRedeemed points. You now have 1 free game rental! 3 points deducted.")
        rent_game(username, free=True) 
        logged_in_menu(username)
    else:
        print("\nYou do not have enough points. Need at least 3 points to redeem.")

#Function for admin log in
def admin_login():
    print("\nAdmin Login Page")
    admin_usn = input("Enter username: ")
    admin_pass = input("Enter password: ")
    if admin_usn == admin_username and admin_pass == admin_password:
        print("Logged in successfully.")
        admin_menu()
    else:
        print("Invalid username or password.")

#Function for admin menu
def admin_menu():
    while True:
        print("\nAdmin Menu")
        print("1. Update game details")
        print("2. Logged out")
        admin_choice = input("Enter the number corresponding to your choice: ")
        try: 
            if admin_choice == "1":
                admin_update_game()
            elif admin_choice == "2":
                print("Logged out successfully.")
                main()
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error occured: {e}.")

#Function for admin to update game details
def admin_update_game():
    while True:
        print("\nAdmin Update Game Details Page")
        print("1. Update Quantity of Games")
        print("2. Update Rental Cost of Games")
        print("3. Back to admin menu")
        admin_choice = input("Enter the number corresponding to your choice: ")
        try:
            if admin_choice == "1":
                update_games_quantity()
            elif admin_choice == "2":
                update_games_rental_cost()
            elif admin_choice == "3":
                admin_menu()
            else:
                print("Your choice isn't included in the provided selection.")
        except Exception as e:
            print(f"Error occured: {e}.")

#Function for updating quantity of games
def update_games_quantity():
    print("\n")
    display_available_games()
    try:
        game_choice = input("Enter the number corresponding to the game you want to update: ")
        if not game_choice.strip():  # Check if input is blank
            print("Canceled.")
            admin_update_game()
            return
        game_choice = int(game_choice)
        if game_choice in game_library:
            game_name = list(game_library[game_choice].keys())[0]
            quantity = int(input(f"Input the updated quantity for {game_name}: "))
            game_library[game_choice][game_name]["quantity"] = quantity
            print(f"Quantity updated for {game_name}: {quantity}")
            admin_update_game()
        else:
            print("Invalid choice.")
    except ValueError as e:
        print(f"Error occured: {e}")

#Function for updating rental costs of games
def update_games_rental_cost():
    print("\n")
    display_available_games()
    try:
        game_choice = input("Enter the number corresponding to the game you want to update: ")
        if not game_choice.strip():  # Check if input is blank
            print("Canceled.")
            admin_update_game()
            return
        game_choice = int(game_choice)
        if game_choice in game_library:
            game_name = list(game_library[game_choice].keys())[0]
            rental_cost = float(input(f"Input the updated rental cost for {game_name}: "))
            game_library[game_choice][game_name]["rental cost"] = rental_cost
            print(f"Rental cost updated for {game_name}: {rental_cost}")
            admin_update_game()
        else:
           print("Invalid choice.")
    except ValueError as e:
        print(f"Error occured: {e}")

#Main function to run the program
def main():
    while True: 
        print("\nWelcome to Video Game Rental System!")
        print("1. Display Available Games")
        print("2. Register User")
        print("3. Log in")
        print("4. Admin log in")
        print("5. Exit")
        
        choice = input("Enter the number corresponding to your choice: ")
        try:
            if choice == "1":
                display_available_games()
            elif choice == "2":
                register_user()
            elif choice == "3":
                log_in_user()
            elif choice == "4":
                admin_login()
            elif choice == "5":
                print("Thank you for using this system!")
                break
            else:
                print("Your choice isn't included in the provided selection.")
        except Exception as e:
            print(f"Error occured: {e}.")

if __name__ == "__main__":
    main()