from collections import Counter,defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #Brute force: 
    

        d=Counter(words)                
        
        freq_set = set(list(d.values()))    
        freq_d=defaultdict(list)
        for f in freq_set:
            for key in d:
                if d[key]==f:
                    freq_d[f]=freq_d[f]+[key]
        final_list=[]
        for key in sorted(freq_d,reverse=True): #.items():
                value=sorted(freq_d[key])
                for i in value:
                    if len(final_list)<k:
                        final_list.append(i)
        
        return final_list[:k]
