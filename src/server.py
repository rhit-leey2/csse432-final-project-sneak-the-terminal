import os
import socket
import sys
import subprocess
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
 
            # Execute AppleScript to get the ID of the frontmost iTerm2 window
            script = 'tell application "iTerm2" to id of current window'
            result = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
            window_id = result.stdout.strip()

            if result.returncode == 0 and window_id:
                # Capture the screenshot of the iTerm2 window using screencapture command
                subprocess.run(['screencapture', '-l', window_id, 'terminal_screenshot.png'])
                print("screenshot done")
            else:
                print("iTerm2 window not found.")

            
            fileName = 'terminal_screenshot.png'
            if(os.path.exists(fileName) == False):
                conn.send(b"File not exist")
            else:
                fileSize = os.path.getsize(fileName)
                conn.send(str(fileSize).encode())
                with open(fileName, "rb") as file:
                    print("Start to send")
                    #conn.send(b"File transfer started")
                    conn.sendfile(file, 0, fileSize)
            #conn.send(b"file transfer of" + bytes(str(fileSize), 'utf-8') + b"bytes complete and placed in current directory")
            
            #conn.send(output)
            
            
            
        conn.close()
        
    
if __name__ == '__main__':
    server_program()