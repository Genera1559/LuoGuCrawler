from tkinter import *
from tkinter import filedialog
import CrawlerGetJson
import CrawlerAnalysisJson
import os

def opendir():
    os.system('start' + " 洛谷题库")



window = Tk()
window.title("洛谷爬虫")
window.geometry("500x100")
button1 = Button(window, text="刷新题库",width = 15, height = 1, bg="blue", fg="white",command = CrawlerGetJson.TCGJmain)
button1.grid(column=1, row=1)
button1 = Button(window, text="入门",width = 15, height = 1, bg="red", fg="white",command = lambda: CrawlerAnalysisJson.main(1))
button1.grid(column=1, row=2)
button2 = Button(window, text="普及-",width = 15, height = 1, bg="orange", fg="white",command = lambda: CrawlerAnalysisJson.main(2))
button2.grid(column=2, row=2)
button3 = Button(window, text="普及/提高-", width = 15, height = 1,bg="yellow", fg="black",command = lambda: CrawlerAnalysisJson.main(3))
button3.grid(column=3, row=2)
button4 = Button(window, text="普及+/提高",width = 15, height = 1, bg="green", fg="white",command = lambda: CrawlerAnalysisJson.main(4))
button4.grid(column=4, row=2)
button5 = Button(window, text="提高+/省选-",width = 15, height = 1, bg="blue", fg="white",command = lambda: CrawlerAnalysisJson.main(5))
button5.grid(column=1, row=3)
button6 = Button(window, text="省选/NOI-", width = 15, height = 1,bg="purple", fg="white",command = lambda: CrawlerAnalysisJson.main(6))
button6.grid(column=2, row=3)
button7 = Button(window, text="NOI/NOI+/CTSC",width = 15, height = 1, bg="black", fg="white",command = lambda: CrawlerAnalysisJson.main(7))
button7.grid(column=3, row=3)
button7 = Button(window, text="打开文件所在位置", width = 15, height = 1,bg="blue", fg="white",command = opendir)
button7.grid(column=4, row=3)

window.mainloop()