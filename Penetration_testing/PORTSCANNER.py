import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
host = input("Please Enter a valid IP: ")
port = int(input("Please enter the port you would like to scan:  "))



def portscanner(port):
    if s.connect_ex((host, port)):
        print("[-] Port is closed.")
    else:
        print ("[+] Port is open.")

portscanner(port)

