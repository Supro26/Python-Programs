import random
matrix=[["Draw","Lose","Win"],
        ["Win","Draw","Lose"],
        ["Lose","Win","Draw"]]
score=0
flag=True
x=input("--- Wanna start the GAME?(y/n) ---\n")
if(x=='y'):
    while(flag):
        choice=int(input("Enter your choice:\n'0' for stone\n'1' for paper\n'2' for scissor\n"))
        a=random.randint(-1,1)
        print(f"Its a {matrix[choice][a]}!")
        if(matrix[choice][a] == "Win"):
            score=score+1
        print("Score:",score)
        y=input("Wanna Continue?!(y/n)\n")
        if(y=='n'):
            flag=False
print("Final Score:",score)