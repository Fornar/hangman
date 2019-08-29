# Игра "Вислелица"
def hangman():
    the_words = ["компьютер",
                 "бумага",
                 "кружка",
                 "кот",
                 "книга",
                 "мир",
                 "свет",
                 "часы",
                 "день",
                 "фломастер",
                 "математика",
                 "мистика",
                 "киберпанк",
                 "планшет",
                 "квадрат"
                 ]
    import random
    word = the_words[random.randint(0,14)]
    wrong = 0
    stages = ["",
              "_______     ",
              "|      |    ",
              "|      |    ",
              "|      0    ",
              "|     /|\   ",
              "|     / \   ",
              "|           "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Добро пожаловать на казнь!")
    print(" ".join(board) + " - столько букв в вашем слове.")
    while wrong < len(stages) - 1:
        print("\n")
        guess = input("Введите букву: ")
        if guess in rletters:
            cind = rletters.index(guess)
            board[cind] = guess
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("Вы выиграли! Было загадано слово: {}.".format(word))
            win = True
            break
    if not win:
        print("Вы проиграли! Было загадано слово: {}.".format(word))
print("Висилица")
ans = input("Начать игру?: ")
if  ans == "да" or ans == "Да" or ans == "ДА":
    print("\n")
    hangman()
    while ans == "да" or ans == "Да" or ans == "ДА":
        ans = input("Начать игру заново?: ")
        if ans == "да" or ans == "Да" or ans == "ДА":
                hangman()
        else:
            print("Отлично сыграно! Приходите ещё!")        
            break
else:
    print("Ну ладно... Ещё увидимся!")
