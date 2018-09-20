#ECE Casino: Main Entrance
#Hosted by ECE Undergradute Student Council at UCSD

#Games are played in the terminal console.

#Current Games:
#	- BLACKJACK (Victor)
#	- WAR (Chau)

#Player enters casino, inputs name, and chooses game.

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
    
    # +1 here and the -1 below to display "1,2,3" instead of "0,1,2"
    for (i, game) in enumerate(current_games):
            print("[%d] %s" % (i+1, game))

    user_game = int(raw_input("> ")) - 1

    if user_game == 0:
            print("Gotcha! One game of BLACKJACK coming right up...")
            import BLACKJACK
            print(BLACKJACK.play_blackjack())
    elif user_game == num_games-1:
    	    print("Thank you! Please come back another day.")
    else:
            print("Sorry! We do not have that game yet. Please come back another day.")
    
    print(BYE_TITLE)

if __name__ == "__main__":
    main()
