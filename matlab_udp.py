'''Send and receive UDP messages in MATLAB (or directly in Python)

MATLAB functionality assumes you have MATLAB set up to run Python
code.  See:
https://www.mathworks.com/help/matlab/call-python-libraries.html

SENDING UDP:

    Call the function to send a message to a specified ip and port.

    Example usage in MATLAB:  
        >> a = py.matlab_udp.send('192.168.1.20', 5005, 'Hello');

    Test in Linux by listening using netcat:  
        $ nc -kluv <port, e.g. 5005>

RECEIVING UDP:

    After calling the function, it will wait until a UDP message
    is received, and then will return the message, ip, and port.

    Example usage in MATLAB:  
        >> a = py.matlab_udp.receive(5005)

        or with timeout (sec)

        >> a = py.udp_rx.receive(5005, 3)

    Test in Linux by sening msg:
        $ nc -u 192.168.1.12 5005

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


#def receive(udp_port, **kwargs):
def receive(udp_port, *args):
    """Receives a UDP message from port udp_port.
    Returns message, sender IP, and sender port.
    """
    udp_ip = "0.0.0.0"
    udp_port = int(udp_port)
    
    if len(args) > 0:
        timeout_sec = args[0]
    else:
        timeout_sec = 0     # 0 means no timeout, wait forever
    
    # print("Creating socket")
    sock = socket.socket(socket.AF_INET,    # Internet
                        socket.SOCK_DGRAM) # UDP
    # print("Socket created")

    # myhostname = socket.gethostname()
    # print("My hostname is {}".format(myhostname))
    # print("My ip is {}".format(socket.gethostbyname(myhostname)))

    if timeout_sec != 0:
        sock.settimeout(timeout_sec)  # Set timeout

    # print("Binding socket to {}:{}".format(udp_ip, udp_port))
    sock.bind((udp_ip, udp_port))
    # print("Socket bound")

    # print("Listening for UDP on {}:{}".format(udp_ip, udp_port))

    retval = {}    # Dictionary for returning values
    try:
        data, (senderip, senderport) = sock.recvfrom(1024) # buffer size is 1024 bytes
    except socket.timeout:
        retval['timeout_occurred'] = bool(1)    
        retval['timeout_sec'] =float(timeout_sec)   # Make sure float for MATLAB interpretation
    else:
        retval['msg'] = data.decode('utf-8')
        retval['sender_ip'] = senderip
        retval['sender_port'] = float(senderport)   # Float for MATLAB interpretation
        retval['timeout_occurred'] = bool(0)
        retval['timeout_sec'] = float(timeout_sec)  # Make sure float for MATLAB interpretation
    finally:       
        return retval
