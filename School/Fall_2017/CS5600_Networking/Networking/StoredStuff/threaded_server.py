from socket import *
import threading
import json
import os.path
from pprint import pprint

class ThreadedServer(threading.Thread):
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(5000)
            threading.Thread(target = self.listenToClient,
                                      args = (client,address)).start()

    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    #print data
                    # Converting received json to dict
                    temp = json.loads(data)
                    #print temp
                    if temp['command'] == 'createTracker':
                        createTracker(temp['data'], client)
                    elif temp['command'] == 'updateTracker':
                        updateTracker(temp['data'], client)
                    elif temp['command'] == 'GET':
                        print 'GET command accepted'
                        GET(temp['data'], client)
                    elif temp['command'] == 'LIST':
                        get_tracker_list(client)
                    else:
                        response = temp['command']
                        client.send('SERVER: Invalid Command')
                else:
                    raise error('  Client disconnected')
            except:
                client.close()
                print '    Client closed'
                return False

def createTracker(data, client):

    file_path = './TrackFiles/' + data['fileName'] + '.track'
    print "in create"
    if os.path.isfile(file_path):
        client.send("SERVER: Tracker already exists.")
    else:
        with open(file_path, "a+") as f:
            temp = json.dump(data, f, sort_keys=False, indent=4, separators=(',', ': '))
            client.send("SERVER: Tracker creation success.")

def updateTracker(data, client):

    file_path = './TrackFiles/' + data['fileName'] + '.track'
    var = ''
    present = False

    if os.path.isfile(file_path):
        with open(file_path, "r") as f:
            var = json.load(f)

            for peer in var['peers']:
                if peer['ip'] == data['peers'][0]['ip']:
                    present = True

            if present == False:
                var['peers'].append(data['peers'][0])

        open(file_path, 'w').close()
        with open(file_path, "a+") as f:
            temp = json.dump(var, f, sort_keys=False, indent=4, separators=(',', ': '))

        client.send("SERVER: Update Successful")
    else:
        client.send("SERVER: No Tracker Exists")

def get_tracker_list(client):
    filenames = []
    print 'test'
    for filename in os.listdir('TrackFiles'):
        filenames.append(filename)
    filenames = json.dumps(filenames, filenames)
    print filenames
    client.send(filenames)

def GET(data, client):
    file_path = './TrackFiles/' + data['fileName'] + '.track'

    if os.path.isfile(file_path):
    	print 'FILE EXISTS'
    	with open(file_path, 'r') as f:
            print 'FILE OPEN'
            temp1 = json.load(f)
            print temp1
            temp1 = json.dumps(temp1, temp1)
            print temp1
    	    # m = hashlib.md5()
    	    # m.update(repr(temp1))
    	    #client.send("REP GET BEGIN")


    	    client.send(temp1)
    	    #client.send("REP GET END " + repr(m.digest()))
    else:
        client.send("Fail")
