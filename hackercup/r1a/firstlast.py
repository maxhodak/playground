from __future__ import division
import sys, itertools
from fractions import Fraction

def partition(lst, n):
  q, r = divmod(len(lst), n)
  indices = [q*i + min(i, r) for i in xrange(n+1)]
  return [lst[indices[i]:indices[i+1]] for i in xrange(n)]

def turn_prob(to_turn, overtake, normal):
  if to_turn:
    return 1-(1/overtake)
  else:
    return 1-(1/normal)

def analyze_case(turnset):
  return reduce(lambda acc, cur: acc*cur,
                [turn_prob(turn[0], turn[1][0], turn[1][1]) for turn in turnset],
                1)

def analyze_race(data):
  data = map(int, data.split(" "))
  r, t = data[0:2]
  turns = partition(data[2:], int(len(data[2:])/2))
  possible_worlds = []
  for comb in itertools.combinations(turns, r):
    race = [(turn in comb, turn) for turn in turns]
    possible_worlds.append(analyze_case(race))
  frac = reduce(lambda acc, cur: acc*cur, possible_worlds, 1)
  return Fraction("%7.5f" % frac)

if __name__ == '__main__':
  i = 0
  for line in sys.stdin:
    if i == 0:
      n = int(line)
    else:
      print analyze_race(line)
      if n == i:
        break
    i += 1