"""""
13.
罗马数字转整数
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符 I， V， X， L，C，D 和 M
数值1,5,10,50,100,500,1000

例如， 罗马数字
2
写做
II ，即为两个并列的
1。12
写做
XII ，即为
X + II 。 27
写做
XXVII, 即为
XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如
4不写做IIII，而是IV。
数字1在数字5的左边，所表示的数等于大数5减小数1得到的数值4 。

同样地，数字9表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5)和X(10)的左边，来表示4和9。
X可以放在L(50)和C(100)的左边，来表示40和90。
C可以放在D(500)和M(1000)的左边，来表示400和900。

给定一个罗马数字，将其转换成整数。输入确保在1到3999的范围内。

示例1:
输入: "III"
输出: 3

示例2:
输入: "IV"
输出: 4

示例3:
输入: "IX"
输出: 9

示例4:
输入: "LVIII"
输出: 58
解释: L = 50, V = 5, III = 3.

示例5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.

提示：
题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
IC和IM这样的例子并不符合题目要求，49应该写作XLIX，999应该写作CMXCIX 。

关于罗马数字的详尽书写规则，可以参考
罗马数字 - Mathematics 。
"""""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        svalue={"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result=0
        lenth=len(s)

        for i in range(0, lenth):
            #防止下标越界
            if(i<lenth-1):
                if(svalue[s[i]]>=svalue[s[i+1]]):
                    result+=svalue[s[i]]
                else:
                    result -= svalue[s[i]]
            else:
                result+=svalue[s[i]];
        return result



if __name__ == '__main__':
    a = Solution()
    print(a.romanToInt("IV"))