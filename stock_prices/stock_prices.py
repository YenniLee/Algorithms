#!/usr/bin/python

import argparse

def find_max_profit(prices):
  current_min_price = prices[0]
  max_profit = prices[1] - prices[0]

  for i in range(1, len(prices)):
    if prices[1] < current_min_price:
      current_min_price = prices[i]
      # print('current min price:', current_min_price)
    elif prices[i] - current_min_price > max_profit:
      max_profit = prices[i] - current_min_price
      # print('max profit:', max_profit)
  return max_profit


print(find_max_profit([1050, 270, 1540, 3800, 2]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))