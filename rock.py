import random

def computerChoice():
    moves = ['r', 'p', 's']
    return random.choice(moves)

while True:
    userMove = input('(r)ock, (p)paper, (s)iccors, (q)uit ')
    computerMove = computerChoice()
    
    if userMove == 'q':
        break
    
    if userMove == computerMove:
        print('Tie!')

    elif userMove == 'r':
        if computerMove == 'p':
            print('You lose!')
        else:
            print('You win!')

    elif userMove == 'p':
        if computerMove == 'r':
            print('You win!')

        else: 
            print('You lose!')

    elif userMove == 's':
        if computerMove == 'p':
            print('You win!')
        else:
            print('You lose!')
    
    

