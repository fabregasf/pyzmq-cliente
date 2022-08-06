import zmq
import utils.z85

port="5506"
url="tcp://localhost:%s" % port

context = zmq.Context()

def init():
    socket = context.socket(zmq.SUBSCRIBE)

    # configuring connection
    socket.setsockopt(zmq.SNDHWM, 1000)
    socket.setsockopt(zmq.IPV6,0)
    socket.setsockopt(zmq.LINGER,0)

    # set server key
    socket.setsockopt(zmq.CURVE_SERVERKEY,"rq:rM>}U?@Lns47E1%kR.o@n%FcmmsL/@{H8]yf7")
    # requester
    socket.setsockopt(zmq.CURVE_PUBLICKEY, "Yne@$w-vo<fVvi]a<NY6T1ed:M$fCG*[IaLV{hID")
    socket.setsockopt(zmq.CURVE_SECRETKEY, "D:)Q[IlAW!ahhC2ac:9*A}h:p?([4%wOTJ%JR%cs")

    # execute the connection
    socket.connect(url)



#while 1:



