# @FileName : 3.3.5别在遍历列表时同步修改
# @Time     : 2022/12/4 11:31
# @Author   : ligg

numbers = [1, 2, 7, 4, 8, 11]

# def remove_even(numbers: list):
#     """去除列表里所有的偶数"""
#     for number in numbers:
#         if number % 2 == 0:
#             # 有问题的代码
#             numbers.remove(number)

# remove_even(numbers)
# print(numbers)
# [1, 7, 8, 11]


# 启用新列表保存修改后的成员
def remove_even(numbers: list):
    """去除列表里所有的偶数"""
    result = []
    for number in numbers:
        if number % 2 == 0:
            continue
        result.append(number)
    return result


print(remove_even(numbers))
# [1, 7, 11]
