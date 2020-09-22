import random
l = [ 1,2,3,4,5,6,7,8,9,10,11,12,13]
SUIT = ["♣","♥","♠","♦",]
card = [ "Joker1",]
for num in range(1,14):
    for suit in SUIT:
        card.append(suit +str(num))
        #print(card[len(card)-1])
print("プレイする人数を入力してください")
x = int(input())
def getcard():
    c = random.choice(card)
    card.remove(c)
    return c
y=54//x
z=54%x
