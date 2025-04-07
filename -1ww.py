import random 
from collections import Counter 

list=["A","B","C","D","F"]

occ=random.choices(list)
print(occ)
counter=Counter(list)
print(counter)

       