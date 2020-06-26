a = 15
b = 4
c = 23

if(a<b and a<c):
    print(a,"is the smallest")

elif(b<a and b<c):
    print(b,"is the smallest")

else:
    print(c,"is the smallest" )

for i in range(0,5):
    for j in range(0,i+1):
        print("*", end =" ")
    print("")