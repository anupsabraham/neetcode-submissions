class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)

        longest = 0

        for n in nums:
            if not hashmap[n]:
                hashmap[n] = hashmap[n-1] + hashmap[n+1] + 1

                # update edges
                hashmap[n-hashmap[n-1]] = hashmap[n]
                hashmap[n+hashmap[n+1]] = hashmap[n]

                longest = max(longest, hashmap[n])
        
        return longest