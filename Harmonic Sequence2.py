#Harmonic Sequence 
import math
from fractions import Fraction
m=int(input("Για να υπολογισετε:\n\t1) Όλους τους ορους της ακολουθιας πιεστε (1) \n\t2) Ενα συγκεκριμενο ορο πιεστε (2) \n\nΕπιλογή= "))



# (2-m)*n +1  -> n  m=2 ->0, m=1 -> n
# m=1 -----> 1
# m=2 -----> n
# (m-1)*n +(2-m)
# m=1 -> 1
# m=2 => n
#y=ax+b
#y=a(m)*n+b(m)
#1=a(m)+b(m)
#n=2a(m)+b(m)
#a(m)=n-1, b(m)=1-n+1=2-n
#a(m)=n-1, b(m)=2-n


if (m==1 or m==2):
  n=int(input('\n\nΜέχρι ποιο όρο της ακολουθίας θέλετε να υπολογίσετε: '))
  d=int(input('Δωστε το βημα της ακολουθιας: '))
  a_1=int(input('Δωστε τον πρώτο όρο της ακολουθιας: '))
  for n in range((m-1)*n +(2-m),n+1):
    numerator=1
    denominator=a_1+(n-1)*d
    fraction=Fraction(numerator,denominator)
    print(fraction)
else:
  print("Incorrect option. Please choose bewween 1 or 2")