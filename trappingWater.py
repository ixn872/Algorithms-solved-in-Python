class Solution:
    def trap(self, height: List[int]) -> int:
     
        water =0
        n = len(height)
           
        if n==0:
            return 0
        left_max=[0 for i in range(n)]
        right_max=[0 for i in range(n)]
        left_max[0]=height[0]
        for i in range(1,n):
            left_max[i]=max(height[i],left_max[i-1])
        right_max[n-1]=height[n-1]
        for i in range(n-2,0,-1):
            right_max[i]=max(height[i],right_max[i+1])
        for i in range(1,n):
            water+=min(left_max[i],right_max[i]) - height[i]
        return water
