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
		play_blackjack()
	else:
		print("Sorry! We do not have that game yet. Please come back another day.")

#main function to play blackjack
def play_blackjack():	
	#cards are dealt
	deck = shuffle_deck()
	player_hand = []
	dealer_hand = []
	player_hand.append(deck.pop())
	dealer_hand.append(deck.pop())
	player_hand.append(deck.pop())
	dealer_hand.append(deck.pop())

	#hands are shown, sums are computed
	print("Your current hand is %s.") % str(player_hand)
	player_sum = get_hand_sum(player_hand)
	print("Your current sum is %s.") % str(player_sum)
	print("The dealer's first card is the %s with the second card face down.") % str(dealer_hand[0])
	dealer_sum = get_hand_sum(dealer_hand)
	
	#checking "natural blackjack"
	if(player_sum==21 and dealer_sum!=21):
		print("BLACKJACK! You automatically beat the dealer who has a hand of %s.") % str(dealer_hand)
		print("Congratulations!")
	elif(player_sum==21 and dealer_sum==21):
		print("BLACKJACK! But the dealer also has BLACKJACK with a hand of %s.") % str(dealer_hand)
		print("TIE GAME!")
	elif(player_sum!=21 and dealer_sum==21):
		print("You automatically lose to the dealer who has BLACKJACK with a hand of %s.") % str(dealer_hand)
		print("SORRY!")

	#player choice to HIT or STAND
	else:
		print("Do you wish to HIT or STAND?")
		player_choice = ""
		while(player_choice.lower()!="hit" and player_choice.lower()!="stand"):
			player_choice = raw_input(">")
			if(player_choice.lower()!="hit" and player_choice.lower()!="stand"):
				print("That is not a valid option! Please choose either HIT or STAND.")
				player_choice = raw_input(">")
		print(player_choice)
	#player HIT
	#player STAND

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

def get_card_value(card,dealer=False):
	#returns the value of the drawn card (int)
	card = card.split(' ')[0]
	if card in ('Jack','Queen','King'):
		return int(10)
	elif(card=='Ace' and not dealer):
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
	elif(card=='Ace' and dealer):
		#better logic for choosing dealer ACE value!!!
		return int(1)
	else:
		return int(card)

def get_hand_sum(hand):
	hand_sum = 0
	for i in hand:
		hand_sum = hand_sum + get_card_value(i)
	return hand_sum

#player enters the casino
enter_casino()