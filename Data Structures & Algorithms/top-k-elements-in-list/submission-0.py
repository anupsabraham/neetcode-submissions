class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = defaultdict(int)

        for num in nums:
            count[num] += 1
        
        freq = [[] for x in range(len(nums))]

        for num, cnt in count.items():
            freq[cnt-1].append(num)
        
        ret = []
        for f in freq[::-1]:
            for val in f:
                if k > 0:
                    ret.append(val)
                    k -= 1
        
        return ret