#find whether the given number id palindrome or not
class solution:
    def Palindrome(self):
        num = int(input())
        print(num)
        rev=0
        original = num
        while num > 0:
            n = num % 10
            num =num // 10
            rev = rev *10 + n
            print(rev)
        if original == rev:
            print("The given number", original , " is a palindrome")
        else:
            print("The given number", original , " is not a palindrome")

obj1 = solution()
obj1.Palindrome()



        