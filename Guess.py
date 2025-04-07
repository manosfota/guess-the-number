import random as rd


def guess():
  tries=0
  flag=False
  while tries < 3:
    m=int(input("Give me the number: "))
    random_num=rd.randint(1,10)
    if (m==random_num):
       print("Correct guess")
       break
    else:
       tries+=1
       print("Please try again, You have got {0} tries.".format(3-tries) )



def main():
  guess()


if __name__=='__main__':
    main()