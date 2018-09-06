#Victor's Casino (for now, we just have Blackjack)

def casino_entrance():
	print("Hi! Welcome to Victor's Casino.")
	print("What is you name?")
	user_name = raw_input(">")
	print("Hi %s, what game do you want to play today?")%user_name.capitalize()
	user_game = raw_input(">")
	if (user_game.lower() in ["blackjack","black jack","21"]):
		print("Okay! One game of BLACKJACK coming right up...")
	else:
		print("Sorry! We do not have that game yet. Come back another day.")

def shuffle_deck():
	print("Deck is shuffled!")

casino_entrance()