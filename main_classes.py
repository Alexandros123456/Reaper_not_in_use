import pandas as pd
import numpy as np
import itertools
import random


class Card:

    def __init__(self):
        self.suite = ['D', 'H', 'S', 'C']
        self.value = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        self.full_deck = [''.join(t) for t in list(itertools.product(*[self.suite, self.value]))]


class Deck(Card):
    number_of_cards = 52

    def __init__(self):
        Card.__init__(self)

    def print_the_deck(self):
        return self.full_deck

    def shuffle_deck(self):
        return random.shuffle(self.full_deck)

    def draw_card(self, number_of_cards):
        return random.sample(self.full_deck, number_of_cards)


class Game(Deck):

    def __init__(self, number_of_players=9):
        Deck.__init__(self)
        Card.__init__(self)

        self.number_of_players = number_of_players
        self.game_rounds = ['preflop', 'flop', 'turn', 'river']

    def deal_cards(self):
        return self.draw_card(self.number_of_players * 2 + 5)

    def deal_cards_game(self):

        game_deck = self.full_deck[:]
        players_draw = []
        player_names = ['Player_' + str(i) for i in range(1, self.number_of_players + 1)]
        preflop_results = pd.DataFrame()
        sep = '-'

        for rnd in self.game_rounds:

            if rnd == 'preflop':

                for plr in player_names:
                    temp_card_1 = random.choice(game_deck)
                    game_deck.remove(temp_card_1)

                    temp_card_2 = random.choice(game_deck)
                    game_deck.remove(temp_card_2)

                    temp_pair = temp_card_1 + '-' + temp_card_2
                    preflop_results[plr] = [temp_pair]

                    players_draw.append(temp_pair)

                preflop_draw = pd.DataFrame(players_draw).T

                for i, plr in enumerate(player_names):
                    preflop_draw.rename(columns={preflop_draw.columns[i]: plr}, inplace=True)

                preflop_draw['Board'] = ''
                preflop_draw['Round'] = rnd

            if rnd == 'flop':
                flop_draw_p = pd.DataFrame(players_draw).T
                flop_draw = random.sample(game_deck, 3)

                for c in flop_draw:
                    game_deck.remove(c)

                for i, plr in enumerate(player_names):
                    flop_draw_p.rename(columns={flop_draw_p.columns[i]: plr}, inplace=True)

                flop_draw_p['Board'] = [sep.join(flop_draw)]
                flop_draw_p['Round'] = rnd

            if rnd == 'turn':
                turn_draw_p = pd.DataFrame(players_draw).T
                turn_draw = random.sample(game_deck, 1)

                for c in turn_draw:
                    game_deck.remove(c)

                for i, plr in enumerate(player_names):
                    turn_draw_p.rename(columns={turn_draw_p.columns[i]: plr}, inplace=True)

                turn_draw_p['Board'] = [sep.join(flop_draw + turn_draw)]
                turn_draw_p['Round'] = rnd

            if rnd == 'river':
                river_draw_p = pd.DataFrame(players_draw).T
                river_draw = random.sample(game_deck, 1)

                for c in river_draw:
                    game_deck.remove(c)

                for i, plr in enumerate(player_names):
                    river_draw_p.rename(columns={river_draw_p.columns[i]: plr}, inplace=True)

                river_draw_p['Board'] = [sep.join(flop_draw + turn_draw + river_draw)]
                river_draw_p['Round'] = rnd

        games_results_round = preflop_draw.append([flop_draw_p, turn_draw_p, river_draw_p])
        games_results_round.reset_index(inplace=True, drop=True)
        games_results_round = games_results_round.rename(columns={'Player_1':'Hero'})



        return games_results_round



#
a = Game(9)
#
test = a.deal_cards_game()
