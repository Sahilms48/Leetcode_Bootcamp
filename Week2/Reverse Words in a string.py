class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0
        j = len(s) - 1
        answer = ""

        
        while i < j and s[j] == " ":
            j = j - 1

        while i < j and s[i] == " ":
            i = i + 1

        k = j
        while k >= i:
            temp = 0

            if s[k] != " ":
                while k >= i and s[k] != " ":
                    temp = temp + 1
                    k = k - 1

                answer = answer + (s[k + 1 : k + temp + 1]) + " "

            while k >= i and s[k] == " ":
                k = k - 1

        return answer[0 : len(answer) - 1]
        
