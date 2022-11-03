"""
功能介绍     ：带访问计数器的列表
@Author     : liguang
@Date       : 2022/11/2 21:44
"""


class CounterList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.counter = 0

    def __getitem__(self, index):
        self.counter += 1
        return super().__getitem__(index)
