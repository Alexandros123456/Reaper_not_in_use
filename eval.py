from main_classes import *


class Evaluator:

    def cards_ranks(self, hand):
        ranks = [r for r, s in hand]
        ranks.sort(reverse=True)
        return ranks

    def hi(self):
        print('hi')

    # def hand_eval(self, hand):
    #     """
    #     Evaluates the a single poker hand. The size of of each hand can be:
    #     *2 @ preflop
    #     *5 @ flop
    #     *6 @ turn
    #     *7 @ river
    #
    #     :param hand: list of hand
    #     :return:
    #     """
    #
    # return
