from CardGame import CardGame
from Player import Player

player1=Player("elad")
player2=Player("eli")
game=CardGame(player1.name.title(), player2.name.title())
print(game.player1)
print(game.player2)
for i in range(1,11):
    if len(game.player1.cards)<1 or len(game.player2.cards)<1:
        break
    c=game.player1.get_card()
    c2=game.player2.get_card()
    print(f'========== Round{i} ==========')
    print(f'{game.player1.name.title()} Card is: {c}')
    print(f'{game.player2.name.title()} Card is: {c2}')
    if c > c2:
        game.player1.add_card(c)
        game.player1.add_card(c2)
        print(game.player1.name.title()),f'Win this round {i} and taking the cards'
    else:
        game.player2.add_card(c)
        game.player2.add_card(c2)
        print(game.player2.name.title()), f'Won this round {i} and taking the cards'

print('========== End Game ==========')
if game.get_winner()==None:
    print("It's a draw")
else:
    print(game.get_winner())

# print(game.player1.cards)
# print(game.player2.cards)