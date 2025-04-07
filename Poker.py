import random as rd
from functools import reduce
import operator as op

def Dealer_Cards(Cards):
    print("\n--DEALER CARDS--")
    d_card=[]                   
    for i in range(5):
        d_card.append(Cards.pop(rd.randrange(len(Cards))))
        print(d_card)
    return d_card


def Players_Cards(Cards):
    print("\n--PLAYER CARDS--\n")
    p1_card=[]
    for i in range(2):
        p1_card.append(Cards.pop(rd.randrange(len(Cards))))
    print(p1_card)
    p2_card=[]
    for i in range(2):
        p2_card.append(Cards.pop(rd.randrange(len(Cards))))
    print(p2_card)
    return p1_card,p2_card
    
def Hand_Ranking(dl_crd,Dlc,P1c,P2c):
    if '\u2663' in Dlc:
        print("\u2663")
    else:
        print("Not")


def Flosh_Royal(dl_crd):
    for dl_crd in len(dl_crd):
        print(dl_crd)



def main():
     Cards=["A\u2663", "A\u2665", "A\u2666", "A\u2660", # Filla Trapoulas
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
          
     dl_crd=Dealer_Cards(Cards)
     [pl_crd,p2_crd]=Players_Cards(Cards)
     print("\n\n\n")
     Flosh_Royal(dl_crd)
   
   
if __name__=='__main__':
    main()




