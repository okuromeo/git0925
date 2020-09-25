import requests
import os
import sys
import time
from uuid import uuid4
os.environ['REQUESTS_CA_BUNDLE'] =  os.path.join(os.path.dirname(sys.argv[0]), 'cacert.pem')
# 反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'csrf': 'P4UIPTC7ZP',
    'Cookie': '_ga=GA1.2.1364894297.1598667243; _gid=GA1.2.1281792713.1598667243; _gat=1; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1598667244,1598669362,1598671655; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1598671655; kw_token=P4UIPTC7ZP'
}
def get_music(rid,name):
    # 播放免费的音乐，获取歌曲下载地址
    url = "http://www.kuwo.cn/url?format=mp3&rid={}&response=url&type=convert_url3&br=128kmp3&from=web&t=1598692433232&httpsStatus=1&reqId=f5629320-e9d7-11ea-914e-617e90b58130".format(rid)
    result=requests.get(url,headers=headers).json()
    #获取json格式中的歌曲URL
    music_url = result['url']
    #根据url下载歌曲
    music=requests.get(music_url).content
    #保存歌曲文件到文件夹
    # filename = '酷我音乐'
    # if not os.path.exists():
    #     os.mkdir(filename)
    # with open(r'./{}+{}/{}.mp3'.format(filename,uuid4(), name), "wb+") as f:
    with open(r'kuwoyinyue/{}.mp3'.format(name),"wb+") as f:
        print(f"正在下载 {name} 中")
        f.write(music)
        print(f"歌曲 {name} 已下载完成！！！")
def main():
    singer = input('请输入歌手或者歌名：')
    number = int(input('请输入页数：'))
    for i in range(1,number+1):
        # 根据歌手和页面查找
        # print(i)
        url="http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&httpsStatus=1&reqId=6cf5ca40-f73b-11ea-9516-0140fe00a6fa".format(singer,number)
        #url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&httpsStatus=1&reqId=35c5aee0-e9bd-11ea-8dd8-9b5ad3ca6d89".format(singer,i)
        #结果以字典显示
        response = requests.get(url,headers=headers).json()
        #过滤信息
        data=response["data"]['list']
        #遍历歌曲id与歌名
        for x in data:
            rid=x['rid']
            name=x['name']
            print(rid,name)
            #调用下载函数
            print("酷我音乐下载指南".center(50,'*'))
            print("""
            1, 下载当前歌曲
            2, 我要看下一曲
            3, 重选歌手歌曲
            4, 退出当前系统
            """)
            i=int(input('选择需要的操作:'))
            while True:
                if i==1:
                    get_music(rid,name)
                    break
                elif i==2:
                    # time.sleep(5)
                    break
                elif i==3:
                    main()
                elif i == 4:
                    print("感谢使用".center(50, '*'))
                    exit()
                else:
                    print('你的输入有误，请重新输入')
                    break
try:
    main()
finally:
    time.sleep(20)
