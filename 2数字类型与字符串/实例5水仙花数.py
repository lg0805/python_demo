"""
判断水仙花数。
如： 153（1 ** 3 + 5 ** 3 + 3 ** 3 ＝ 1 + 125 + 27 ＝ 153）
千位：123 // 100
百位：123 // 10 % 10
个位：123 % 10

请输入一个三个数：1.34
您输入的数字不合法！
请输入一个三个数：123
123不是水仙花数！
请输入一个三个数：153
153是水仙花数！
"""
res = 0
num = input('请输入一个三个数：')
if num.isnumeric():
    for n in num:
        res += int(n) ** 3
    if int(num) == res:
        print("{}是水仙花数！".format(num))
    else:
        print("{}不是水仙花数！".format(num))
else:
    print("您输入的数字{}不合法！".format(num))





