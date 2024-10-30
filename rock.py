import random

def computerChoice():
    moves = ['r', 'p', 's']
    return random.choice(moves)


wins, loses, ties = 0, 0, 0

while True:
    userMove = input('(r)ock, (p)paper, (s)iccors, (q)uit ')
    computerMove = computerChoice()
    
    if userMove == 'q':
        break
    
    if userMove == computerMove:
        print('Tie!')
        ties += 1
        print('wins:', wins, 'loses:', loses, 'ties:', ties)

    elif userMove == 'r':
        if computerMove == 'p':
            print('You lose!')
            loses += 1
            print('wins:', wins, 'loses:', loses, 'ties:', ties)
        else:
            print('You win!')
            wins += 1
            print('wins:', wins, 'loses:', loses, 'ties:', ties)

    elif userMove == 'p':
        if computerMove == 'r':
            print('You win!')
            wins += 1
            print('wins:', wins, 'loses:', loses, 'ties:', ties)

        else: 
            print('You lose!')
            loses+= 1
            print('wins:', wins, 'loses:', loses, 'ties:', ties)

    elif userMove == 's':
        if computerMove == 'p':
            print('You win!')
            wins += 1
            print('wins:', wins, 'loses:', loses, 'ties:', ties)
        else:
            print('You lose!')
            loses +=1
            print('wins:', wins, 'loses:', loses, 'ties:', ties)
    
    

