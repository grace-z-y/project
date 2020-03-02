"""
FTP客户端
"""
from socket import *
import sys

ADDR = ('127.0.0.1',8888)

class FTPClient():
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def quit(self):
        self.sockfd.send(b'E')
        self.sockfd.close()
        sys.exit("谢谢使用")
    def list(self):
        pass

    def get(self,filename):
        data = 'G '+ filename
        self.sockfd.send(data.encode())

        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename,'wb')
            while True:
                data = self.sockfd.recv(1024)
                if data == b'##':
                    break
                f.write(data)
            f.close()
        else:
            print(data)

def main():
    s = socket()
    s.connect(ADDR)

    ftp = FTPClient(s)

    while True:
        print("========命令选项========")
        print("***      list       ***")
        print("***    get file     ***")
        print("***    put file     ***")
        print("***      quit       ***")
        print("=======================")
        cmd = input("输入命令：")

        if cmd == 'quit':
            ftp.quit()

if __name__ == '__main__':
    main()


