#!/usr/bin/python3
"""Script implementation of send() function in matlab_udp module

Example usage from Linux:  
    $ python udp_send.py 192.168.1.12 5005 "Hello"

W. Newhall 1/2020 (original)
"""


import matlab_udp
import argparse


def main():
    # Get arguments from command line
    parser = argparse.ArgumentParser(description='Sends UDP message to specified ip and port')
    parser.add_argument('destip', type=str, help="Destination IP address")
    parser.add_argument('destport', type=int, help="Destination port")
    parser.add_argument('msg', type=str, help="Message to send")
    args = parser.parse_args()

    udp_ip = args.destip
    udp_port = args.destport
    udp_msg = args.msg

    num_bytes_sent = matlab_udp.send(udp_ip, udp_port, udp_msg)

    print("Sent {} UDP bytes to {}:{}  {}".format(int(num_bytes_sent), udp_ip, udp_port, udp_msg))

if __name__== "__main__":
  main()
