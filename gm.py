import random as rd

def kremala():
  words_array=['heist','threaten','murder','parrot','rooftop','admission','snake','rain','validation']
  random_word=rd.choice(words_array)
  word_array=random_word
  print(word_array)
  range_word= [ "_" for i in range(len(random_word))]
  print("The word include {0} letters".format(len(random_word)))
  print(range_word)
  letters_given=""
  cntr=10
  start=int(input("Press 1 to start the game: \n"))
  while (start==1)and(0<cntr<=10):
      try:
        guess_letter=str(input("Guess Letter:"))
        if (guess_letter in word_array):
          if (guess_letter not in letters_given):
            #print("This letter exists.")
            indices=[pos for pos, char in enumerate(word_array) if char == guess_letter]
            #print(indices)
            letters_given=letters_given+guess_letter
          else:
            print("The letter has been given. Try again")    
        else:
          cntr-=1
          print(" Wrong Guess,Remaining Tries: {0}".format(cntr))
      except ValueError:
        print("Please,Try again!")
        
      
        





def main():
  kremala()



if __name__=='__main__':
  main()
