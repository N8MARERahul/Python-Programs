import random
#functions that simulate the toss of a fair coin
def coin_toss(): 
    possibilities_coin = ["Head", "Tale"]
    print(random.choice(possibilities_coin))
#functions that simulate the roll of an unbiased ‘n’ sided die
def dice_throw(n):
    possibilities_dice = []
    for i in range(1, n+1):
        possibilities_dice.append(i)
    print(random.choice(possibilities_dice))
#Driver code..
side = int(input("Enter the total side of the Die: "))
print("Result of the coin Toss-->")
coin_toss()
print("\nResult of the {} sided dice throw-->".format(side))
dice_throw(side)