#HEMANT GURAV M18
n=int(input("Enter a number:"))
s = 0
t= n
while t > 0:
   d = t % 10
   s=s+digit ** 3
   t //= 10
if n== s:
   print(n," Armstrong number")
else:
   print(n," Not an Armstrong number")