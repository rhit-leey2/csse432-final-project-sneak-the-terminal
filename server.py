import socket
import sys
import subprocess

# 127.0.0.1 IP address for localhost
# ipconfig

def server_program():
    #get the hostname and print it
    host = socket.gethostname()
    print("Host name: " + str(host))

    if(len(sys.argv)!=2):
        print("Usage: python server.py <port_number>")
        sys.exit()
        
    port = int(sys.argv[1])
    
    #create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind method takes a tuple
    server_socket.bind((host, port))
    
    server_socket.listen(2)
    while True:
        conn, address = server_socket.accept()
        print("Connection from: "+str(address))
        
        #receive data
        while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            
            print("from connected user: " + str(data))
            # Run the command and capture the output
            if (str(data)[:2] == "cd"):
                print("This command start with cd")
                subprocess.check_output(str(data), shell=True)
                output = "You ran %s", (str(data))
            else:
                output = subprocess.check_output(str(data), shell=True)
            
            # Print the output
            print("HERE IS THE OUTPUT:")
            #print(output.decode())

            conn.send(output)
            
        conn.close()
        
    
if __name__ == '__main__':
    server_program()