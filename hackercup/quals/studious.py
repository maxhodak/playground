import sys, math, itertools

def generate_candidates(token_string):
  tokens = token_string[2:].strip().split(" ")
  return sorted(["".join(permute) for permute in itertools.permutations(tokens)])[0]

if __name__ == '__main__':
  i = 0
  for line in sys.stdin:
    if i == 0:
      n = int(line)
    else:
      print generate_candidates(line)
      if n == i:
        break
    i += 1