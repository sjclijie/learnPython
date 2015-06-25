#!/usr/local/bin/python

import socket
import binascii

def convert_ipv4_address():
    for ip_addr in ['192.168.1.1','115.28.147.133']:
        packed_ip = socket.inet_aton(ip_addr)
        unpacked_ip = socket.inet_ntoa(packed_ip)
        print "Packed: %s, Unpacked: %s" % (binascii.hexlify(packed_ip), unpacked_ip)
        

if __name__ == '__main__':
    convert_ipv4_address()
            
