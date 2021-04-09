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
a = [number1,number2,number3,number4,number5]
print(number1,number2,number3,number4,number5)

print("交換するカードを選んでください。\n")
print("交換したいカードがない場合0\n""交換するカードが1枚の場合、そのカードが上から何番目かを教えてください\n")
print("交換するカードが複数枚の場合は、数字の後にコンマをつけてください。\n")

print("例えば、1枚目と2枚目の場合は1,2のようにしてください\n")

s = input()
def changecard():
    x = getcard()
    a[s] = x
A1 = changecard()
print(A1)