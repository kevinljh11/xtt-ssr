import logging

def record_connection(remote_addr,remote_port,client_addr,client_port,userid,data):
    client_addr=client_addr.replace("::ffff:","")
    logging.info("{} is connecting {}:{} from {}:{}".format(userid,remote_addr,remote_port,client_addr,client_port));
