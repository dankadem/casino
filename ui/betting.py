minimum = {
    "Blackjack": 500
}

def place_bet(money, game):
    print("="*20)
    print("Place a bet")
    print("="*20)
    print(f'Game: {game}')
    print("-"*20)
    print(f'Your balance: {money}')
    print('-'*20)
    print(f'Minimum stake: {minimum[game]}')
    print('='*20)
    while True:
        stake = int(input(">"))
        if stake > minimum[game] and stake <= money:
            break
        print("You haven't got enough money or your stake is too small")
    return stake