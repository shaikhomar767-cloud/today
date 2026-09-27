rowsize = int(input("Enter your number of rows"))
if rowsize%2 == 0:
    halfdiamrow = rowsize//2

else:
    halfdiamrow = rowsize // 2+1
space = halfdiamrow-1
    
    #loop for upper part
for i in range(1, halfdiamrow + 1):
    for j in range(1, space+1):
        print(end="#")
    space = space-1
    num = 1

    for j in range(2*i-1):
        print(num,end="")
        
        num = num+1
    print()
for i in range(1,halfdiamrow):
    for j in range(1,space+1):
        print(end="")
    space = space+1
    num+1
    for j in range(1,2*(halfdiamrow-i)):
        print(num,end="")
    num + num+1
    print()