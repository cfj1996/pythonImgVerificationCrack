import queue
import threading
import time
import openScver
import pymysql
from datetime import datetime


exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, name, q):
        self.connection = pymysql.connect(host='localhost',port=3307,user='root',password='root',db='cnblogs',charset='utf8')
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q, self.connection)
        self.connection.close()
        print ("退出线程：" + self.name)

def process_data(threadName,q, db):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()            
            dataList = openScver.init("https://zzk.cnblogs.com/s/blogpost?Keywords=前端面试题&pageindex=" + str(data))
            print('数据长度', len(dataList))
            if(len(dataList)):
                try:
                    cursor = db.cursor()
                    cursor.executemany('INSERT INTO `url` (`uuid`, `url`, `creator_time`) VALUES (%s,%s, %s)',dataList)
                    db.commit()
                    print('写入成功')
                except:
                    db.rollback()
        else:
            queueLock.release()
threadList=[]
for i in range(5):
    threadList.append('线程'+str(i+1))
nameList = range(1,51)
queueLock = threading.Lock()
workQueue = queue.Queue()

threads = []

# 创建新线程
for tName in threadList:
    thread = myThread(tName, workQueue)
    thread.start()
    threads.append(thread)

# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()

# 等待队列清空
while not workQueue.empty():
    pass

# 通知线程是时候退出
exitFlag = 1
# 等待所有线程完成
for t in threads:
    t.join()

print ("退出主线程")