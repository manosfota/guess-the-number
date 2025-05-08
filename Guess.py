import random as rd


def guess():
  secret=rd.randint(1,10)
  tries=0
  max_tries=3

  while tries < max_tries:
    try:
      user_guess=int(input("Give me the number: "))
    except ValueError:
      print("!Please enter a valid number.")
      continue
    
    if (user_guess==secret):
      print("Congratulation. You guessed it!")
      break
    else:
      tries+=1
      remaining=max_tries-tries
      if remaining > 0:
        print("Please try again, You have {0} tries.".format(remaining))
      else:
        print(f" Game over! The correct number was {secret}.")


def main():
  while True:
    guess()
    again=input("Do you want to play again? (yes or no):").lower()
    if again !="yes":
      print("👋 Thanks for playing!")
      break
      


if __name__=='__main__':
    main()