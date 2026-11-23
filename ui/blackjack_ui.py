#Функция рисования руки, рисует столько карт, сколько есть у игрока
def print_hand(hand): #Принимает руку, которую будет рисовать
    print("  ".join("|------|" for card in hand))
    print("  ".join("|      |" for card in hand))
    print("  ".join(f"|{card[0] + card[1]:^6}|" for card in hand))
    print("  ".join("|      |" for card in hand))
    print("  ".join("|------|" for card in hand))

#Функция отрисовки самой игры, при ходах игрока
def bj_screen(data, score):
    dealer_hand = data["dealer_hand"]
    player_hand = data["player_hand"]
    print("=====Blackjack=====")
    print("Dealer:")
    print_hand(dealer_hand)
    print(f"\nScore: {score[1]}")
    print("-" * 50)
    print("Player:")
    print_hand(player_hand)
    print(f"\nScore: {score[0]}")
    print('')
    print('Next move:')
    print('1 - Hit')
    print('2 - Stand')
    while True:
        choice = input("> ")
        match choice:
            case '1':
                return 'hit'
            case '2':
                return 'stand'
            case _:
                print("Invalid choice")

#Отрисовка финального экрана, где показан итог игры
def bj_end(data, score, result):
    dealer_hand = data["dealer_hand"]
    player_hand = data["player_hand"]
    print("=G=A=M=E= =E=N=D=")
    print_hand(dealer_hand)
    print(f"\nScore: {score[1]} : {score[0]}, {result}")
    print_hand(player_hand)