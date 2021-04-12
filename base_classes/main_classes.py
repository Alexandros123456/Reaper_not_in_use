# import pandas as pd
import numpy as np
import itertools
import random


class Card:

    def __init__(self):
        self.suite = ['D', 'H', 'S', 'C']
        self.value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.cards_list = [''.join(t) for t in list(itertools.product(*[self.suite, self.value]))]
        self.symbol_mapping = {
            'S': '♠',
            'D': '♦',
            'H': '♥',
            'C': '♣',
        }


class Deck(Card):
    deck_size = 52

    def __init__(self):
        super().__init__()
        self.deck = random.sample(self.cards_list, self.deck_size)

    def draw_card(self, number_of_cards):
        self.drawn_cards = random.sample(self.deck, number_of_cards)
        self.deck = set(self.deck).difference(self.drawn_cards)

        return self.drawn_cards, self.deck


class Players:

    def __init__(self, number_of_players=9):
        self.player_names = ['Villain_' + str(i) for i in range(1, number_of_players)]
        self.player_names.insert(0, 'Hero')


class Game(Players, Deck):

    def __init__(self):
        Players.__init__(self)
        Deck.__init__(self)
        self.board = []
        self.game_rounds = ['Pref-lop', 'Flop', 'Turn', 'River']
        self.draw_player_cards_at_round = [2, 0, 0, 0]
        self.draw_board_cards_at_round = [0, 3, 1, 1]

    def run_game(self):

        for i, game_round in enumerate(self.game_rounds):

            self.board.append(self.draw_card(self.draw_board_cards_at_round[i])[0])
            print('\nIt is round {}: Cards on board: {}\n'.format(game_round, list(np.concatenate(self.board).flat)))

            for j, player in enumerate(self.player_names):
                if self.draw_player_cards_at_round[i] != 0:
                    print('Player: {} draws cards:{}'.format(player,
                                                             self.draw_card(self.draw_player_cards_at_round[i])[0]))
