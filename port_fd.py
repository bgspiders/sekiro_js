# coding=utf-8
import socket,threading,redis,json
#redis的配置
redisconn = redis.Redis(host='127.0.0.1', port=6379, db=1, password='1010')
#获取代理
def proxise():
    # 从redis读取爬虫代理的ip地址
    prox_ = json.loads(redisconn.get("ip"))['http'].replace('http://','').split(':')
    ip={'ip':prox_[0],'port':prox_[1]}
    print(ip)
    return ip
#代理服务器的ip。没有端口号！！！9
def source_host():
    #返回的是一个字符串
    return str(proxise()['ip'])
# 端口号！！！
def source_port():
    # 返回的是一个整数 Int类型
    return int(proxise()['port'])
#需要转发的ip地址，一般是本地
desc_host = '127.0.0.1'
#需要转发的端口
desc_port = 8099

#发送tcp请求的方法
def send(sender, recver):
    while 1:
        try:
            #接受数据
            data = sender.recv(4096)
        except:
            print("recv error")
            break
        try:
            # 发送数据
            recver.sendall(data)
        except:
            print("send error")
            break
    #关闭端口
    sender.close()
    recver.close()
def proxy(client):
    #创建对象
    # socket.AF_INET 是服务器于服务器直接的连接，SOCK_STREAM是基于tcp流
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 连接的ip和端口号 source_host()每次都是读取新的代理Ip redis提供了可靠的并发
    server.connect((source_host(), source_port()))
    # 开启一个线程
    threading.Thread(target=send, args=(client, server)).start()
    threading.Thread(target=send, args=(server, client)).start()

def main():
    proxy_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 相当于一个缓冲区  SOL_SOCKET 我的理解是正在使用的这个socker目前连接的设置 SO_REUSEADDR是不需要一定等到超时才结束
    proxy_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # bind就是绑定指定的端口号
    proxy_server.bind((desc_host, desc_port))
    #开始tcp监听。backlog指定在拒绝连接之前，可以挂起的最大连接数量。该值至少为1
    proxy_server.listen(50)
    print("Proxying from %s:%s to %s:%s ..."%(source_host(), source_port(), desc_host, desc_port))
    while True:
        # 被动接受TCP客户端连接, (阻塞式)等待连接的到来
        conn,addr = proxy_server.accept()
        print("received connect from %s:%s"%(addr[0], addr[1]))
        # 创建线程
        threading.Thread(target=proxy, args=(conn, )).start()

if __name__ == '__main__':
    main()