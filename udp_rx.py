#!/usr/bin/python3
"""Script implementation of receive() function in matlab_udp module

Example usage from Linux:  
    $ python udp_rx.py 5005
    $ python udp_rx.py 5005 --timeout_sec 3

    timeout_sec = 0 results in no timeout (wait forever)

W. Newhall 1/2020 (original)
"""


import matlab_udp
import argparse


def main():
    # Get arguments from command line
    parser = argparse.ArgumentParser(description='Receive a UDP message.')
    parser.add_argument('myport', type=int, help="My port to listen on")
    parser.add_argument('--timeout_sec', type=int, help="Timeout of waiting for UDP packet")
    args = parser.parse_args()
    udp_port = args.myport

    if args.timeout_sec is not None:
        timeout_sec = args.timeout_sec
    else:
         timeout_sec = 0

    #udp_msg, senderip, senderport = matlab_udp.receive(udp_port)
    #rx_info = matlab_udp.receive(udp_port, timeout_sec=timeout_sec)
    rx_info = matlab_udp.receive(udp_port, timeout_sec)
    
    if rx_info['timeout_occurred'] == False:
        print("Received UDP from {}:{} {}".format(rx_info['sender_ip'], int(rx_info['sender_port']), rx_info['msg']))
    else:
        print("Timeout occurred.")


if __name__== "__main__":
  main()
