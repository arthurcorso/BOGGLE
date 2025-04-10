import random

DES = [
    ['L', 'E', 'N', 'U', 'Y', 'G'],
    ['E', 'L', 'U', 'P', 'S', 'T'],
    ['Z', 'D', 'V', 'N', 'E', 'A'],
    ['S', 'D', 'T', 'N', 'O', 'E'],
    ['A', 'M', 'O', 'R', 'I', 'S'],
    ['F', 'X', 'R', 'A', 'O', 'I'],
    ['M', 'O', 'Q', 'A', 'B', 'J'],
    ['F', 'S', 'H', 'E', 'E', 'I'],
    ['H', 'R', 'S', 'N', 'E', 'I'],
    ['E', 'T', 'N', 'K', 'O', 'U'],
    ['T', 'A', 'R', 'I', 'L', 'B'],
    ['T', 'I', 'E', 'A', 'O', 'A'],
    ['A', 'C', 'E', 'P', 'D', 'M'],
    ['R', 'L', 'A', 'S', 'E', 'C'],
    ['U', 'L', 'I', 'W', 'E', 'R'],
    ['V', 'G', 'T', 'N', 'I', 'E']
]

def generer_grille():
    lettres = [random.choice(de) for de in DES]
    random.shuffle(lettres)
    return [lettres[i*4:(i+1)*4] for i in range(4)]
