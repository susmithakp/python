# Find the missing numbers in an array containing 1 to N integers.

class solution:
    def __init__(self):
        print ("finding missing element in an array")
    def MissingNumber(self,array,n):
        #self.array = array
        #self.n = n
        actual_set = [x for x in range (1, n+1)]
        result = list(set(actual_set).difference(set(array)))
        return result
numbers = solution()
missing_elements = numbers.MissingNumber([1,2,3,4,6,8,9,11],11)
print(missing_elements)