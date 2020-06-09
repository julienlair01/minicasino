# coding: utf-8
import math
import random

# Wallet = 50$
# Player bets on number (0 - 49)
# Roll ball
# Compare result with bet
# if result_nb == bet_nb then wallet = wallet + bet + bet * 3
# elif result_color == bet_color then wallet = walllet + bet + bet * 0.5

def nb_color (nb):
    if nb%2 == 0:
        return 'black'
    else:
        return 'red'



wallet = 50

print ("You have ${}".format(wallet))
bet_sum = input ("How much do you bet? ")
bet_nb = input ("Which number do you bet on? ")
bet_sum = int(bet_sum)
bet_nb = int(bet_nb)

result_nb = random.randrange(2)
result_color = nb_color(result_nb)

print ("The ball stopped on: {} {}".format(result_color, result_nb))

if result_nb == bet_nb:
    wallet = wallet + 4 * bet_sum
    print('Bravo, perfect')
elif result_color == nb_color(bet_nb):
    print('Bravo, color match')
else:
    print("Perdu")

print ("You now have ${}".format(wallet))
   
