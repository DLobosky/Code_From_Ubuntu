import threading
from socket import *
import time

class ThreadedHost(threading.Thread):
    def __init__(self, host_sock):
        self.host_sock = host_sock
        print "ThreadedHost inited"

    def listen(self):
        while True:
            print "    Host sock running"
            time.sleep(3)
        #self.host_sock.listen(5)
        # while True:
        #     client, address = self.sock.accept()
        #     client.settimeout(60)
        #     threading.Thread(target = self.listenToClient,
        #                      args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                filename = client.recv(size)
                if filename:
                    client.send("SEEDER: Request received.")
                else:
                    raise error('  Client disconnected')
            except:
                client.close()
                print '    Client closed'
                return False
