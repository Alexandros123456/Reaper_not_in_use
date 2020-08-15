from main_classes import *
import collections


def poker(hands):
    return max(hands, key=hand_rank)


def card_ranks(hand):
    """

    :param cards: list of cards
    :return: ranks in descending order
    """

    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks


def straight(ranks):
    """
    Returns True if the ordered ranks form a 5- card straight

    :param ranks:
    :return True/False:
    """
    return (max(ranks) - min(ranks) == 4) and (len(set(ranks)) == 5)


def flush(hand):
    """
    Returns True if 5 cards have the same suit
    :param hand:
    :return:
    """
    suits = [s for r, s in hand]
    freq = collections.Counter(suits)
    if 5 in list(freq.values()):
        return True
    else:
        return False


def kind(n, ranks):
    """
    Returns the first rank that this hand has exactly n of or None
    :param n:
    :param ranks:
    :return:r or None
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
        else:
            return None


def hand_rank(hand):
    """
    Returns the rank of a hand. Ranks are from 8 to 0, with:

    8: straight flush
    7: four of a kind
    6: full house
    5: flush
    4: straight
    3: 3 of a kind
    2: 2 pairs
    1: 1 pair
    0: highest kicker

    :param hand as a list
    :return: rank of hand
    """
    ranks = card_ranks(hand)

    # straignt flush
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    # four of a kind
    elif kind(4, ranks):
        return (7, kind(4, ranks))
    # full house
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    # flush
    elif flush(hand):
        return (5, ranks)
    # straight
    elif straight(ranks):
        return (4, max(ranks))
    # three of a kind
    elif kind(3, ranks):
        return (3, kind(3, ranks))
    # 2 pairs
    elif two_pair(ranks):
        return (2, two_pair(ranks))
    # 1 pairs
    elif kind(2, ranks):
        return (1, kind(2, ranks))
    # kicker
    else:
        return (0, ranks)

# class Evaluator:
#
#     def cards_ranks(self, hand):
#         ranks = [r for r, s in hand]
#         ranks.sort(reverse=True)
#         return ranks
#
#
#
#     # def hand_eval(self, hand):
#     #     """
#     #     Evaluates the a single poker hand. The size of of each hand can be:
#     #     *2 @ preflop
#     #     *5 @ flop
#     #     *6 @ turn
#     #     *7 @ river
#     #
#     #     :param hand: list of hand
#     #     :return:
#     #     """
#     #
#     # return
