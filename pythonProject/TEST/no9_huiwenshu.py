

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        a=str(x)
        lenth=len(a)
        lenth2=lenth//2
        for i in range(0,lenth2):
            if(a[i]==a[lenth-1]):
                lenth-=1
            else:
                return False

        return True

if __name__ == '__main__':
    a = Solution()
    print(a.isPalindrome(12321))
