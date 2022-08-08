# subscriber em python
import zmq

connect_xpubs=["5556", "5555"]

def init():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)

    socket.setsockopt(zmq.RCVHWM, 1000)
    socket.setsockopt(zmq.SNDHWM, 1000)
    socket.setsockopt(zmq.IPV6, 0)
    socket.setsockopt(zmq.LINGER, 0)
    socket.connect("tcp://127.0.0.1:" + connect_xpubs[1])
    socket.setsockopt_string(zmq.SUBSCRIBE, "gustavinho")
    socket.setsockopt_string(zmq.SUBSCRIBE, "fabricio falando")

    while True:
        poller = zmq.Poller()
        # connect using socket to outgoing messages to publicher
        poller.register(socket, zmq.POLLOUT)

        try:
            events = poller.poll(1000)
            #msg = socket.recv() # le do socket
            #print(msg)

            if events:
                print("Message comes from...")

        except Exception as e:
            print(e)

        finally:
            poller.unregister(socket)


init()









