import random as rd
def count_letters():
  words_array=['heist','threaten','murder','parrot','rooftop','admission','snake','rain','validation']
  vowels=['e','a','i','u','o','y']
  random_word=rd.choice(words_array)
  print(random_word)
  count=0
  for i in range(len(random_word)):
    if random_word[i] in vowels:
      count=count+1
  consonants=(len(random_word))-count
  print("The word includes {} vowels".format(count)) 
  print("The word includes {} consonants".format(consonants))


def main():
  count_letters()


if __name__=='__main__':
  main()



 



