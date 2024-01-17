s = input("Enter string to be reversed: ")

#TC=O(n) SC=O(1)  Extended Slicing
rev_str = s[::-1]

#TC=O(n) SC=O(1)   For Loop
rev_str = ""
for ch in s:
    rev_str = ch + rev_str

#TC=O(n) SC=O(n)   Stack(LIFO)
stack = []
for ch in s:
    stack.append(ch)
rev_str = ""
while len(stack)!=0:
    rev_str = rev_str + stack.pop()

#TC=O(n) SC=O(n)   Reversed Method
rev_str = "".join(reversed(s))

#TC=O(n) SC=O(1)   Convert into List & Reverse List
lst = list(s)
lst.reverse()
rev_str = "".join(lst)

#TC=O(n) SC=O(1)   List Comprehension
lst = [ s[i] for i in range(len(s)-1, -1, -1)] 
rev_str = "".join(lst)

print(rev_str)