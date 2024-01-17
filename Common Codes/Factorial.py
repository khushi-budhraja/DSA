n = int(input("Enter the number for its factorial: "))

#Using For Loop
factorial = 1
for i in range(n,0,-1):
    factorial *= i
print(factorial)

#With Recursion
def factorial(n):
    if n<=1:
        return 1
    return n * factorial(n-1)
print(factorial(n))