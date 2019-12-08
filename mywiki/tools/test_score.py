from threading import Thread
import random ,requests


# 向8000或8001服务器发起1个请求
def get_request():
    url1='http://127.0.0.8000/test_cors'
    url2 ='http://127.0.0.8001/test_cors'
    url=random.choice([url1, url2])
    # 发请求- 相当于在浏览器地址栏输入URL敲回车动作
    requests.get(url)

