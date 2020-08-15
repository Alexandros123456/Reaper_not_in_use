import random
from main_classes import *

# #lets run a simulation!!!
#
# n = 100000
# results = []
# for i in range(1,n):
#     a = Game(9)
#     results.append(a.deal_cards())
#
# results_flat = [item for sublist in results for item in sublist]
#
# results = pd.DataFrame(results_flat, columns=['test'])
#
# freqs = pd.DataFrame(results['test'].value_counts()).reset_index()
#
#
# freqs.plot.bar(x='index', y='test', rot=0)


a = Game(9)
print(a)