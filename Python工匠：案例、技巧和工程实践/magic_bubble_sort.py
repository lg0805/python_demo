# @FileName : sort_demo
# @Time     : 2022/11/28 14:07
# @Author   : ligg


from typing import List

numbers = [23, 32, 1, 3, 4, 19, 20, 2, 4]


def magic_bubble_sort(numbers: List[int]):
    """
    有魔力的冒泡排序算法， 默认所有的偶数比奇数大
    :param numbers: 需要排序的列表，函数会直接修改原始列表
    """
    stop_position = len(numbers) - 1
    while stop_position > 0:
        for i in range(stop_position):
            current, next_ = numbers[i], numbers[i + 1]
            current_is_even, next_is_even = current % 2 == 0, next_ % 2 == 0
            should_swap = False
            # 交换位置的两个条件：
            # 1.前面是偶数，后面是奇数
            # 2.前后同为奇数或偶数，但前比后大
            if current_is_even and not next_is_even:
                should_swap = True
            elif current_is_even == next_is_even and current > next_:
                should_swap = True
            if should_swap:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        stop_position -= 1

    return numbers


print(magic_bubble_sort(numbers))
