cake_angle = 360
n = int(input("Enter n: "))


if(cake_angle%n==0):
    print("Yes the cake can be cut into equal pieces of angle %d"%(360/n))
else:
    print("NO the cake can't be cut into equal pieces of size %d"%n)


if(n>cake_angle):
    print("NO the cake cannot be cut in %d pieces of any size."%n)
else:
    print("YES the cake will cut in %d pieces of size."%n)

n=1
for i in range(n):
    cake_angle-=n
    n+=1
    if(cake_angle<0):
        print("No the cake will not cut into %d pieces such that no two of them are equal"%n)
        break
else:
        print("YES the cake will cut into %d pieces such that no two of them are equal"%n)
