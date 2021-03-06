from collections import defaultdict
import math as m
class Solution:
    def euklDist(self,x):
       
        v= x[0]**2+x[1]**2
        return m.sqrt(v)



    def kClosest(self, points,k): #: List[List[int]], k: int) -> List[List[int]]:
        #first approach, brute force appending to new list with insertion sort  
        my_dict=defaultdict() #has points as keys

        for i in points: #or the process with some other algo or extra-check
            d = self.euklDist(i)            
            my_dict[tuple(i)]=d 

        my_points=list(my_dict.keys())
        my_distance=list(my_dict.values())
        my_distance_sorted=list(sorted(my_dict.values()))
        print(my_dict)
        def add(i):
            print("my points before:",my_points)
            print("i:",i) #i is distance
            corresponding_point=my_points[my_distance.index(i)]
            print(corresponding_point)
            res = list(corresponding_point)    
            print("point to remove:",corresponding_point)
            my_points.remove(corresponding_point)
            my_distance.remove(i)
            print("my points after:",my_points)
            return res

        result=[add(i) for i in my_distance_sorted[:k]]
 
        return result
    
x= Solution()
#print(x.kClosest([[1,0],[0,-1]],2))
#print(x.kClosest([[3,1],[0,-1]],2))

print(x.kClosest([[3,3],[5,-1],[-2,4]],2))
