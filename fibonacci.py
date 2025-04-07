

n=int(input('\n\nΜέχρι ποιο όρο της ακολουθίας Fibonacci θέλετε να υπολογίσετε: '))

fib_1=1
fib_2=1
print("Οι όροι της ακολουθίας fibonacci είναι: \n" + str(fib_1) + " " + str(fib_2), end=' ')
for i in range(0,n-2):
  fib_new=fib_1+fib_2
  fib_2=fib_1
  fib_1=fib_new
  # print(fib_new, end=' ')
  print(fib_1/fib_2)



# 1 6 11 16 21 26 

# fib_first=1
# fib_second=1
# n=int(input('\n'))
# for i in range(1,n):
#   fib_new=fib_first+fib_second
#   print(fib_new)
#   fib_sec=fib_new
#   fib_first=fib_sec