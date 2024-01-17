n = int(input("Enter range: "))

#To display fibonacci series
n1 = 0
n2 = 1
print(n1,n2,end=" ")
for i in range(n-2):
    add = n1+n2
    print(add,end=" ")
    n1,n2 = n2, add

#To display nth fibonacci number
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(n-1))