import random

def game():
    print("You are playing a game: ")
    score = random.randint(1,99)
    
    with open("files/highscore.txt") as f:
        highscore=f.read()
        if (highscore!= ""):
            highscore=int(highscore)
        else:
            highscore = 0    

    print(f"Your score is {score}")

    if(score > highscore):
        with open("files/highscore.txt","w")as f:
            f.write(str(score))

    #return score


game()