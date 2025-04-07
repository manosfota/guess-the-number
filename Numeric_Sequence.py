#n, a1, d

# --------Geometric Sequence--------
n=int(input('\n\nΜέχρι ποιο όρο της ακολουθίας θέλετε να υπολογίσετε: '))
d=int(input('Δωστε το βημα της ακολουθιας: '))
a_1=int(input('Δωστε τον πρώτο όρο της ακολουθιας: '))
sum=a_1
print(a_1, end=' ')
for i in range(0, n-1):  
  a_n= sum + d
  sum=a_n
  print(a_n, end=' ')

# 1 5 25 125 625...








