#adding two elements in an array to get a sum s.
class solution:
    def SubArray(self,array,n,s):
        final_array = []
        for i in range(len(array)):
            final_array = [array[i]] 
            sum = 0
            print(final_array)
            #print(array[i])
            for j in range(i+1,len(array)):
                sum = array[i] + array[j]
                final_array.append(array[j])
                print(final_array)
                if(sum == s):
                    print ("sumis ", sum )
                    return [i,j]
sub_array = solution()
array_sum = sub_array.SubArray([1,2,38,9,7,24,8],7,46)
print(array_sum)


