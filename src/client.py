import socket
import sys
from PIL import Image
import os
from imgurpython import ImgurClient

# ASCII_CHARS_DETAIL = "@%#*+=-:. "
# ASCII_CHARS_EXTRA_DETAIL = "@%#*+=-:.~^,`'\"<>i!lI;:,_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
# ASCII_CHARS_ULTRA_DETAIL = "@%#*+=-:.~^,`'\"<>i!lI;:,_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

client_id = 'c1ad9ed60abff73'

client_secret = 'bdeeda763017ee2db235ec38cd6912193bd888ce'

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
            to_send = message
        
        # handle error cases for invalid messages
        # when invalid message -> don't send, return and prompt back

        client_socket.send(to_send.encode())  # send message, default encoding encoding="utf-8", errors="strict"
        data = client_socket.recv(1024).decode()  # receive response

        #temporary name for the picture
        filename = 'temporary'

        #save the picture received from the server and get its filepath
        picture_path = save_png_data(data, filename, client_socket)
    # Initialize the Imgur client

        client = ImgurClient(client_id, client_secret)



        # Upload the image

        image_path = picture_path # Replace with the path to your image
        uploaded_image = client.upload_from_path(image_path, anon=True)



        # Get the uploaded image link
        image_link = uploaded_image['link']

        print("Image uploaded successfully. Link:", image_link)
        #Displaying the ASCIIart with the provided picture path
        # display_ASCIIart(picture_path)
        

        # print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input
        print(message)
    client_socket.close()  # close the connection

# def resize_image(image, new_width=100):
#     width, height = image.size
#     aspect_ratio = float(height) / float(width)
#     new_height = int(aspect_ratio * new_width * 0.55)
#     resized_image = image.resize((new_width, new_height))
#     return resized_image

# def image_to_ascii(image):
#     image = image.convert("L")  # Convert to grayscale
#     pixels = image.getdata()
#     ascii_str = ""
#     for pixel_value in pixels:
#         ascii_index = int(pixel_value / 256 * len(ASCII_CHARS_ULTRA_DETAIL))
#         ascii_str += ASCII_CHARS_ULTRA_DETAIL[ascii_index]
#     return ascii_str

def save_png_data(data, filename, socket):
    # Get the current directory
    current_directory = os.getcwd()
    
    # Build the file path in the current directory with .png extension
    filepath = os.path.join(current_directory, filename)

    if not filepath.lower().endswith('.png'):
        filepath += '.png'
    
    # Convert the received data from string to bytes
    png_data = data.encode()
    fileSize = int(data)
    # Save the data to a file
    with open(filepath, "wb") as file:
        bytes_received = 0
        while bytes_received < fileSize:
            chunk = socket.recv(1024)
            if not chunk:
                break
            file.write(chunk)
            bytes_received += len(chunk)
    print(f"PNG file '{filename}' saved as '{filepath}'.")

    return filepath

# def display_ASCIIart(file_path):
#     try:
#             #opening the image
#         image = Image.open(file_path)
#     except Exception as e:
#         print(f"Unable to open image file: {e}")
#         return
        
#     image = resize_image(image)
#     ascii_str = image_to_ascii(image)

#     #process of displaying ASCII art in the terminal 
#     width = image.width
#     ascii_str_len = len(ascii_str)
#     ascii_img = [ascii_str[i:i + width] for i in range(0, ascii_str_len, width)]
#     ascii_img = "\n".join(ascii_img)
#     print(ascii_img)



if __name__ == '__main__':
    client_program()