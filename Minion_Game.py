''' Hackerrank Problem called Minion Game found here https://www.hackerrank.com/challenges/the-minion-game/problem '''

vowel_list=["A","E","I","O","U"]

#point_staurt=dict()
#point_kevin=dict()


def minion_game(string):

    staurt_score=0
    kevin_score=0

    x=len(string)
    for i in range(x):
        if string[i] in vowel_list:
            for j in range(i+1,x+1):
                kevin_score=kevin_score+1
                #point_kevin[string[i:j]]=point_kevin.get(string[i:j],0)+1

    for i in range(x):
        if string[i] not in vowel_list:
            for j in range(i+1,x+1):
                staurt_score=staurt_score+1
                #point_staurt[string[i:j]]=point_staurt.get(string[i:j],0)+1

    if staurt_score>kevin_score:
        print("Stuart "+str(staurt_score))
    elif kevin_score>staurt_score:
        print("Kevin "+str(kevin_score))
    else:
        print("Draw")


def minion_game2(string):
    staurt_score=0
    kevin_score=0

    x=len(string)

    useful_kevin=list()
    useful_staurt=[y for y in range(x)]

    for i in range(x):
        if string[i] in vowel_list:
            useful_staurt.remove(i)
            useful_kevin.append(i)
            kevin_score+=1
            staurt_score+=1

    staurt_score=staurt_score*(-1)+x

    kevin_score+=(x-1)*(len(useful_kevin))-sum(useful_kevin)
    staurt_score+=(x-1)*(len(useful_staurt))-sum(useful_staurt)

    if staurt_score>kevin_score:
            print("Stuart "+str(staurt_score))
    elif kevin_score>staurt_score:
            print("Kevin "+str(kevin_score))
    else:
            print("Draw")

minion_game2("BANANA")
