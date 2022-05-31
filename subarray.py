#find a continuous sub-array which adds to a given sum S.
class solution:
    def SubArray(self,array,n,s):
        final_array = []
        for i in range(len(array)):
            final_array = [array[i]] 
            sum = array[i]
            print(final_array)
            #print(array[i])
            for j in range(i+1,len(array)):
                sum = sum + array[j]
                final_array.append(array[j])
                print(final_array)
                if(sum == s):
                    print ("sumis ", sum )
                    #return [i,j]
                    return final_array
sub_array = solution()
array_sum = sub_array.SubArray([1,2,38,9,7,24,8],7,54)
print(array_sum)




