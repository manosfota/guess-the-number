import random as rd

def game():
  list_codes=["Rock","Paper","Scissors"]
  try:
    num_player=int(input("Choose a number: "))
    while (num_player < 0 or num_player > 3):
      num_player=int(input("Choose a number: "))
    num_pc=rd.randint(1,3)
    print("Player: {0}, PC: {1}".format(list_codes[num_player-1],list_codes[num_pc-1]))
    if (num_player==num_pc):
      print("Draw")
    elif (((num_player==2) and (num_pc==1)) or ((num_player==3) and (num_pc==2)) or ((num_player==1) and (num_pc==3))):
      print("Player Winner!")
    else:
      print("Pc Winner")
  except ValueError:
    print("Exception Error Program Terminated.")









def main():
  game()


if __name__=='__main__':
    main()