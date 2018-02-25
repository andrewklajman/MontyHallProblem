import random


def result():
    DOORS = ['G', 'G', 'G']
    DOORS[random.randrange(0,3)] = 'C'
    ContestantChoice = random.randrange(0,3)

    HostChoice = 0
    for i in range(3):
        if i != ContestantChoice and DOORS[i] == 'G':
            HostChoice = i
            break


    Result1 = DOORS[ContestantChoice] == 'C'

    for i in range(3):
        if i != ContestantChoice and i != HostChoice:
            ContestantChoice = i
            break

    Result2 = DOORS[ContestantChoice] == 'C'
    return(Result1, Result2)



with open('output.csv','w') as f:
    for i in range(1000000):
        GameResult = result()
        ouput = str(GameResult[0]) + ',' + str(GameResult[1]) + '\n'
        f.write(ouput)
        if i % 1000 ==0: print(i)



##
##prizeBehindDoor = random.randrange(1,4)
##doorToRemove = (random.randrange(1,3) == 1)
##
##doors = ['0','0','0']
##doors[prizeBehindDoor - 1] = '*'
##
##for door in range(len(doors)):
####    print(door)
##    if doors[door] == '*': continue
##    if doorToRemove:
##        doors[door] ='X'
####        print(door)
##        break
##    doorToRemove = True
##    
##
##print(doors)
