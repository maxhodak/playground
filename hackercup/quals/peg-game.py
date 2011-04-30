import sys, math, itertools

def partition(lst, n):
  q, r = divmod(len(lst), n)
  indices = [q*i + min(i, r) for i in xrange(n+1)]
  return [lst[indices[i]:indices[i+1]] for i in xrange(n)]

def prob_for_column(col_idx, r, c, holes_map):
  cur_col = col_idx
  for row in xrange(r):
    if cur_col == 0:
      cur_col
       or cur_col == c:
      

def analyze_case(data):
  data = map(int, data.split(" "))
  r, c, k, m = data[0:4]
  pairs = partition(data[4:], 2)
  print r
  print c
  print k
  print m
  print pairs

if __name__ == '__main__':
  i = 0
  for line in sys.stdin:
    if i == 0:
      n = int(line)
    else:
      print analyze_case(line)
      if n == i:
        break
    i += 1