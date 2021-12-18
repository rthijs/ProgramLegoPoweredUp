import socket
import json

def xboxc_server():
    host = "127.0.0.1"
    port = 8099

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(1) #we only listen to one client
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(128).decode() #message max size 128 bytes
        print(str(data))
        
        input_event = json.loads(data)
        
        index = input_event['controllerIndex']
        item = input_event['item']
        value = input_event['value']

        print(str(index))
        print(str(item))
        print(str(value))
        print('--------------------------')


    conn.close()


if __name__ == '__main__':
    xboxc_server()