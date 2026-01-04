n = int(input("enter a number(n>0):"))
n1=0
n2=1
print("Fibonacci series:", n1, n2, end=" ")
for i in range(2, n+1):
    n3 = n1 + n2
    print(n3, end=" ")
    n1 = n2
    n2 = n3
