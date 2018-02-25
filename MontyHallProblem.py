import random


prizeBehindDoor = random.randrange(1,4)
doorToRemove = (random.randrange(1,3) == 1)

doors = ['0','0','0']
doors[prizeBehindDoor - 1] = '*'

for door in range(len(doors)):
##    print(door)
    if doors[door] == '*': continue
    if doorToRemove:
        doors[door] ='X'
##        print(door)
        break
    doorToRemove = True
    

print(doors)
