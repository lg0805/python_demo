# @FileName : demo_2.py
# @Time     : 2022/11/1 23:10
# @Author   : ligg
import sys

my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
max_index = len(my_letters)
output_file = sys.argv[1]
filewriter = open(output_file, 'w')
for index_value in range(len(my_letters)):
    if index_value < (max_index - 1):
        filewriter.write(my_letters[index_value] + '\t')
    else:
        filewriter.write(my_letters[index_value] + '\n')
filewriter.close()

