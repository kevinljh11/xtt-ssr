import logging
import time
import threading
import webapi_utils
from configloader import load_config, get_config
CC = []

def record_connection(remote_addr,remote_port,client_addr,client_port,userid,data):
    global CC
    client_addr=client_addr.replace("::ffff:","")
    CC.append([
        userid,client_addr,client_port,remote_addr,remote_port,int(time.time())
    ])
    #print(CC)
    #logging.info("{} is connecting {}:{} from {}:{}".format(userid,remote_addr,remote_port,client_addr,client_port));

def loop(event):
    webapi = webapi_utils.WebApi()
    while True:
        time.sleep(1)
        global CC
        if(CC==[]):
            continue;
        WTP = CC
        CC=[]
        res = webapi.postApi("usage",{'node_id': get_config().NODE_ID},{"data":WTP})
        if(res):
            logging.info("Usage push succeed! {} usages pushed!".format(len(WTP)))
        else:
            logging.error("Usage Push Failed!")
            CC += WTP
        if event.is_set():
            logging.info("leo stopped!")
            break

def start():
    e = threading.Event()
    e.clear()
    a = threading.Thread(target=loop,args=(e,), name='LoopThread')
    a.start()
    return e
