n =1071
for i in range (14):
    if n%2==0:
        n = n//2
    elif n%2 != 0:
        n = (3*n)+1
print (n)
