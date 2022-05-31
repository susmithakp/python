n= int(input("enter a range to print prime numbers"))
#count =0
print("Prime numbers:",end=' ')
for j in range (1, n+1):
    for i in range (2,j):
        if (j%i ==0):
            #count =count+1
            #print(count)
            #print ("The given numberis not a prime number")
            break
    else:
        print(j,end = ' ')






    

