#!/usr/bin/env python
import sys
class Person:
	def __init__(self, pid, rankings):
		self.pid = pid
		self._rankings = rankings
		self._proposedTo = dict([(k,False) for k in rankings])
		self._engagedTo = None

	def _breakOffWith(self, p):
		assert(p == self._engagedTo and p != None)
		self._engagedTo = None
		p._engagedTo = None

	def nextHighestUnproposed(self):
		for r in self._rankings:
			if not self._proposedTo[r]: return r
		return None

	def breakOff(self):
		p = self._engagedTo
		self._breakOffWith(p)

	def getFiancee(self):
		return self._engagedTo

	def engageTo(self, p):
		if self.getFiancee():
			self.breakOff()
		self._engagedTo = p
		if p.getFiancee():
			p.breakOff()
		p._engagedTo = self

	def isFree(self):
		return not self._engagedTo

	def prefers(self, m1, m2):
		return self._rankings.index(m1.pid) < self._rankings.index(m2.pid)

	def proposedTo(self, p):
		self._proposedTo[p.pid] = True

	def canPropose(self):
		return not all(self._proposedTo.values())

men_rankings = {'MA': ['WA','WB','WC','WD'], 'MB': ['WB','WD','WC','WA'],
			    'MC': ['WC','WB','WA','WD'], 'MD': ['WB','WA','WD','WC']}
women_rankings = {'WA': ['MC','MD','MA','MB'], 'WB': ['MA','MD','MB','MC'],
				  'WC': ['MC','MB','MA','MD'], 'WD': ['MB','MC','MD','MA']}
#men_rankings = {'MA': ['WA','WB','WC'], 'MB': ['WB','WA','WC'], 'MC': ['WB','WA','WC']}
#women_rankings = {'WA': ['MA','MC','MB'], 'WB': ['MA','MB','MC'], 'WC': ['MB','MC','MA']}
men = {k: Person(k,ranks) for (k,ranks) in men_rankings.items()}
women = {k: Person(k,ranks) for (k,ranks) in women_rankings.items()}

def freeMan(ms):
	for m in ms.values():
		if m.isFree() and m.canPropose(): return m
	return None

#################################
######## Begin algorithm ########
#################################

m = freeMan(men)
while m:
	wid = m.nextHighestUnproposed()
	w = women[wid]
	if w.isFree():
		m.engageTo(w)
	else:
		m2 = w.getFiancee()
		if w.prefers(m, m2):
			w.engageTo(m)
	m.proposedTo(w)
	m = freeMan(men)

for m in sorted(men.values(), key=lambda m: m.pid):
	w = m.getFiancee()
	print "%s <==> %s" % (m.pid, w.pid if w else "NONE")
