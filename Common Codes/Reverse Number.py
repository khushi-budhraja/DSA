n = int(input("Enter number to be reversed: "))

rev_num = 0
while n > 0:
    rem = n%10
    rev_num = 10*rev_num + rem
    n = n//10
print(rev_num)