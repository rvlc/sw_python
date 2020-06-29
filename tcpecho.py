import socket
import sys
import random
import string


def get_constants(prefix):
    """Create a dictionary mapping socket module constants to their names."""
    return dict((getattr(socket, n), n)
                for n in dir(socket)
                if n.startswith(prefix)
                )


families = get_constants('AF_')
types = get_constants('SOCK_')
protocols = get_constants('IPPROTO_')

# Create a TCP/IP socket
sock = socket.create_connection(('192.168.0.10', 2019))

print ('Family  :', families[sock.family])
print ('Type    :', types[sock.type])
print ('Protocol:', protocols[sock.proto])
iteration = 0;
while True:
    try:
        # Send data
        data = ''
        recvdata = ''
        N = random.randrange(2, 50)
        message = ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
        #print ('sending "%s"' % message)
        sock.sendall(message.encode('utf-8'))

        amount_received = 0
        #amount_expected = len(message)
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            recvdata += data.decode("utf-8")
            #print("Received: %s" % data)
        if message == recvdata:
            #print("String is Ok\n")
            iteration += 1
            print("iteration : %d" % iteration)

        else:
            print("********String is not OK***********\n")
            print("Send Msg: %s" %message)
            print("recv msg: %s" %recvdata)
    finally:
        iteration += 1
        print("iteration : %d" % iteration)

sock.close()
