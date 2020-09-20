import random 
a = ["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と"
,"な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ","ま","み","む","め","も","ら","り","る","れ","ろ","や","ゆ","よ","わ"
,"ん"]
word = random.choices(a,k=random.randint(1,5))
use = input()
if use[-1] == "ん":
    print("ゲームオーバー")
else:
    print(use[-1] + ''.join(word)[-1])
    while ''.join(word)[-1] != "ん":
        user = input()
        if user[-1] == "ん" or ''.join(word)[-1] != user[0]:
            break
        print(user[-1] + ''.join(word))  
    print("ゲームオーバー")