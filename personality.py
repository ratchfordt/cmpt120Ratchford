# personality.py
# Ex Machina?
# Trevor Ratchford
# CMPT 120

import random

def getUser():
    pass



def main():
    emotions = ["angry", "disgusted", "fearful", "happy", "sad", "surprised"]
    actions = ["reward", "punish", "threaten", "joke"]
    interactions = [[[5,"Hmm. Thanks."],[0,">:^("],[2,"Don't hurt me!"],[1,"Ha. Very funny."]],
                    [[3,"Well. Thank you."],[2,"Ow!"],[1,"You disgust me."],[0,"Not funny."]],
                    [[5,"Huh, thanks."],[0,"Hey! That hurts."],[4,"T_T"],[4,"Not in the mood for jokes..."]],
                    [[3,":)"],[5,"Hey! What was that for?"],[2,"Ah!"],[3,"ㅋㅋㅋ"]],
                    [[3,"Aw, thanks."],[1,"Sadist."],[2,":("],[4,"Haha..."]],
                    [[3,":D"],[4,"Ow..."],[2,"D:"],[4,"Heh."]]]
    current = int(random.random()*6)

    while True:
        print("available actions are: ")
        for a in actions:
            print(a,)
        print("or type q to quit\n")
        print("The robot is currently " + emotions[current] + ".")

        user = input("What would you like to do? ")
        if user == "q":
            break
        elif not user in actions:
            print("Invalid action.")
        else:
            for i in range(0,4):
                if actions[i] == user:
                    print("\'" + interactions[current][i][1] + "\'\n")
                    current = interactions[current][i][0]


main()
