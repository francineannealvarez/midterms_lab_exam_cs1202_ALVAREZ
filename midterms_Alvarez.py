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
                "balance": 0.0,
                "points": 0,
                "inventory": []
            }
            main()
            
#Function for logging in
def log_in_user():
    print("\nLog in Page")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in user_accounts and user_accounts[username]["password"]:
        print(f"Logged in successfully. Welcome {username}!")
        logged_in_menu(username)
    else:
        print("Invalid username or password.")

#Function to handle user's logged in menu
def logged_in_menu(username):
    while True:
        print("\nUsers Menu Page")
        print("1. Rent a Game")
        print("2. Return a Game")
        print("3. Top-up Account")
        print("4. Display Inventory")
        print("5. Redeem a Free Game Rental")
        print("6. Logged out")
        user_choice = input("Enter the number corresponding to your choice: ")

        if user_choice == "1":
            rent_game(username)
        elif user_choice == "2":
            return_game(username)
        elif user_choice == "3":
            top_up_account(username)
        elif user_choice == "4":
            display_inventory()
        elif user_choice == "5":
            redeem_free_rental(username)
        elif user_choice == "6":
            print(f"Logged out as {username} successfully.")
            main()


#Function to rent a game 
def rent_game(username, free=False):
    display_available_games()
    try:
        game_choice = int(input("Enter the number corresponding to the game you want to rent: "))
        if game_choice in game_library:
            game_name = list(game_library[game_choice].keys())[0]
            game_info = game_library[game_choice][game_name]
            balance = user_accounts[username]["balance"]
            if game_info["quantity"] > 0:
                rental_cost = 0 if free else game_info["rental_cost"]
                if balance >= rental_cost:
                    game_info["quantity"] -= 1
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
    except ValueError as e: 
        print(f"Error occured: {e}.")
                        
#Function to return a game
def return_game(username):
    pass

#Function to top_up user account
def top_up_account(username):
    pass

#Function to display user's inventory
def display_inventory(username):
    pass

#Function for admin to update game details
def admin_update_game(username):
    while True:
        print("\nAdmin Update Game Details Page")
        print("1. Update Quantity of Games")
        print("2. Update Rental Cost of Games")
        print("3. Back to admin menu")
        admin_choice = input("Enter the number corresponding to your choice: ")
        
        if admin_choice == "1":
            update_games_quantity()
        elif admin_choice == "2":
            update_games_rental_cost()
        elif admin_choice == "3":
            admin_menu()
        else:
            print("..")

#Function for updating quantity of games
def update_games_quantity():
    pass

#Function for updating rental costs of games
def update_games_rental_cost():
    pass

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
        
        if admin_choice == "1":
            admin_update_game()
        elif admin_choice == "2":
            print("Logged out successfully.")
        else:
            print("Invalid choice.")


#Function for users to redeem points for a free game rental
def redeem_free_rental(username):
    rental_points = user_accounts[username]["points"]
    if rental_points >= 3:
        user_accounts[username]["points"] -= 3
        rent_game(username)
    else:
        print("\nYou do not have enough points. Need at least 3 points to redeem.")


#Function to display game inventory
def display_game_inventory():
    pass


#Function to check user credentials
def check_credentials(username, password):
    pass

#Main function to run the program
def main():
    pass

if __name__ == "__main__":
    main()