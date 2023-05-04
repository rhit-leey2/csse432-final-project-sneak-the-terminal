import socket
import sys


def client_program():
    if(len(sys.argv) != 3):
        print("Usage: python client.py <server_(IP)_address> <server_port_number>")
        sys.exit()
    #host = socket.gethostname()
    #host = sys.argv[2]
    port = int(sys.argv[2])

    server_ip = socket.gethostbyname(sys.argv[1])
    print("server IP: ", server_ip)

    server_addr = (server_ip, port)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instantiate
    client_socket.connect(server_addr)  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != ';;;':

        # if (message == "dir"):
        #     to_send = "ls"
        # elif message == "cd":
        #     to_send == "pwd"
        # elif message == "mkdir newFolder":
        #     to_send = "mkdir myFolder"
        # elif message == "echo some-test > fileName(.txt)":
        #     to_send = "cat > fileName(.txt)"
        # elif message == "ren oldFolderName= 


        client_socket.send(message.encode())  # send message, default encoding encoding="utf-8", errors="strict"
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
        print(message)
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()