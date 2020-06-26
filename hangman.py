import random
def hangman (word):
    wrong = 0
    stages = ['',
              '________',
              '|    |  ',
              '|    |  ',
              '|    O  ',
              '|   /|\ ',
              '|   / \ ',
              '|       ',
              ]
    rleters = list(word)
    board = ['_']*len(word)
    win = False
    print('Добро пожаловать на казнь!')
    while wrong<len(stages) - 1:
        print((' '.join(board)))
        print('\n')
        msg = 'Введите букву: '
        char = input (msg)
        if char in rleters:
            cind = rleters.index(char)
            board[cind]=char
            rleters[cind]='$'
        else:
            wrong+=1
        print ((' '.join(board)))
        e= wrong+1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('Вы выиграли! Было загадано слово: ')
            print (' '.join(board))
            win = True
    if not win:
        print ('\n'.join(stages[0:wrong]))
        print ('Вы проиграли! Было загадано слово: {}.'.format(word))
dict =['питон',
       'кот',
       'танк',
       'орангутанг',
       'машина']
hangman(random.choice(dict))