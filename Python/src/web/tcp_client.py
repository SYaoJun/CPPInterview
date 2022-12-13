import socket
if __name__ == '__main__':
    address = '127.0.0.1'  # 监听哪些网络127.0.0.1是监听本机 0.0.0.0是监听整个网络
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
    # tcpSocket.bind(("",12345)) #元组
    tcpSocket.connect((address, 8080))
    tcpSocket.send('约吗？'.encode("GBK"))  # 已经建立了连接 直接发送
    recvData = tcpSocket.recv(1024)
    print(recvData.decode("GBK"))
    tcpSocket.close()
