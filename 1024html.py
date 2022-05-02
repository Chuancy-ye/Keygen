import json
import chaojiying
import requests
from bs4 import BeautifulSoup
from datetime import datetime
# import sched
import time
import sys
headers_login = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",

}
url_info = "https://cl.7296y.xyz/require/codeimg.php?%27+Math.random()"
s=requests.session()
def get_soup(r):
    r.raise_for_status()  # 检验http状态码是否为200
    r.encoding = r.apparent_encoding  # 识别页面正确编码
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def yanzheng(reginvcode,code):

    data1={
        'reginvcode': reginvcode,
        'validate': code,
        'action': 'reginvcodeck'
    }
    url_post = "https://cl.7296y.xyz/register.php?"
    r = s.post(url_post,headers=headers_login,data=data1)
    soup = get_soup(r)
    soup=str(soup).split('(')
    soup=soup[1].split(")")


    return soup[0]

def download_img(url_info):
    if url_info:
        print("正在下载图片")
        # 这是一个图片的url
        try:
            url = url_info
            response = s.get(url)
            # 获取的文本实际上是图片的二进制文本
            img = response.content
            # 将他拷贝到本地文件 w 写  b 二进制  wb代表写入二进制文本
            #保存路径
            path='%s.jpg' % ('codeimg')
            with open(path, 'wb') as f:
                f.write(img)
        except Exception as ex:
            print("--------出错继续----")
            pass


def start(i,j):
    download_img(url_info)
    code = chaojiying.main()
    vildcode=code.get('pic_str')
    # num=input()
    # num=num.split(' ')
    # i=num[0]
    # j=num[1]
    raw="7bb1eafd9"+str(i)+"87bd4"+str(j)
    reginvcode=raw
    soup=yanzheng(reginvcode,vildcode)
    print(raw,"and",vildcode)
    if soup == "'"+str(2)+"'":
        id=code.get('pic_id')
        chaojiying.report(id)
    return soup

if __name__ == '__main__':
    for i in range(4,7):
        for j in range(0,10):


             re=start(i,j)
             # re = start()
             print(re)
             while re == "'"+str(2)+"'":
                 print('验证码错误')
                 time.sleep(2)
                 re = start(i,j)
             if re == "'"+str(1)+"'":
                 print('错误下一个')
                 time.sleep(2)
             else:
                 print(i,j,'成功@@@@@@@@@@@@@@@@@@@@@@@@')
                 sys.exit()



