x = int(input("Enter Number: "))

def fact(n):
   if(n==0):
       return 1

   elif(n<0):
       print("Enter Positive Value")

   else:
       return n*fact(n-1)

y = fact(x)

print(y)