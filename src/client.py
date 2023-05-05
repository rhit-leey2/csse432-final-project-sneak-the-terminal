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

        messageArr = []
        messageStr = ""
        
        if (message == "dir"):
            to_send = "ls"
        elif message == "cd":
            to_send == "pwd"
        elif message == "cd..":
            to_send = "cd .."
        elif message.startswith("mkdir"):
            mkdir, folder = messageArr.split(" ")
            to_send = "mkdir " + folder
        elif message.startswith("echo"):
            echo, file1, file2 = message.split(" ")
            messageStr.append("cat ")
            messageStr.append(file1 + " > ")
            messageStr.append(file2)
            to_send = messageStr
        elif message.startswith("rmdrir"):
            to_send = message
        elif message.startswith("ren"):
            ren, oldFile, newFile = message.split(" ")
            messageStr.append("mv ")
            messageStr.append(oldFile + " ")
            messageStr.append(newFile)
            to_send = messageStr
        elif message.startswith("robocopy"):
            robocopy, folder, filePath = message.split(" ")
            messageStr.append("cp -r")
            messageStr.append(folder + " ")
            messageStr.append(filePath) 
            to_send = messageStr
        elif message == "move":
            to_send == "mv"
        elif message.startswith("move"):
            move, folder, dir = message.split(" ")
            messageArr.append("mv")
            messageArr.append()
            to_send = "mkdir "
        elif message.startswith("cls"):
            to_send = "clear"
        elif message.startswith("type"):
            type, file = message.split(" ")
            to_send = "cat " + file
        elif message.startswith("Type"):
            type, path, pip, find, v, c = message.split(" ")
        elif message.startswith("dig"):
            to_send = message;
        
        # handle error cases for invalid messages
        # when invalid message -> don't send, return and prompt back

        client_socket.send(message.encode())  # send message, default encoding encoding="utf-8", errors="strict"
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
        print(message)
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()