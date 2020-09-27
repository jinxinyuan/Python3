class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        shortest=min(strs, key=len)
        for i in range(0,len(shortest)):
            for j in range(0,len(strs)-1):
                if((strs[j])[i]!=(strs[j+1])[i]):
                    return shortest[0:i]

if __name__ == '__main__':
    a = Solution()
    print(a.longestCommonPrefix(["flower","flow","flight"]))