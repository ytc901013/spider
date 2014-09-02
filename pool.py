# !/usr/bin/env python  
# -*- coding:utf-8 -*-  
  
import Queue  
import threading  
import time
import traceback
  
class WorkManager(object):  
    def __init__(self, thread_num):
        self.work_queue = Queue.Queue()  
        self.threads = []
        self.mylock = threading.Lock()
        self.__init_thread_pool(thread_num)  

    def __init_thread_pool(self,thread_num):  
        for i in range(thread_num):  
            self.threads.append(Work(self.work_queue, self.mylock))  
 
    def add_job(self, func, *args):  
        self.work_queue.put((func, list(args)))            
  
class Work(threading.Thread):  
    def __init__(self, work_queue, mylock):  
        threading.Thread.__init__(self)  
        self.work_queue = work_queue
        self.mylock = mylock
        self.setDaemon(True)
        self.start()  
  
    def run(self):  
        while True:
            try:
                do, args = self.work_queue.get(block=False)
                do(args)  
                self.work_queue.task_done()
            except Queue.Empty:
               pass
            except:
                traceback.print_exc()
            finally:
                time.sleep(0.001)
