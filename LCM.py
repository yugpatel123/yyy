a = int(input("Enter 1st No:"))
b = int(input("Enter 2nd No:"))

if(a>b):
    max = a
else:
    max = b

while(1):
    if(max%a==0 and max%b==0):
        print(max)
        break
    max = max + 1