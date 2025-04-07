#Harmonic Sequence 
import math
from fractions import Fraction
m=int(input("Για να υπολογισετε:\n\t1) Όλους τους ορους της ακολουθιας πιεστε --1-- \n\t2) ενα συγκεκριμενο ορο πιεστε --2-- \n\n"))

n=int(input('\n\nΜέχρι ποιο όρο της ακολουθίας θέλετε να υπολογίσετε: '))
d=int(input('Δωστε το βημα της ακολουθιας: '))
a_1=int(input('Δωστε τον πρώτο όρο της ακολουθιας: '))

if m==1:
  for n in range(1,n):
    numerator=1
    denominator=a_1+(n-1)*d
    fraction=Fraction(numerator,denominator)
    print(fraction)
elif m==2:
  numer=1
  denom=a_1+(n-1)*d
  fraction=Fraction(numer,denom)
  print(fraction)
else:
  print("Incorrect option. Please choose bewween 1 or 2")