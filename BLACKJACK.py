#Victor's Casino (for now, we just have Blackjack)
import random

def casino_entrance():
	#player inputs name and chooses game
	print("Welcome to the ECE Casino!")
	print("What is you name?")
	user_name = raw_input(">")
	print("Hi %s, what game do you want to play today?")%user_name.capitalize()
	user_game = raw_input(">")
	if (user_game.lower() in ["blackjack","black jack","21"]):
		print("Gotcha! One game of BLACKJACK coming right up...")
	else:
		print("Sorry! We do not have that game yet. Please come back another day.")

def shuffle_deck():
	#fresh deck of cards is shuffled
	card_values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
	card_types = ['Spades','Diamonds','Hearts','Clubs']
	deck = []
	for i in card_types:
		for j in card_values:
			deck.append(j+' of '+i)
	random.shuffle(deck)
	print("A new deck of cards has been shuffled.")
	return deck

shuffle_deck()