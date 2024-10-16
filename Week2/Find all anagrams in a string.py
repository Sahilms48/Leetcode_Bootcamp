class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        result = []
        hashmap = collections.Counter(p)
        left = 0
        right = 0
        n = len(p)
        while right < len(s):
            if hashmap[s[right]] >= 1:
                n -= 1
            hashmap[s[right]] -= 1
            right += 1

            if n == 0:
                result.append(left)
            if right-left==len(p):
                if hashmap[s[left]] >= 0:
                    n += 1
                hashmap[s[left]] += 1
                left += 1

        return result
        
