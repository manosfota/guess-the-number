import decimal 
from decimal import Decimal 
decimal.getcontext().prec=16

from fractions import Fraction
import time

n=int(input('\n\nΜέχρι ποιο όρο της ακολουθίας θέλετε να υπολογίσετε: '))

start_time = time.time()

numerator=1
denominator=1
sum=0
for i in range (0,n):
  fraction=((-1)**i)*Fraction(numerator,denominator)
  print(fraction,end= ' ')

  sum+=((-1)**i)*(Decimal(numerator)/Decimal(denominator))
  
  # print(sum)
  denominator+=2
print("\n",4*sum)
elapsed_time = time.time() - start_time
print(f'Elapsed time: {elapsed_time} seconds')


  
