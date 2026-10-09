class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=""
        for i in s:
            if i.isalnum():
                a+=i

        if a[::-1].lower()==a.lower():
            return True
        else:
            return False
