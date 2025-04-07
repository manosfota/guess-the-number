from functools import reduce
import random as rd
from collections import Counter


def Player_Cards(Cards):
    print("How many players are trere? :")
    num_of_players=int(input())
    card_players= [[] for _ in range(num_of_players)]
    #pl_card=[]
    for i in range(0,num_of_players):
        for j in range(0,2):
          card_players[i].append(Cards.pop(rd.randrange(len(Cards))))
    for i in range(0,num_of_players):
      print("\n PLAYER",i+1," CARDS:", card_players[i],"\n")
    return card_players


def PLayer_Investigation(Cards,card_players):
   pass
   

def main():

  Cards=["A\u2663", "A\u2665", "A\u2666", "A\u2660",
           "2\u2663", "2\u2665", "2\u2666", "2\u2660",
           "3\u2663", "3\u2665", "3\u2666", "3\u2660",
           "4\u2663", "4\u2665", "4\u2666", "4\u2660",
           "5\u2663", "5\u2665", "5\u2666", "5\u2660",
           "6\u2663", "6\u2665", "6\u2666", "6\u2660", 
           "7\u2663", "7\u2665", "7\u2666", "7\u2660",
           "8\u2663", "8\u2665", "8\u2666", "8\u2660",
           "9\u2663", "9\u2665", "9\u2666", "9\u2660",
           "10\u2663","10\u2665","10\u2666","10\u2660",
           "J\u2663", "J\u2665", "J\u2666", "J\u2660",
           "Q\u2663", "Q\u2665", "Q\u2666", "Q\u2660",
           "K\u2663", "K\u2665", "K\u2666", "K\u2660"]
  Player_Cards(Cards)

if __name__=='__main__':
  main()

