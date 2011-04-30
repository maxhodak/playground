import sys, math, itertools, multiprocessing

def partition(lst, n):
  q, r = divmod(len(lst), n)
  indices = [q*i + min(i, r) for i in xrange(n+1)]
  return [lst[indices[i]:indices[i+1]] for i in xrange(n)]

def perfect_squares(n):
  return [pow(i,2) for i in xrange(n)]

def perfect_pairs(n):
  done = []
  ret = []
  for square1 in n:
    done.append(square1)
    for square2 in n:
      if square2 not in done:
        total = (square1**2) + (square2**2)
        if total <= 2147483647:
          ret.append((square1, square2, total))
  return ret

def find_factor_count(val):
  """docstring for find_factors"""
  pass

if __name__ == '__main__':
  i = 0
  procs = multiprocessing.Pool(15)
  pairs = [resp for resp in procs.map(perfect_pairs, partition(range(741456), 741456/50)) if len(resp) > 0]
  pairs = list(itertools.chain(*pairs))
  for line in sys.stdin:
   if i == 0:
     n = int(line)
   else:
     y = int(line)
     if y == 0:
       print 1
     else:
       matches = filter(lambda x: x[2] == y, pairs)
       print len(matches)
     if n == i:
       break
   i += 1
