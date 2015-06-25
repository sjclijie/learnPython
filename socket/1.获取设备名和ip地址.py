#!/usr/local/bin/python

import socket;

def print_machine_info():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)

    print "Host name: %s" % host_name
    print "Host Ip: %s" % host_ip



def print_remote_machine_info(remote_host):
    try:
        print "Ip address: %s " % socket.gethostbyname(remote_host)
    except socket.error, err_msg:
        print "%s: %s" % (remote_host, err_msg)


if __name__ == '__main__':
    print_machine_info()
    print_remote_machine_info("www.jaylee.cc");
