from packetSniffer.scapy.all import *

def showpacket(packet):
    print(packet.show())

def main(filter):
    sniff(filter = "port 53", prn = showpacket, count = 0)

if __name__ == '__main__':
    main(filter)