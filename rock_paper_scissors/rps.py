#!/usr/bin/python

import sys

# n = 1: [['rock'], ['paper'], ['scissors']]
# n = 2: [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'], ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'], ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']]

def rock_paper_scissors(n):
  moves = [['rock'], ['paper'], ['scissors']] 
  possible_plays = []
  # print('possible plays', possible_plays)

  if n == 0:
    return [[]]
  if n == 1:
    return moves
  
  for rps_list in rock_paper_scissors(n-1):
    for play in moves:
      possible_plays.append(rps_list + play)
      print('rps_list', rps_list)
      print('play', play)
  return possible_plays

  


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')