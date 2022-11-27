import random
winning_num= random.randint(1,6)
guess=1
num=int(input("enter a number b/w 1 to 6:"))
game_over=False
while not game_over :
    if num==winning_num:
     print(f"you win and your guess {guess} times")
     game_over=True
    else:
     if num<winning_num:
         print("too low")
     else:
         print("too high")
     guess+=1
     num=int(input("guess again:"))