import socket
import threading
from queue import Queue

queue=Queue()
open_port=[]
target="192.168.XX.XXX"

def port_scanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((target, port))
        return True
    except:
        return False
def fill_queue(port_list):
    for port in port_list:
        queue.put(port)
def scanning():
    while not queue.empty():
        port=queue.get()
        if port_scanner(port):
            open_port.append(port)
            print("Port {} is open".format(port))

port_list=range(1,1024)
fill_queue(port_list)
thread_list=[]

for i in range(250):
    t=threading.Thread(target=scanning)
    thread_list.append(t)
for t in thread_list:
    t.start()
for t in thread_list:
    t.join()

print(f"Open ports: {open_port}")
