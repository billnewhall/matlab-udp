'''Send and receive UDP messages in MATLAB (or directly in Python)

MATLAB functionality assumes you have MATLAB set up to run Python
code.  See:
https://www.mathworks.com/help/matlab/call-python-libraries.html

SENDING UDP:

    Call the function to send a message to a specified ip and port.

    Example usage in MATLAB:  
        >> a = py.udp_send.send('192.168.1.20', 5005, 'Hello');

    Example usage in Linux:  
        $ python udp_send.py <ip adress> <port, e.g. 5005> <message>

    Test in Linux by listening using netcat:  
        $ nc -kluv <port, e.g. 5005>

RECEIVING UDP:

    After calling the function, it will wait until a UDP message
    is received, and then will return the message, ip, and port.

    Example usage in MATLAB:  
        >> a = py.udp_rx.receive(5005)
                (then send msg with nc or udp_send.py)
        a = 
        Python tuple with no properties.
            ('Hello', '192.168.1.12', 53842.0)
        >> a{1}
        ans = 
        Python str with no properties.
            Hello
        >> char(a{1})
        ans =
            'Hello'
        >> char(a{2})
        ans =
            '192.168.1.12'
        >> a{3}
        ans =
            53842

    Example usage in Linux:  
        $ python udp_rx.py <port, e.g. 5005>


W. Newhall 1/2020 (original)
'''



import socket
import argparse


def send(udp_ip, udp_port, udp_msg):
    """Sends the UDP message udp_msg to destination udp_ip port udp_port.
    Returns number of bytes sent.
    """
    udp_port = int(udp_port)

    # print("Creating socket")
    sock = socket.socket(socket.AF_INET,    # Internet
                        socket.SOCK_DGRAM)  # UDP

    # print("Socket created")

    # myhostname = socket.gethostname()
    # print("My hostname is {}".format(myhostname))
    # print("My ip is {}".format(socket.gethostbyname(myhostname)))

    # print("Sending UDP to {}:{} from {}".format(udp_ip, udp_port, udp_ip))

    message = udp_msg
    num_bytes_sent = sock.sendto(message.encode('utf-8'), (udp_ip, udp_port))

    # print("Sent {} UDP bytes to {}:{}  {}".format(num_bytes_sent, udp_ip, udp_port, udp_msg))
    return float(num_bytes_sent)


def receive(udp_port):
    """Receives a UDP message from port udp_port.
    Returns message, sender IP, and sender port.
    """
    udp_ip = "0.0.0.0"
    udp_port = int(udp_port)

    # print("Creating socket")
    sock = socket.socket(socket.AF_INET,    # Internet
                        socket.SOCK_DGRAM) # UDP
    # print("Socket created")

    # myhostname = socket.gethostname()
    # print("My hostname is {}".format(myhostname))
    # print("My ip is {}".format(socket.gethostbyname(myhostname)))

    # print("Binding socket to {}:{}".format(udp_ip, udp_port))
    sock.bind((udp_ip, udp_port))
    # print("Socket bound")

    # print("Listening for UDP on {}:{}".format(udp_ip, udp_port))

    data, (senderip, senderport) = sock.recvfrom(1024) # buffer size is 1024 bytes
    udp_msg = data.decode('utf-8')
    # print("Received UDP from {}:{} {}".format(senderip, senderport, udp_msg))
    return (udp_msg, senderip, float(senderport))

