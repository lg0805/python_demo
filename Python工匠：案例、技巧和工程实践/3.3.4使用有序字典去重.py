# @FileName : 3.3.4使用有序字典去重
# @Time     : 2022/12/4 10:59
# @Author   : ligg

nums = [10, 2, 3, 21, 10, 3, 11]
# 去重但丢失了顺序
# print(set(nums))
# {3, 10, 2, 21}


# OrderedDict 同时满足两个条件：
# 1.它的键是有序的
# 2.它的键不会复复
from collections import OrderedDict
print(list(OrderedDict.fromkeys(nums).keys()))
# [10, 2, 3, 21, 11]


# dict() 去重并保留顺序
print(list({num: 0 for num in nums}.keys()))
# [10, 2, 3, 21, 11]
３