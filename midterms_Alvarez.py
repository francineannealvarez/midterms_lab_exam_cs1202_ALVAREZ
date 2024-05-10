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
        quantity = games[game_name]['quantity']
        rental_cost = games[game_name]['rental cost']
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

#Function to rent a game 
def rent_game(username):
    pass

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
    pass

#Function to display game inventory
def display_game_inventory():
    pass

#Function to handle user's logged in menu
def logged_in_menu(username):
    pass

#Function to check user credentials
def check_credentials(username, password):
    pass

#Main function to run the program
def main():
    pass

if __name__ == "__main__":
    main()