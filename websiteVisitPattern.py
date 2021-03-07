from collections import defaultdict
class Solution:
    website_count=defaultdict(dict)
    def quicksort(self,website,low,high):
        if low<high:
            for i in range(low,high):
                if website[i] not in self.website_count:
                    self.website_count[website[i]]=0
                self.website_count[website[i]]+=1
                if website[i]<website[i+1]:
                                       
                    website[i],website[i+1]=website[i+1],website[i]
                    return self.quicksort(website,low,i)
                return self.quicksort(website,low+1,high)
                                
        return website  
    
    def web_count(self,website,username):
        self.website_count=defaultdict(dict)
        temp=defaultdict(list)
        for w,u in zip(website,username):
            if w not in self.website_count:
                self.website_count[w]={}
                temp[w]=[]
                self.website_count[w]=0
            if u not in temp[w]:
                temp[w].append(u)
                self.website_count[w]+=1
  
        return self.website_count
        
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        #Will first sort websites lexicographically and add in a dictionary with their counts
        #I am thinking of using quicksort
        #list(self.web_count(website).keys())[:3]
        x=self.web_count(website,username)
        print(x)
        res=[i for i in list(x.keys())[:3]]
        print(res)
        res2=[]
        #while len(res2)<=3:
        for web in res:            
                for j in range(x[web]):
                              res2.append(web)
        res3=res2.sort()
        return res2[:3]
        
