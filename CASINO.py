#ECE Casino: Main Entrance
#Hosted by ECE Undergradute Student Council at UCSD

#Games are played in the terminal console.

#Current Games:
#	- BLACKJACK (Victor)
#	- WAR (Chau)

#Player enters casino, inputs name, and chooses game.

#Initial variables
CASINO_TITLE = """
______ _____ ______    _____           _____ _____ _   _  ____  
|  ____/ ____|  ____|  / ____|   /\    / ____|_   _| \ | |/ __ \ 
| |__ | |    | |__    | |       /  \  | (___   | | |  \| | |  | |
|  __|| |    |  __|   | |      / /\ \  \___ \  | | | . ` | |  | |
| |___| |____| |____  | |____ / ____ \ ____) |_| |_| |\  | |__| |
|______\_____|______|  \_____/_/    \_\_____/|_____|_| \_|\____/ 

"""
BYE_TITLE = """
______     ________              ______     ________ 
|  _ \ \   / /  ____|            |  _ \ \   / /  ____|
| |_) \ \_/ /| |__      ______   | |_) \ \_/ /| |__   
|  _ < \   / |  __|    |______|  |  _ < \   / |  __|  
| |_) | | |  | |____             | |_) | | |  | |____ 
|____/  |_|  |______|            |____/  |_|  |______|

"""
current_games = ["BLACKJACK", "WAR (in progress)", "EXIT CASINO (closes game)"]
num_games = len(current_games)

def main():

    print(CASINO_TITLE)

    print("Welcome to the ECE Casino!")

    print("What is you name?")

    # Keep going until we get their name
    got_name = False
    while (not got_name):
            try:
                    user_name = raw_input("> ")
                    if (len(user_name) == 0):
                            raise Exception()
                    else:
                    	    got_name = True
            except:
                    print("Please provide your name!")

    print("Hi %s, what game do you want to play today?" % user_name.capitalize())
    
    print("Our current selection of games include:")
    
    # Game options printed and indexed starting at 1 (with the 'start' parameter)
    for (i, game) in enumerate(current_games,start=1):
            print("[%d] %s" % (i, game))

    # Checking valid choice and starting up chosen game (or EXIT)
    invalid_choice = True
    while (invalid_choice):
    	    user_game = raw_input("> ")
            if user_game == "1":
                    print("Gotcha! One game of BLACKJACK coming right up...")
                    invalid_choice = False
                    import BLACKJACK
                    print(BLACKJACK.play_blackjack())
            elif user_game == str(num_games):
    	            print("Thank you! Please come back another day.")
    	            invalid_choice = False
            else:
                    print("That is an invalid option! Please choose a valid option.")
    
    print(BYE_TITLE)

if __name__ == "__main__":
    main()
