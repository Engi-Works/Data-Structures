class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        
        mapList = dict()
        
        for i in nums:
            if i not in mapList.keys():
                mapList.update({i : 0})
                
            elif i in mapList.keys():
                val = mapList.get(i) + 1
                mapList.update({ i : val })
                
        count = 1
        ansList = list()
        for key,value  in sorted(mapList.items() , key=lambda item:item[1] , reverse=True):
            ansList.append(key)
            count += 1
            if count > k:
                break
            
        
        return ansList
