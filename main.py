from src.blackjack import *
from ui.blackjack_ui import *
from ui.clear import clear #функция очистки экрана, в пайчарм не работает, только в комадной строке

#основной цикл
while True:
    print('1 - Play Blackjack')
    print('2 - Exit')
    choice = input()
    if choice == '1':
        data = bj_start() #стартовая раздача
        scores = score(data)
        #цикл ходов игрока
        while True:
            clear() #то что ниже работает так: ход получает функцию отрисовки экрана, которая отрисовывает экран и при этом даёт ход
            action = move(data, bj_screen(data, scores), 'player') #получает колоды, ход и то, что ходит игрок
            scores = score(data)
            result = win_calculate(data, scores) #смотрим, не закончилась ли игра
            if result != 'continue':
                break
            if action == 'stand': #если игрок нажал стенд - заканчиваем его ходы
                break
        #цикл дилера
        while result == 'continue':
            move(data, dealer_move(scores), 'dealer')
            scores = score(data)
            result = win_calculate(data, scores)
        clear()
        bj_end(data, scores, result)
    else:
        break