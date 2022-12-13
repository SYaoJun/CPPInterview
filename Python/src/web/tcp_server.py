import socket
if __name__ == '__main__':
    tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
    tcpSocket.bind(("", 8080))  # 元组
    tcpSocket.listen(128)  # 监听上限 在windows 128有效 在linux无效
    newSocket, ipPort = tcpSocket.accept()  # 阻塞等待客户端连接 ipPort是个元组只有两个元素
    print(ipPort[0])  # IP
    print(ipPort[1])  # port
    while True:
        recvData = newSocket.recv(1024)
        # 当接收到数据为空的时候，表示客户端已经断开连接了
        if recvData:
            print(recvData.decode("GBK"))
            user_input = input()
            newSocket.send(user_input.encode("GBK"))
        else:
            print("客户端断开连接！")
            newSocket.close()
            break
    tcpSocket.close()
