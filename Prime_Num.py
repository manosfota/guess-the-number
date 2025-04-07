from functools import reduce
import random as rd
import numpy as np
from collections import Counter
from itertools  import combinations 
import time

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
print("*** Elapsed time: ",end=' ')
print(end - start)
print("*** End of Program ***")    
  





  















 



