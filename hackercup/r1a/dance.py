import sys, itertools, re
from Queue import Queue

def partition(lst, n):
  q, r = divmod(len(lst), n)
  indices = [q*i + min(i, r) for i in xrange(n+1)]
  return [lst[indices[i]:indices[i+1]] for i in xrange(n)]

def parse_map(rows):
  legal = {}
  for row_id in xrange(len(rows)):
    for col_id in xrange(len(rows[row_id])):
      if rows[row_id][col_id] == 'W':
        continue
      moves = []
      if rows[row_id][col_id].isdigit() and int(rows[row_id][col_id]) > 0:
        for teleport in find_all_chars(rows, rows[row_id][col_id]):
          if teleport != (row_id,col_id):
            moves.append(teleport)
      if row_id > 0 and rows[row_id-1][col_id] != 'W':
        moves.append((row_id-1, col_id))
      if row_id < len(rows) - 1 and rows[row_id+1][col_id] != 'W':
        moves.append((row_id+1, col_id))
      if col_id > 0 and rows[row_id][col_id-1] != 'W':
        moves.append((row_id,col_id-1))
      if col_id < len(rows[row_id]) - 1 and rows[row_id][col_id + 1] != 'W':
        moves.append((row_id,col_id + 1))
      legal[row_id,col_id] = moves
  return legal

def breadthfirst(graph,start,end):
  q = Queue()
  q.put([start])
  while q.empty() == False:
    path = q.get()
    current = path[-1]
    if current == end:
      return len(path) - 1
    for link_node in graph[current]:
      if link_node not in path:
        new_path = path + [link_node]
        q.put(new_path)

def move(rows, moves, to_pos, step_num = 0, path = []):
  if step_num > len(rows)*len(rows[0]):
    raise Exception("Sanity check: too many steps. move has a bug.")
  if rows[to_pos[0]][to_pos[1]] == 'W':
    raise Exception("Sanity check: can't move into a wall. parse_map has a bug.")
  if rows[to_pos[0]][to_pos[1]] == 'E':
    return (step_num, path)
  path.append(to_pos)
  best = (1000,)
  for to_next in moves[to_pos]:
    if (5, 8) == path[-1]:
      print path
      print moves[to_pos]
    if to_next not in path:
      yy = move(rows, moves, to_next, step_num+1, path)
      if yy[0] < best[0]:
        best = yy
  return best

def find_all_chars(rows, char):
  positions = []
  for row_id in xrange(len(rows)):
    for col_id in xrange(len(rows[row_id])):
      if rows[row_id][col_id] == char:
        positions.append((row_id, col_id))
  return positions

def find_char(rows, char):
  return find_all_chars(rows, char)[0]

def find_start(rows):
  return find_char(rows, 'S')

def find_end(rows):
  return find_char(rows, 'E')

def analyze_map(data):
  data = data.strip().split(" ")
  r, c = data[0:2]
  rows = map(list, data[2:])
  moves = parse_map(rows)
  start = find_start(rows)
  end = find_end(rows)
  return breadthfirst(moves, start, end)
  #return move(rows, moves, start, 0, [])

if __name__ == '__main__':
  i = 0
  for line in sys.stdin:
    if i == 0:
      n = int(line)
    else:
      print analyze_map(line)
      if n == i:
        break
    i += 1