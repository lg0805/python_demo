"""
功能介绍     ：人脸识别
@Author     : liguang
@Date       : 2022/11/2 13:10
"""
import base64
from aip import AipFace

APP_ID = '28208365'
API_KEY = 'BGMffmzxPIWg6YrQnBrvTv8M'
SECRET_KEY = 'EB6WAiCwthSz4xULvRK1P62SfSCLtCTG'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

image = open('m_5.jpeg', 'rb').read()
base = base64.b64encode(image)          # 将图像文件按BASE64编码
image1 = str(base, encoding='utf-8')    # 
imageType = 'BASE64'                    # 指定图像编码为BASE64

""" 可选参数 """
options = {}
options["face_field"] = "age,beauty"

# 调用人脸识别
result = client.detect(image1, imageType, options)
print('颜值:', result['result']['face_list'][0]['beauty'])
print('年龄:', result['result']['face_list'][0]['age'])
