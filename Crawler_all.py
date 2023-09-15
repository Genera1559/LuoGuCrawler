import re
import requests
import bs4
import urllib.parse


baseUrl = "https://www.luogu.com.cn/problem"
savePath = "D:\\Database\\1261640141\\FileRecv\\Term3\\软件工程\\洛谷爬虫\\洛谷题库\\"
minnum = 1020
maxnum = 1080

def main():
    crawler(minnum,maxnum)

def crawler(minnum,maxnum):
    
    print("准备爬取P{}".format(maxnum))
    for i in range(minnum,maxnum+1):
        print("正在爬取P{}...".format(i),end="")
        r = getProblemHTML(baseUrl +"/P" +str(i))
        if str(r).find("200") != 11:
            print("爬取失败,HTTP:" + str(r))
        else:
            title = getTitle(r.text)
            problemMD = getProblemMD(r.text)
            print("爬取成功！正在保存...",end="")
            saveData(problemMD,"P"+str(i)+"-"+str(title) +".md")
            print("题目保存成功!")
        r = getSolutionHTML(baseUrl +"/solution/P"+ str(i))
        if str(r).find("200") != 11:
            print("爬取失败,HTTP:" + str(r))
        else:
            #title = getTitle(r.text)
            problemMD = getSolutionMD(r.text)
            print("爬取成功！正在保存...",end="")
            #print("保存路径"+str(title)+"\\"+"P"+str(i)+"-"+str(title)+ "-题解" +".md")
            saveData(problemMD,"P"+str(i)+"-"+str(title)+ "-题解" +".md")
            print("解答保存成功!")
    print("爬取完毕")
    return 0

def getProblemHTML(url):
    #伪装自己是浏览器
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76"
    }
    r = requests.get(url = url,headers = headers)
    r.encoding = 'utf-8'
    if str(r).find("200") == 11:#正确返回的话状态码为200
        return r
    elif(str(r).find("302") == 11):
        return "302"
    elif(str(r).find("403") == 11):
        return "403"
    else:
        return "未知错误"
    

def getSolutionHTML(url):
    #不知道具体需要哪些头字段所以直接全写了
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
    #r.encoding = 'ISO-8859-1'
    #r.encoding = 'unicode_escape'
    #print(str(r.text))
    if str(r).find("200") == 11:#正确返回的话状态码为200
        return r
    elif(str(r).find("302") == 11):
        return "302"
    elif(str(r).find("403") == 11):
        return "403"
    else:
        return "未知错误"
def getTitle(text):
    bs = bs4.BeautifulSoup(text,"html.parser")
    #通过<h1>标签确定标题位置
    try:
        text = bs.select("h1")[0]
    except:
        print(str(text))
        text = bs.select("h3")[0]
    print(str(text))
    #剪切字符串
    title = str(text).removeprefix("<h1>")
    title = title.removesuffix("</h1>")
    return title

def getProblemMD(text):
    bs = bs4.BeautifulSoup(text,"html.parser")
    core = bs.select("article")[0]
    md = str(core)
    md = re.sub("<h1>","# ",md)
    md = re.sub("<h2>","## ",md)
    md = re.sub("<h3>","#### ",md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

def getSolutionMD(text):
    #解码
    text = str(urllib.parse.unquote(text,encoding ='unicode_escape'))
                                                #re.S 将整个字符串视为一个整体
    core = re.findall('decodeURIComponent\("\{"code":200,"currentTemplate":"ProblemSolution","currentData":\{"solutions":\{"result":\[\{"content":"(.*?)\)\)', text,re.S)[0]
    #bs = bs4.BeautifulSoup(text,"html.parser")
    #core = bs.select("script")[0]
    #core = bs.find("script")
    md = str(core)
    print(md)
    #text = str(urllib.parse.unquote(text,encoding ='unicode_escape'))
    
    #md = re.findall('decodeURIComponent(.*?)', text)[0]
    print(str(core))
    md = re.sub("<h1>","# ",md)
    md = re.sub("<h2>","## ",md)
    md = re.sub("<h3>","#### ",md)
    md = re.sub("</?[a-zA-Z]+[^<>]*>","",md)
    return md

def saveData(data,filename):
    cfilename = savePath + filename
    file = open(cfilename,"a",encoding="utf-8")
    for d in data:
        file.writelines(d)
    file.close()

if __name__ == '__main__':
    main()


