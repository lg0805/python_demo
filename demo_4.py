"""
功能介绍     ：
@Author     : liguang
@Date       : 2022/11/2 20:54
"""


def check_index(key):
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}

    def __setitem__(self, key, value):
        """修改字典中的元素"""
        check_index(key)
        self.changed[key] = value

    def __getitem__(self, key):
        check_index(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step


s = ArithmeticSequence(1, 2)
