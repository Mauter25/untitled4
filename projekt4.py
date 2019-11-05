from random import randint, choice
letterslist = ['a', 'b', 'c']
shiplist = []
buchschtabe = []
for i in range(3):
    letter = input()
    shiplist.append(i)
for n in range(3):
    buchschtabe.append(randint(0, 2))
while buchschtabe != [] or shiplist != []:
    q = input('Введите координаты: ')
    if q[0] == "a":
        if int(q[1]) == buchschtabe[0]:
           print('Убил')
           buchschtabe.remove(buchschtabe[0])
        else:
            print('Промах')
            buchschtabe.remove(buchschtabe[0])
    if q[0] == "b":
        if int(q[1]) == buchschtabe[1]:
            print('Убил')
            buchschtabe.remove(buchschtabe[1])
        else:
            print('Промах')
            buchschtabe.remove(buchschtabe[1])
    if q[0] == "c":
        if int(q[1]) == buchschtabe[2]:
            print('Убил')
            buchschtabe.remove(buchschtabe[2])
        else:
            print('Промах')
            buchschtabe.remove(buchschtabe[2])
    shot = randint(0, 2)
    shot_1 = choice(letterslist)
    if shiplist[shot] == shot_1:
        print('Ваш корабль убит!')
        shiplist.remove(shot_1)
    else:
        print('Соперник промахнулся!')