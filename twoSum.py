class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = []
        for i in range(len(nums)):
            if len(L)==2:
                return L
            complement = target - nums[i]
            if complement in nums and complement!=nums[i]: 
                           
                L.append(i)
                L.append(nums.index(complement))
                return L
        
            if complement in nums and complement==nums[i] and complement in nums[i+1:]:
                   
                    L.append(i) 
                    j=i+1
                    while(j<len(nums)):
                        if nums[j]==complement:
                            
                            L.append(j)
                            return L
                        j=j+1
                    
               
