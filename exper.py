from functools import reduce
import random 
import numpy as np
from collections import Counter
from itertools  import combinations

def list_names():
  list_owner={1:"Tom",2:"James",3:"Catherine"}
  while True:
    #try:
      cd_owner=int(input("Give me the code of owner: "))
      if (cd_owner==1) | (cd_owner==2) | (cd_owner==3):
        print("Welcome",list_owner[cd_owner],"\n")
        nm=list_owner[cd_owner]
        personal_cd(nm, cd_owner)
        break
      else:
        print("Your choises are one of the number (1) (2) (3) \n")   
    # except ValueError:
    #   print("Invalid Code")
  return nm, cd_owner



def personal_cd(mn, cd_owner):
  # import getpass   
  # import sys
  import pwinput

  list_codes={"Tom":2022,"James":8954,"Catherine":3422}
  tries=0
  flag=False
  while tries < 3:
    print("Please {0} press your personal code:".format(mn))
    # p_cd= int(getpass.getpass())
    p_cd=int(pwinput.pwinput(prompt='Password: ', mask='*') )
    if (p_cd==2022) or (p_cd==8954) or (p_cd==3422):
      for name,code in list_codes.items():
        if code == p_cd:
          print("Welcome ",name)
          flag=True
          break
          # sys.exit()
    else:
      print("Invalid code")
    if (flag):
      break
    else:
      tries+=1




def main():
  list_names()


if __name__=='__main__':
    main()