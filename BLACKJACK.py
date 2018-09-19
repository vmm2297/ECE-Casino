#ECE Casino: BLACKJACK
#Hosted by ECE Undergradute Student Council at UCSD

#Games are played in the terminal console.

#Rules taken from Bicycle Cards: https://www.bicyclecards.com/how-to-play/blackjack/

import random

def play_blackjack():
	#cards are dealt
	player_hand.append(game_deck.pop())
	dealer_hand.append(game_deck.pop())
	player_hand.append(game_deck.pop())
	dealer_hand.append(game_deck.pop())

	#hands are shown, sums are computed (first hand)
	print("Your current hand is %s.") % str(player_hand)
	player_sum = get_hand_sum(player_hand,False)
	print("Your current sum is %s.") % str(player_sum)
	print("The dealer's first card is the %s with the second card face down.") % str(dealer_hand[0])
	dealer_sum = get_hand_sum(dealer_hand,True)
	
	#checking "natural blackjack" (when either player gets 21 on first hand)
	if(player_sum==21 and dealer_sum!=21):
		print("BLACKJACK! You automatically beat the dealer who has a hand of %s.") % str(dealer_hand)
		return "CONGRATS!"
	elif(player_sum==21 and dealer_sum==21):
		print("BLACKJACK! But the dealer also has BLACKJACK with a hand of %s.") % str(dealer_hand)
		return "TIE GAME!"
	elif(player_sum!=21 and dealer_sum==21):
		print("You automatically lose to the dealer who has BLACKJACK with a hand of %s.") % str(dealer_hand)
		return "SORRY!"

	#player and dealer plays
	else:
		#player can decide to HIT or STAND as long as sum is under 21
		while (player_sum<21):
			choice = player_choice()
			
			#if player chooses to HIT
			if (choice.lower()=="hit"):
				hit_card1 = game_deck.pop()
				player_hand.append(hit_card1)
				print("You drew the %s.") % str(hit_card1)
				print("Your current hand is %s.") % str(player_hand)
				player_sum = get_hand_sum(player_hand,False)
				print("Your current sum is %s.") % str(player_sum)
				
				#if player hand is BUST (sum>21)
				if (player_sum>21):
					print("Your hand is a BUST!")
					return "YOU LOSE!"
				#if player hand is BLACKJACK (sum=21)
				elif (player_sum==21):
					print("You got BLACKJACK! Now it's the dealer's turn.")
					break
				#player continues to HIT or STAND
				else:
					print("You can continue.")

			#if player chooses to STAND
			else:
				print("Your current hand is %s.") % str(player_hand)
				print("Your current sum is %s.") % str(player_sum)
				print("Now it is the dealer's turn.")
				break

		#dealer reveals full hand and must HIT until sum is at least 17
		print("The dealer's full hand is now revealed to be %s.") % str(dealer_hand)
		print("The dealer's current sum is %s.") % str(dealer_sum)
		while (dealer_sum<17):
			hit_card2 = game_deck.pop()
			dealer_hand.append(hit_card2)
			dealer_sum = get_hand_sum(dealer_hand,True)
			print("The dealer's current hand is now %s.") % str(dealer_hand)
			print("The dealer's current sum is now %s.") % str(dealer_sum)

			#if dealer hand is BUST (sum>21)
			if (dealer_sum>21):
				print("The dealer's hand is a BUST!")
				return "YOU WIN!"
			#if dealer hand is BLACKJACK (sum=21)
			elif (dealer_sum==21):
				print("The dealer got BLACKJACK!")
				#if player also has BLACKJACk
				if (player_sum==21):
					print("Since you also have BLACKJACK, nobody wins.")
					return "TIE GAME!"
				#if player does not have BLACKJACK
				else:
					print("Since you don't have BLACKJACK, the dealer wins.")
					return "YOU LOSE!"
			#dealer continues to HIT
			else:
				print("The dealer continues to HIT.")

		#scores between the player and the dealer are compared to determine winner
		print("Now the dealer must STAND and compared hands with the player.")
		if(player_sum>dealer_sum):
			print("Your score of %s is more than the dealer's score of %s.") % (str(player_sum),str(dealer_sum))
			return "YOU WIN!"
		elif(player_sum==dealer_sum):
			print("Your score of %s is equal to the dealer's score of %s.") % (str(player_sum),str(dealer_sum))
			return "TIE GAME!"
		else:
			print("Your score of %s is less than the dealer's score of %s.") % (str(player_sum),str(dealer_sum))
			return "YOU LOSE!"

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

def get_card_value(card,dealer):
	#returns the value of the drawn card (int)
	card = card.split(' ')[0]
	if card in ('Jack','Queen','King'):
		return int(10)
	elif(card=='Ace' and (not dealer)):
		print("Your hand includes an ACE! Do you want the value to be 1 or 11?")
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
		return int(11)
	else:
		return int(card)

def get_hand_sum(hand,dealer):
	#returns the value of the hand (int)
	hand_sum = 0
	for i in hand:
		hand_sum = hand_sum + get_card_value(i,dealer)
	return hand_sum

def player_choice():
	#promt for player to HIT or STAND
	print("Do you wish to HIT or STAND?")
	choice = raw_input(">")
	while(choice.lower()!="hit" and choice.lower()!="stand"):
		print("That is not a valid option! Please choose either HIT or STAND.")
		choice = raw_input(">")
	print("You have chosen to %s.") % choice.upper()
	return choice

#initialize deck and hand variables (global)
game_deck = shuffle_deck()
player_hand = []
dealer_hand = []