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


def two_pair(ranks):
    """
    For 2 pairs, returns the the 2 ranks as a tuple. Since there can be 7 cards on the
    :param ranks
    :return: tuple (high pairs, low pair)
    """
    # ranks = ranks[:4]
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return (pair, lowpair)
    else:
        return None


def group(items):
    """
    return a list of [(count, x)...] highest count first then highest x first

    :param items:
    :return:
    """
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(pairs): return zip(*pairs)


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
    groups = group(['--23456789TJQKA'.index(r) for r, s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = (len(ranks) == 5) and (max(ranks) - min(ranks) == 4)
    flush = len(set([r for r, s in hand])) == 1
    return max(count_rankings[counts], 4 * straight + 5 * flush), ranks


count_rankings = {(5,): 10, (4, 1): 7, (3, 2): 6, (3, 1, 1): 3, (2, 2, 1): 2,
                  (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}

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

