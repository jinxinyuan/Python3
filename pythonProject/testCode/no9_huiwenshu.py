import main


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
                return 1==0

        return 1==1

if __name__ == '__main__':
    print(Solution.isPalindrome(main,12321))
