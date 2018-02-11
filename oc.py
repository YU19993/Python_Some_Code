import sys
import timeit
import random

#compare two set of coins
def weight(a,b):
    if (a > b):
        return 0
    elif (a == b):
        return 1
    else:
        return 2

#sum the weight of coins
def sum_coins(a, b, c):
    all_coins = 0
    for i in range(c):
        all_coins = all_coins + a[b+i]
    return all_coins

def main():
	n = int(sys.argv[1])
	n = 3*(n) 
	print("Coin number: " + str(n))
	coins = []
	for i in range(n):
		coins.append(0)
	odd_coin = random.randint(0, n)
	coins[odd_coin] = 1
	print("Odd coind in: " + str(odd_coin))
	pile = n 
	head = 0
	time_call = 0	
	while True:
		time_call = time_call + 3
		pile = pile // 3
		print("Pile number: " + str(pile))
		pile_1 = sum_coins(coins, head, pile)
		pile_2 = sum_coins(coins, head+pile, pile)
		pile_3 = sum_coins(coins, head+pile*2, pile)
		if( weight(pile_1, pile_2) == 1 ):
			head = head + 2*pile
		elif( weight(pile_1,pile_3) == 1 ):
			head = head + pile
		if ( pile == 1 ):
			break;
	
	print("Odd coin in: "+str(head))
	print("Time of functional call: " + str(time_call))


start = timeit.default_timer()
main()


stop = timeit.default_timer()
print (stop - start)
