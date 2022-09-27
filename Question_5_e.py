import random
#functions that simulate the toss of a fair coin
def coin_toss(): 
    possibilities_coin = ["Head", "Tale"]
    print(random.choices(possibilities_coin, weights = [5, 1]))#Add weight to head..
#functions that simulate the roll of an unbiased ‘n’ sided die
def dice_throw(n):
    possibilities_dice = []
    for i in range(1, n+1):
        possibilities_dice.append(i)
    weight_dice = possibilities_dice
    #Add weight to dice
    print(random.choices(possibilities_dice, weights= weight_dice, k = 1))
#Driver code..
side = int(input("Enter the total side of the Die: "))
print("Result of the coin Toss-->")
coin_toss()
print("\nResult of the {} sided dice throw-->".format(side))
dice_throw(side)