# Python Module for Sending & Receiving UDP in MATLAB

## Overview

This Python module provides functions to send and receive UDP messages in MATLAB (or directly in Python).

MATLAB functionality assumes you have MATLAB set up to run Python code.  See:
[https://www.mathworks.com/help/matlab/call-python-libraries.html](https://www.mathworks.com/help/matlab/call-python-libraries.html)

In the examples below, replace my IP address (192.168.1.12) with your IP address.

Files:

* ```matlab_udp.py``` contains the module.  No other files needed to use the module.
* ```udp_send.py``` is a Python script that uses the module to send a UDP message in Python or  terminal command line.
* ```udp_rx.py``` is a Python script that uses the module to receive a UDP message in Python or terminal command line.


## Sending UDP with ```matlab_udp``` Module

Use the module's ```send()``` function to send a message via UDP to a specified IP and port.

The function returns the number of bytes sent.

Example usage in MATLAB:  

    >> a = py.matlab_udp.send('192.168.1.12', 5005, 'Hello');

Example usage in Python:

    >>> import matlab_udp
    >>> matlab_udp.send('192.168.1.12', 5005, "Hello")

This message can be received in Linux using netcat to listen:  

    $ nc -kluv 5005
    Listening on [0.0.0.0] (family 0, port 5005)
    Hello

## Receiving UDP with ```matlab_udp``` Module

Use the module's ```receive()``` function to receive a message via UDP from a specified port.

The function will block until a UDP message is received (unless a timeout is specified).

The function returns the message, IP address of sender, and port of sender.

Example usage in MATLAB:  

    >> msg = py.matlab_udp.receive(5005);

Then, send a message from a Linux terminal using:

    $ nc -u 192.168.1.12 5005
    Hello

The msg variable contains the message:

    msg = 
      Python dict with no properties.
        {'msg': 'Hello\n', 'sender_ip': '192.168.1.12', 'sender_port': 44155.0, 'timeout_occurred': False, 'timeout_sec': 0.0}
    
    >> char(msg{'msg'})
    ans =
        'Hello
         '        

    >> char(msg{'msg'}(1:end-1))
    ans =
        'Hello'

    >> char(msg{'sender_ip'})
    ans =
        '192.168.1.12'
    
    >> msg{'sender_port'}
    ans =
           44155    
    
 Note that ```nc``` sends an end-of-line, so the message string has an end-of-line.  This module's ```send()``` function does not send the end-of-line.
    
Example usage in Python:  

    >>> import matlab_udp
    >>> matlab_udp.receive(5005)

Then, send a message using:

    $ nc -u 192.168.1.12 5005
    Hello

Python will show:
    
    {'msg': 'world\n', 'sender_ip': '192.168.1.12', 'sender_port': 44155.0, 'timeout_occurred': False, 'timeout_sec': 0.0}

A timeout can be specified for receiving.  After the timeout, the function returns and indicates a timeout in the returned values.  Specifying zero for the optional timeout paramter means no timeout -- wait forever.

In MATLAB, to specify a 3 second timeout:

    >> msg = py.matlab_udp.receive(5005, 3);

If a UDP message is not received within the timeout, the return value is:

    msg = 
      Python dict with no properties.
        {'timeout_occurred': True, 'timeout_sec': 3.0}

In Python, to specify a 3 second timeout:

    >>> matlab_udp.receive(5005, 3)
    
If a UDP message is not received within the timeout, the return value is:

    {'timeout_occurred': True, 'timeout_sec': 3.0}
 
## Running from Linux Command Line

To send a message via UDP from a Linux terminal using the ```matlab_udp``` module, use the ```udp_send.py``` script.

    $ python udp_send.py 192.168.1.12 5005 "Hello"
    Sent 5 UDP bytes to 192.168.1.12:5005  Hello

This message can be received in another Linux terminal using:

    $ nc -kluv 5005
    Listening on [0.0.0.0] (family 0, port 5005)
    Hello

To receive a message via UDP from a Linux terminal using the ```matlab_udp``` module, use the ```udp_rx.py``` script.

    $ python udp_rx.py 5005

Then, send a message from another Linux terminal using:

    $ nc -u 192.168.1.12 5005
    Hello

The terminal running ```udp_rx.py``` will show:

    Received UDP from 192.168.1.12:47185 Hello

To specify a receive timeout

    $ python udp_rx.py 5005 --timeout_sec 3

If a UDP message is not received within the timeout, the terminal will show is:

    Timeout occurred.

