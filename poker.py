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
number6 = getcard()
number7 = getcard()
number8 = getcard()
number9 = getcard()
number10 = getcard()
print(number1)
print(number2)
print(number3)
print(number4)
print(number5)

print("交換するカードを選んでください。\n")
print("交換したいカードがない場合0\n""交換するカードが1枚の場合、そのカードが上から何番目かを教えてください\n")
print("交換するカードが複数枚の場合は、数字の後にコンマをつけてください。\n")

print("例えば、1枚目と2枚目の場合は1,2のようにしてください\n")

s = input()
if s == "1":
    print(number6)
    print(number2)
    print(number3)
    print(number4)
    print(number5)
elif s == "2":
    print(number1)
    print(number6)
    print(number3)
    print(number4)
    print(number5)
elif s == "3":
    print(number1)
    print(number2)
    print(number6)
    print(number4)
    print(number5)
elif s == "4":
    print(number1)
    print(number2)
    print(number3)
    print(number6)
    print(number5)
elif s == "5":
    print(number1)
    print(number2)
    print(number3)
    print(number4)
    print(number6)
