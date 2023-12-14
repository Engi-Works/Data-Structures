class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        nums.sort()
        count = 1
        answer = dict()

        for i in range(0 , len(nums) - 1):
            
            if nums[i] == nums[i+1]:
                count += 1
            
            elif nums[i] != nums[i+1]:
                    answer[nums[i]] = count
                    count = 1
            
            if k < len(answer):
                for key , value in dict(answer).items():
                    if value == min(answer.values()):
                        del answer[key]
                        continue
            
        
        ansList = list(answer.keys())
        return ansList
        
#Test
array = [1 , 2 , 3 , 1 , 4 , 2 , 1]

myObj = Solution()

print(myObj.topKFrequent(array , 3))
