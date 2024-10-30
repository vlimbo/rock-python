import random

def computerChoice():
    moves = ['rock', 'paper', 'scissors']
    return random.choice(moves)

userMove = input('(r)ock, (p)paper, (s)iccors, (q)uit ')
