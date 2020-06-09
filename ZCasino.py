# coding: utf-8
import random
import math

wallet = 100
continue_game = True

print ("Welcome to the ZCasino !\nYou have ${}".format(wallet))

while continue_game:
    bet_nb = -1
    while bet_nb < 0 or bet_nb > 49:
        bet_nb = input ("Which number do you bet on (0-49)? ")
        try:
            bet_nb = int(bet_nb)
        except ValueError:
            print("Please enter a number.")
            bet_nb = -1
            continue
        if bet_nb < 0:
            print("This is a negative number.")
        if bet_nb > 49:
            print("This number is too high.")

    bet_sum = 0
    while bet_sum <= 0 or bet_sum > wallet:
        print ("You have ${}".format(wallet))
        bet_sum = input ("How much do you bet? ")
        try:
            bet_sum = int(bet_sum)
        except ValueError:
            print("Please enter a number.")
            bet_sum = 0
            continue
        if bet_sum > wallet:
            print("Your bet is higher than the money in your wallet.")
        if bet_sum <= 0:
            print("Please enter a positive bet.")
        

    result_nb = random.randrange(2)
    print("The ball stopped on", result_nb, ".")

    if result_nb == bet_nb:
        wallet += 3 * bet_sum
        print("Congratulations, perfect match. You just won", 3 * bet_sum, "$!")
    elif result_nb % 2 == bet_nb % 2:
        wallet += math.ceil(0.5 * bet_sum)
        print("Not bad, color match. You just won", math.ceil(0.5 * bet_sum), "$!")
    else:
        wallet -= bet_sum
        print("Sorry, you lost", bet_sum, "$.")

    if wallet <= 0:
        continue_game = False
    
    print ("You now have ${}".format(wallet))
    