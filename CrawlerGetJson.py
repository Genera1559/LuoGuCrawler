import requests
import bs4
import re
import json
import urllib.parse
import threading

baseUrl = "https://www.luogu.com.cn/problem/list?ProblemListParams&page="

def requestToLuogu(url):
    headers = {
        "authority":"www.luogu.com.cn",
        "method":"GET",
        "path":"/problem/P8000",
        "scheme":"https",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Cookie":"__client_id=a9a7f6dc9a1733e681d82f395f7d12d740413ff7; _uid=1088102; C3VK=195332",
        "Referer":"https://www.luogu.com.cn/",
        #"Sec-Ch-Ua":"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"
        #Sec-Ch-Ua-Mobile:?0
        #Sec-Ch-Ua-Platform:"Windows"
        #Sec-Fetch-Dest:document
        #Sec-Fetch-Mode:navigate
        #Sec-Fetch-Site:same-origin
        #Sec-Fetch-User:?1
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
    }
    r = requests.get(url = url,headers = headers)
    #用Unicode格式解码
    #r.encoding = 'unicode_escape'
    return r

def analysis(text):
    text = str(urllib.parse.unquote(text,encoding ='unicode_escape'))
    #bs = bs4.BeautifulSoup(text,"html.parser")
    #core = bs.find("script")
    #print(text)
    core = re.findall('decodeURIComponent\("(.*?)"\)\)', text)[0]
    print(str(core))
    return core
    
def save(soup,i):
    content = str(soup)
    cfilename = "Json\\content"+str(i)+".json"
    content = content.replace('\\', '\\\\')
    #json.loads(content)
    file = open(cfilename,"w",encoding="utf-8")
    
    for d in content:
        file.writelines(d)
    file.close()

def CGJmain(JIndex):
        r = requestToLuogu(baseUrl+str(JIndex))
        soup = analysis(r.text)
        save(soup,JIndex)
def TCGJmain():
    threads = []
    t1 = threading.Thread(target = CGJmain,args=(0,))
    threads.append(t1)
    t2 = threading.Thread(target = CGJmain,args=(1,))
    threads.append(t2)
    t3 = threading.Thread(target = CGJmain,args=(2,))
    threads.append(t3)
    t4 = threading.Thread(target = CGJmain,args=(3,))
    threads.append(t4)
    t5 = threading.Thread(target = CGJmain,args=(4,))
    threads.append(t5)
    t6 = threading.Thread(target = CGJmain,args=(5,))
    threads.append(t6)
    t7 = threading.Thread(target = CGJmain,args=(6,))
    threads.append(t7)
    t8 = threading.Thread(target = CGJmain,args=(7,))
    threads.append(t8)
    t9 = threading.Thread(target = CGJmain,args=(8,))
    threads.append(t9)
    t10 = threading.Thread(target = CGJmain,args=(9,))
    threads.append(t10)
    for t in threads:
         t.start()

