from random import shuffle #функция перемешивания списка, как раз для колоды

#Создание колоды, через цикл, где к каждому значению даём по 4 масти
suits = ['♥️', '♦️', '♠️', '♣️']
cards = ['2', '3', '4','5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

deck = []
for card in cards:
    for suit in suits:
        deck.append([card, suit]) #добавляем в колоду карту в виде списка [значение, масть]

#Стартовая раздача, перемешивание колоды, создание главного словаря
def bj_start():
    shuffle(deck) #перемешиваем колоду
    player_hand = []
    dealer_hand = []
    for i in range(2):
        player_hand.append(deck[i])
    dealer_hand.append(deck[2])
    return {
        'player_hand': player_hand,
        'dealer_hand': dealer_hand,
        'num_cards': 3, #индекс следующей карты в колоде
        'deck': deck, #сама колода
        'end': False #закончилась игра или нет
    }

#функция подсчёта. Сама ничего не считает, а просто вызывает на каждого игрока функцию
def score(data):
    player_hand = data['player_hand'] #на самом деле, абсолютно бесполезная херня, функция по-другому должна была
    dealer_hand = data['dealer_hand'] #выглядеть, но я поменял её, а эту часть для красоты оставил
    return hand_score(player_hand), hand_score(dealer_hand) #возращает список из [счёт игрока, счёт дилера]

#сам подсчёт у игроков
def hand_score(hand):
    score = 0
    for card in hand:
        try: #если наша карта это число, то просто добавляем его. Если карта не может стать числом, прибавляем 10
            score += int(card[0])
        except ValueError:
            if card[0] == 'A':
                score += 11 #В начале задаём тузам 11, если в итоге счёт с ними превысит 21, то меняем их на 1
            else:
                score += 10
    for card in hand:
        if card[0] == 'A' and score > 21:
            score -= 10
    return score

#Функция дирижёр ходов(их будет больше)
def move(data, move, player):
    match move: #крутая штука, аналог if else. match задаёт какой параметр сравниваем, case действия при определённом значение
        case 'hit':
            hit(data, player)
            return 'hit'
        case 'stand':
            if player == 'dealer':
                data['end'] = True #если дилер перестаёт брать карты - заканчиваем игру
            return 'stand'

#Функция добавления карт, к руке добавляет следующую карту из колоды
def hit(data, player):
    hand = f'{player}_hand'
    data[hand].append(data['deck'][data['num_cards']])
    data['num_cards'] += 1

#определяет, как походит дилер, пока умственных вычислений тут нет, делает втупую, но потом будут
def dealer_move(score):
    if score[1] < score[0] and score[0] <= 21 or score[1] < 17:
        return "hit"
    if score[1] == score[0] and score[1] < 17: #типа крутой и сильно не рискует
        return "hit"
    return "stand"

#Смотрит, есть ли победитель в игре
def win_calculate(data, score):
    if score[0] > 21: #Если перебор у кого-то - игра заканчивается сразу
        data['end'] = True
        return "player busted" #bust - перебор
    if score[1] > 21:
        data['end'] = True
        return "dealer busted"
    if data['end']: #Когда дилер остановился, считаем очки
        if score[0] > score[1]:
            return "win"
        if score[1] > score[0]:
            return "lose"
        if score[0] == score[1] and score[0] != 21: #отдельно смотрим ничью, где у каждого 21 и остальные
            return "draw"
        return blackjack_chek(data) #Смотрим ничью, где по 21
    return "continue" #Если никакое условие конца игры невыполнено - говорим продолжать игру

#Блекджек это именно если выбил 21 с двух карт, если больше, то это не блекджек. Он ценится выше, чем 21
def blackjack_chek(data):
    hands = [] #список, в котором 1 - блекджек, 0 - просто 21
    if len(data['player_hand']) == 2:
        hands.append(1)
    else:
        hands.append(0)
    if len(data['dealer_hand']) == 2:
        hands.append(1)
    else:
        hands.append(0)
    match hands:
        case [1, 0]:
            return 'win'
        case [0, 1]:
            return 'lose'
        case _: #такое выражение значит, что при всех значениях не использованных до этого
            return 'draw'