import zmq

xpub_addr = 'tcp://127.0.0.1:5555'
xsub_addr = 'tcp://127.0.0.1:5556'
context = zmq.Context()

#create XPUB 
xpub_socket = context.socket(zmq.XPUB)
xpub_socket.bind(xpub_addr)


#create XSUB
xsub_socket = context.socket(zmq.XSUB)
xsub_socket.connect(xsub_addr)

# create poller
poller = zmq.Poller()
# register incoming messages
poller.register(xpub_socket, zmq.POLLIN)
poller.register(xsub_socket, zmq.POLLIN)


while True:
    # set messages to a dict that are on the poll with timeout de 1000
    event = dict(poller.poll(1000))
    if xpub_socket in event:
        message = xpub_socket.recv_multipart()
        print("[BROKER] xpub_socket recv message: %r" % message)
        xsub_socket.send_multipart(message)
    if xsub_socket in event:
        message = xsub_socket.recv_multipart()
        print("[BROKER] xsub_socket recv message: %r" % message)
        xpub_socket.send_multipart(message)
