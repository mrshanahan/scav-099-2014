import random

perm_list1 = ["MA", "MB", "MC", "MD", "ME", "MF", "MG", "MH", "MI", "MJ"]
perm_list2 = ["WA", "WB", "WC", "WD", "WE", "WF", "WG", "WH", "WI", "WJ"]

mens_rankings = {}
womens_rankings = {}

for i in perm_list1:
    mens_rankings[i] = sorted(perm_list2, key=lambda k: random.random())

for i in perm_list2:
    womens_rankings[i] = sorted(perm_list1, key=lambda k: random.random())

print mens_rankings
print "\n\n"
print womens_rankings
