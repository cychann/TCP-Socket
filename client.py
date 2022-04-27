from socket import *

serverName = '192.168.0.6'
serverPort = 12345

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

while True:
    input_msg = input('msg:')

    # end 명령어를 치면 소켓 통신 종료
    if input_msg == "end":
        break
    if input_msg == "GET":
        request_message = 'GET / HTTP/1.1\r\nHost: 192.168.0.6:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n'
    elif input_msg == "POST":
        request_message = 'POST / HTTP/1.1\r\nHost: 192.168.0.6:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\nContent-Length: 0\r\n\r\n'
    elif input_msg == "HEAD":
        request_message = 'HEAD / HTTP/1.1\r\nHost: 192.168.0.6:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n'
    elif input_msg == "PUT":
        request_message = 'PUT / HTTP/1.1\r\nHost: 192.168.0.6:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\nContent-Length: 0\r\n\r\n'
    elif input_msg == "DELETE":
        request_message = 'DELETE / HTTP/1.1\r\nHost: 192.168.0.6:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n'
    else:
        request_message = 'NotAllowed / HTTP/1.1\r\nHost: 192.168.0.6:12345\r\nUser-Agent: insomnia/2022.2.1\r\nAccept: */*\r\n\r\n'
    clientSocket.send(request_message.encode('utf-8'))
    recieve_message = clientSocket.recv(65535)
    print(recieve_message.decode())


clientSocket.close()
