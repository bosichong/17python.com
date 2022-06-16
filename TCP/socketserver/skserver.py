import socketserver
from time import ctime

class MySocketServer(socketserver.BaseRequestHandler):
    '''请求处理程序'''
    def handle(self):
        '''重写处理socket连接的方法'''
        print(self.request)
        print(self.server)
        print(self.client_address)
        while True:
            self.data = self.request.recv(1024).decode().strip()
            print(self.data)
            self.request.sendall("{}:{}".format(ctime(),self.data.upper()).encode('utf-8'))
            if self.data == 'serverexit':
                self.request.sendall("服务器已关闭".encode('utf-8'))
                break
        self.request.close()


if __name__ == '__main__':
    HOST,PORT = "127.0.0.1",8888
    #通过socketserver及自定义的requesthandler创建服务器
    server = socketserver.TCPServer((HOST, PORT),MySocketServer)
    server.serve_forever()#启动服务器监听