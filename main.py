from random import randint

score = 0
while True:
    door = randint(1, 3)
    while True:
        door_inp = input('Pick a door (1, 2 or 3): ')
        if door_inp.isdigit():
            door_inp = int(door_inp)
        if door_inp not in range(1, 4):
            print('Invalid door!')
        else:
            break
    if door != door_inp:
        print('You enter the next room (oooooh spoooky)')
        score += 1
    else:
        print('GHOST! 👻')
        break
print(f'You died! Your score was {score}')
