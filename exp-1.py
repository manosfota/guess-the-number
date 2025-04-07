from functools import reduce
import random as rd
import numpy as np
from collections import Counter
from itertools  import combinations 
import time



  # if (intl_num > 0) & (fnl_num > 0):
  #   break
  # else:
  #   print("(Οι αριθμοι πρεπει να  ειναι θετικοι ακαιρεοι) \n")

# for i in range(1,fnl_num):
#    for j in range (1, fnl_num):
#      if (i%j==0):
#        print(f"Ο αριθμος {i} ")
fnl_num=int(input("Δωστε τoν αριθμο τον οποιο θελετε να βρειτε τους πρωτους αριθμους: "))
start = time.time()
print("*** Start of Program ***")
for num in range(2,fnl_num):
    prime = True
    for i in range(2,(num//2)+1):
        if (num%i==0):
            prime = False
            break
    if prime:
      print(num, end=' ')


end = time.time()
print (start, end)
print("*** Elapsed time: ",end=' ')
print(end - start)
print("*** End of Program ***")    
  





  















 



