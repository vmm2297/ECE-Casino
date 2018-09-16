#ECE Casino: Main Entrance
#Hosted by ECE Undergradute Student Council at UCSD

#Games are played in the terminal console.

#Current Games:
#	- BLACKJACK (Victor)
#	- WAR (Chau)

#Player enters casino, inputs name, and chooses game.
print("Welcome to the ECE Casino!")
print("What is you name?")
user_name = raw_input(">")
print("Hi %s, what game do you want to play today?")%user_name.capitalize()
user_game = raw_input(">")
if user_game.lower() in ("blackjack","black jack","21"):
	print("Gotcha! One game of BLACKJACK coming right up...")
	import BLACKJACK
	BLACKJACK.play_blackjack()
else:
	print("Sorry! We do not have that game yet. Please come back another day.")