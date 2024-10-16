class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        answer = 0
        sign = 1
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1

        while i < n and s[i].isdigit():
            answer = answer * 10 + int(s[i])
            if answer * sign <= -2**31:
                return -2**31
            if answer * sign >= 2**31 - 1:
                return 2**31 - 1
            i += 1

        return answer * sign
