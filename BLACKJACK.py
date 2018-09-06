#Victor's Casino (for now, we just have Blackjack)
import random

def enter_casino():
	#lets player input name and choose game
	print("Welcome to the ECE Casino!")
	print("What is you name?")
	user_name = raw_input(">")
	print("Hi %s, what game do you want to play today?")%user_name.capitalize()
	user_game = raw_input(">")
	if user_game.lower() in ("blackjack","black jack","21"):
		print("Gotcha! One game of BLACKJACK coming right up...")
	else:
		print("Sorry! We do not have that game yet. Please come back another day.")

def shuffle_deck():
	#returns a freshly shuffled deck of cards (list)
	card_values = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
	card_types = ['Spades','Diamonds','Hearts','Clubs']
	deck = []
	for i in card_types:
		for j in card_values:
			deck.append(j+' of '+i)
	random.shuffle(deck)
	print("A new deck of cards has been shuffled.")
	return deck

def get_value(card):
	#returns the value of the drawn card (int)
	card = card.split(' ')[0]
	if card in ('Jack','Queen','King'):
		return int(10)
	elif card == 'Ace':
		print("You drew an ACE! Do you want the value to be 1 or 11?")
		choice = raw_input(">")
		while(True):
			if choice == '1':
				return int(1)
			elif choice == '11':
				return int(11)
			else:
				print("That is not a valid option! Please choose either 1 or 11.")
				choice = raw_input(">")
	else:
		return int(card)

#start of debugging code
deck = shuffle_deck()
print get_value(deck.pop())