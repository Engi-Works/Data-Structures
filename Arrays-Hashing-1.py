
class Solution:
    
    def containsDuplicate(self, nums: list[int]) ->bool:
        x,y = 0 , 1
        nums.sort()
        for y in range(1,len(nums)):
            if nums[x] == nums[y]:
                return True
            y +=1
            x +=1

        return False
     
  
        
        
            
#test = [1,2,3,4,2] 
test =[0]

L1 = Solution()

print(L1.containsDuplicate(test))
