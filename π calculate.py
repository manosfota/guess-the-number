from fractions import Fraction

n=int(input('\n\nΜέχρι ποιο όρο της ακολουθίας θέλετε να υπολογίσετε: '))
numerator=1
denominator=1
sum=0
for i in range (0,n):
  fraction=Fraction(numerator,denominator)
  print(fraction,end= ' ')
  if (i%2==0):    
    sum+=float(fraction)    
  else:
    sum-=float(fraction)
  # print(sum)
  denominator+=2
print("\n",4*sum)


  
