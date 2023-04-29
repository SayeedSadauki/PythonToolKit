import argparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        cskt = socket(AF_INET, SOCK_STREAM)
        cskt.connect((tgtHost, tgtPort))
        print('[+] %d/tcp open' %tgtPort)
        cskt.close()
    except:
        print('[-] %d/tCP connection closed' %tgtPort)

def portscan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] cannot resolve '%s' : Unknown Host" % tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('\n[+] scan results for:' + tgtName[0])
    except:
        print('\n[+] scan result for :' + tgtIP)

    setdefaulttimeout(10)
    for tgtPort in tgtPorts:
        print('Scanning port' + str(tgtPort))
        connScan(tgtHost,int(tgtPort))

    

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
