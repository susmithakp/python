arr = input("Enter list of integer elements")
num = list(map(int,arr.split(' ')))
#num =[23,45,78,98,65,63,23,12,12]
def search(arr, x):
    for i in range(len(arr)):
        #print(i)
        if arr[i] == x:
            print(i)
            return i
    return -1

a=search(num, 34)
print(a)
