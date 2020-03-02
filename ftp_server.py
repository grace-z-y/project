"""
FTP文件处理
多线程并发和套接字联系
"""

from socket import *
from threading import Thread

HOST = '0,0,0,0'
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端请求
class FTPSever(Thread):
    def __init__(self, connfd):
        super().__init__()
        self.connfd = connfd

        #循环接收请求，分发任务
        def run(self):
            while True:
                data = self.connfd.recv(1024).decode()
                if not data or data=='E':
                    return

# 框架结构，启动函数
def main():
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    print("listen the port 8888")


    while True:
        c,addr = s.accept()
        print("connect from:",addr)

        t = FTPSever(c)
        t.setDaemon(True)
        t.start()

    s.close()

if __name__ == '__main__':
    main()

