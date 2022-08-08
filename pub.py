# publisher em python
import zmq
import z85

# many publishers
connected_xsubs=["5555","5556", "5557", "5558", "5559", "5560"]

def init():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)

    # configuring connection
    # outbound messages limit, otherwise 0mq drops packages
    socket.setsockopt(zmq.SNDHWM, 1000)
    socket.setsockopt(zmq.RCVHWM, 1000)
    socket.setsockopt(zmq.IPV6,0)
    socket.setsockopt(zmq.LINGER,0)
    # set server key
    socket.setsockopt_string(zmq.CURVE_SERVERKEY,"rq:rM>}U?@Lns47E1%kR.o@n%FcmmsL/@{H8]yf7")
    socket.setsockopt_string(zmq.CURVE_PUBLICKEY, "Yne@$w-vo<fVvi]a<NY6T1ed:M$fCG*[IaLV{hID")
    socket.setsockopt_string(zmq.CURVE_SECRETKEY, "D:)Q[IlAW!ahhC2ac:9*A}h:p?([4%wOTJ%JR%cs")

    # sub to topic
    socket.connect("tcp://127.0.0.1:5556")
    namepublisher = "Publisher gustavo".encode('utf-8')

    while True:
        message = input('input the message:')
        socket.send_multipart([namepublisher, message.encode('utf-8')])
        print("mensagem enviada para o xsub: "+ message)

    context.destroy()


init()

