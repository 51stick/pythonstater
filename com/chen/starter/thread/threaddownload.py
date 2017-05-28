import threading
import requests
import os


# 线程代码
class TaskThread(threading.Thread):
    """HHH"""

    def __init__(self, name):
        threading.Thread.__init__(self, name=name)

    def run(self):
        print('thread %s is running to downloan contract' % self.getName())

        url = 'https://www.bestsign.cn/openpage/contractDownload.page?mid=ac3219a6e9664206a39894bd31b7762f&fsdid=1493792227436LLDL2&status=3&sign=IuiVpv0vnPKjX9EFYVvTrB%2F6LGCS%2B0bvMHV52JF9RSjBwlkEjF2df7jiINxRS%2FbkDlD6zmNl2pQM8uZaYCWrvydtIan4yKeYutiILU83VZceFJYg9AEEgKXGDYzidj1YaaM%2BABYW9EFn12frN9qwwQo1UjJadMZyncu%2FnTT0Ops%3D'
        path = "H:\pythondownload\contract"

        if not os.path.exists(path):
            os.makedirs(path)

        for i in range(6):
            file_name = path + "\contract2017050_%s.zip" % i
            print('thread %s is begin to downloan contrat %s' % (self.getName(), file_name))
            r = requests.get(url)
            with open(file_name, "wb") as code:
                code.write(r.content)

            print('thread %s downloan contrat %s successed' % (self.getName(), file_name))
        print('thread %s finished to download contract.' % self.getName())

taskthread = TaskThread('TaskThread')
taskthread.start()
taskthread.join()
