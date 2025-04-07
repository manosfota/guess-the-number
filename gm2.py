import random as rd
import sys

 #substitution=str.maketrans({wr_array: '*'})
  #result=wr_array.translate(substitution)

def kremala():
  words_array=['heist','threaten','murder','parrot','rooftop','admission','snake','rain','validation']
  random_word=rd.choice(words_array)
  wr_array=random_word
  print(wr_array)
 
  
  range_word= [ "_" for i in range(len(random_word))]
  print("The word include {0} letters".format(len(random_word)))
  print(range_word)

  letters_given=""
  cntr=10
  flag=True
  while (flag):
    try:
      start=int(input("Press 1 to start the game: \n"))
      if (start == 1):        
        flag=False
    except:
      print("Please try again")

  while (cntr>0):
      if ('_' in range_word):
        try:
          guess_letter=input("Please give me your guess Letter: ")
          if (guess_letter.isalpha() and len(guess_letter)==1):        
            if (guess_letter in wr_array):
              if (guess_letter not in letters_given):              
                indices=[pos for pos, char in enumerate(wr_array) if char == guess_letter]
                # print(indices)
                letters_given+=guess_letter
                for i in range(0, len(indices)):
                  range_word[indices[i]]=guess_letter
                  print (range_word)
                cntr-=1
              else:
                print("The letter has been given. Try again")  
            else:     
              cntr-=1       
              if (cntr >=1):
                print(" Wrong Guess. Remaining Tries: {0}".format(cntr))
              
          else:
              print("Please try again. Your attempt has not been counted.")
        except:
          print("Please,Try again!")
      else:
        print("\nYou won!!!")
        exit()
  print("\nUnfortunately you lost... Please play again.")
        
      
        





def main():
  kremala()



if __name__=='__main__':
  main()
