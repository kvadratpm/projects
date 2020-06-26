from random import shuffle


class Card:
    suits = ['пикей',
             'червей',
             'бубей',
             'треф']
    values = [None, None, '2', '3', '4', '5', '6', '7', '8', '9', '10',
              'валет', 'дама', 'король', 'туз']

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __lt__(self, card2):
        if self.value < card2.value:
            return True
        if self.value == card2.value:
            if self.suit < card2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, card2):
        if self.value > card2.value:
            return True
        if self.value == card2.value:
            if self.suit > card2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):
        value = self.values[self.value] + ' ' + self.suits[self.suit]
        return value


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name


class Game:
    def __init__(self):
        name1 = input('Имя игрока 1: \n')
        name2 = input('Имя игрока 2: \n')
        self.deck = Deck()
        self.player1 = Player(name1)
        self.player2 = Player(name2)

    def wins(self, winner):
        win = f'{winner} забирает карты'
        print(win)

    def draw(self, p1n, p1c, p2n, p2c):
        d = f'{p1n} кладет {p1c}, {p2n} кладет {p2c}'
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print('Поехали!',len(cards))
        while len(cards) >= 2:
            m = 'Нажмите X для выхода. Нажмите любую другую клавишу для начала игры'
            response = input(m)
            if response == 'X':
                break
            p1c = self.deck.remove_card()
            p2c = self.deck.remove_card()
            p1n = self.player1.name
            p2n = self.player2.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:
                self.player1.wins += 1
                self.wins(self.player1.name)
            else:
                self.player2.wins += 1
                self.wins(self.player2.name)
            win = self.winner(self.player1, self.player2)
            print(f'Игра окончена. {win} выиграл!')

    def winner(self, player1, player2):
        if player1.wins > player2.wins:
            return player1.name
        if player2.wins > player1.wins:
            return player2.name
        else:
            return 'Ничья!'


game = Game()
game.play_game()
