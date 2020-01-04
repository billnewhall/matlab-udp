#!/usr/bin/python3
"""Script implementation of receive() function in matlab_udp module

Example usage from Linux:  
    $ python udp_rx.py 5005

W. Newhall 1/2020 (original)
"""


import matlab_udp
import argparse


def main():
    # Get arguments from command line
    parser = argparse.ArgumentParser(description='Receive a UDP message.')
    parser.add_argument('myport', type=int, help="My port to listen on")
    args = parser.parse_args()
    udp_port = args.myport

    udp_msg, senderip, senderport = matlab_udp.receive(udp_port)
    
    print("Received UDP from {}:{} {}".format(senderip, int(senderport), udp_msg))


if __name__== "__main__":
  main()
