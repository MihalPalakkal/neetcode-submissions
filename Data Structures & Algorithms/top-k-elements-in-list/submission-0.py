class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        
        for num in nums:
            if num in dic:
                dic[num]+=1
            else:
                dic[num]=1

        d=dict(sorted(dic.items(), key=lambda x:x[1], reverse=True))
        
        res=[]
        for key in d:
            res.append(key)
            if len(res)==k:
                break

        return res