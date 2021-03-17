k=int(input('enter the number'))
for i in range (2,k):
    if k%i==0:
        print('not prime number')
        break
    else:
        print('primr number')
