# -*- coding: unicode-escape -*-
import json
import Crawler
import threading

def main(num):
    #使用了多线程爬取,因为爬出来的题库是一个页码一个json文件,所以干脆一个json文件一个线程
    threads = []
    t1 = threading.Thread(target = CrawlerByDifficult,args=(num,0))
    threads.append(t1)
    t2 = threading.Thread(target = CrawlerByDifficult,args=(num,1))
    threads.append(t2)
    t3 = threading.Thread(target = CrawlerByDifficult,args=(num,2))
    threads.append(t3)
    t4 = threading.Thread(target = CrawlerByDifficult,args=(num,3))
    threads.append(t4)
    t5 = threading.Thread(target = CrawlerByDifficult,args=(num,4))
    threads.append(t5)
    t6 = threading.Thread(target = CrawlerByDifficult,args=(num,5))
    threads.append(t6)
    t7 = threading.Thread(target = CrawlerByDifficult,args=(num,6))
    threads.append(t7)
    t8 = threading.Thread(target = CrawlerByDifficult,args=(num,7))
    threads.append(t8)
    t9 = threading.Thread(target = CrawlerByDifficult,args=(num,8))
    threads.append(t9)
    t10 = threading.Thread(target = CrawlerByDifficult,args=(num,9))
    threads.append(t10)
    for t in threads:
         t.start()
    #CrawlerByDifficult(num,1)



def CrawlerByDifficult(difficult,JIndex):
    filename = 'Json\\content'+str(JIndex)+'.json'
    with open(filename,encoding='utf-8') as file:
        jsonData = json.load(file)
        print(type(jsonData))
    for i in range(50):
        #print(jsonData["currentData"]["problems"]["result"])
        if(jsonData["currentData"]["problems"]["result"][i]["difficulty"] == difficult):
             PID = jsonData["currentData"]["problems"]["result"][i]["pid"]
             PID = str(PID).removeprefix("P")
             ID = int(PID)
             print(type(ID))
             Crawler.main(PID,difficult)
        #print(jsonData["tags"][0]["type"])

if __name__ == '__main__':
    main(1)