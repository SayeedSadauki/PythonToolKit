import argparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        cskt = socket(AF_INET, SOCK_STREAM)
        cskt.connect((tgtHost, tgtPort))
        cskt.send('Hello there may i connect\r\n'.encode())
        results = cskt.recv(1024).decode()
        screenLock.acquire()
        print('[+] {}:{} open\n{}'.format(tgtHost, tgtPort, results))
        print('[+] %d/tcp open' %tgtPort)
        
    except:
        screenLock.acquire()
        print('[-] %d/tCP connection closed' %tgtPort)
    finally:
        screenLock.release()
        cskt.close()
def portscan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] cannot resolve '%s' : Unknown Host" % tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] scan results for :' + tgtName[0])
    except:
        print('\n[+] scan result for :' + tgtIP)

    setdefaulttimeout(10)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

    

if __name__ == '__main__':
    p = argparse.ArgumentParser(description='This is an advanced Port Scanner')

    p.add_argument('-H', '--tgtHost', type=str, help='specify target host')
    p.add_argument('-p', '--tgtPorts', nargs='+', type=int, help='specify target port(s) separated by space')


    args= p.parse_args()

    tgtHost= args.tgtHost
    tgtPorts= args.tgtPorts
    if not (tgtHost and tgtPorts):
        p.print_help()
        exit(0)
portscan(tgtHost, tgtPorts)
