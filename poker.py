import random
l = [ 1,2,3,4,5,6,7,8,9,10,11,12,13]
SUIT = ["♣","♥","♠","♦",]
card = [ ]
for num in range(1,14):
    for suit in SUIT:
        card.append(suit +str(num))
        #print(card[len(card)-1])
def getcard():
    c = random.choice(card)
    card.remove(c)
    return c
number1 = getcard()
number2 = getcard()
number3 = getcard()
number4 = getcard()
number5 = getcard()
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)

