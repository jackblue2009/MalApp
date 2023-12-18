import cv2
import socket

def connect_to_server(ip_address, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((ip_address, port))
        print(f"Connected to server at {ip_address}:{port}")

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and the correct IP address and port are provided.")
    
    finally:
        client_socket.close()

def get_local_ip():
    temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    temp_socket.connect(("8.8.8.8", 80))

    local_ip = temp_socket.getsockname()[0]
    temp_socket.close()
    return local_ip

ip = "192.168.100.32"
port = 8080
connect_to_server(ip, port)

local_ip = get_local_ip()
print(f"Local IP address: {local_ip}")

#url = 'http://193.188.123.45:80/video'

#cap = cv2.VideoCapture(url)

#while True:

#    ret, frame = cap.read()

#    if ret:
#        cv2.imshow('IP Camera Feed', frame)
    
#    if cv2.waitKey(1) == ord('q'):
#        break

#cap.release()
#cv2.destroyAllWindows()