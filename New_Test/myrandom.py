import random

perm_list1 = ["MA", "MB", "MC", "MD"]
perm_list2 = ["WA", "WB", "WC", "WD"]

men_rankings = {}
women_rankings = {}

for i in perm_list1:
    men_rankings[i] = sorted(perm_list2, key=lambda k: random.random())

for i in perm_list2:
    women_rankings[i] = sorted(perm_list1, key=lambda k: random.random())

print "men_rankings = {}".format(men_rankings)
print "\n"
print "women_rankings = {}".format(women_rankings)
