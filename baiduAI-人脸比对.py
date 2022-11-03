"""人脸对比"""
import base64

from aip import AipFace

APP_ID = '28223164'
API_KEY = 'GiEBCXDdnFwRpPeeRGdiGTVk'
SECRET_KEY = 'K2jHvXgTzGChiUMG3TOPPPEeQ6zxFP5A'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

result = client.match([
    {
        'image': base64.b64encode(open('p_11.png', 'rb').read()).decode(),
        'image_type': 'BASE64',
    },
    {
        'image': base64.b64encode(open('p_12.png', 'rb').read()).decode(),
        'image_type': 'BASE64',
    }
])

res = result['result']['score']
if res < 50:
    print('相似度', int(res), '%, 不同能是同一个人')
elif res < 85:
    print('相似度', int(res), '%, 有可能是同一个人')
elif res >= 85:
    print('相似度', int(res), '%, 同一个人的可能性极高')


