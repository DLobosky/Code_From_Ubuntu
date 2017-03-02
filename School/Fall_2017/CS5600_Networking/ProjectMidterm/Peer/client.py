from socket import *
import os
import threading
import sys
import json
import time
import netifaces as ni
import math
import hashlib

client_ip = ni.ifaddresses('eth0')[2][0]['addr']
portMin = 8000
portMax = 9000
#threadLock = threading.Lock()

def calculate_md5(file_path):
    md5temp = hashlib.md5()
    with open(file_path,'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5temp.update(chunk)
    return repr(md5temp.digest())

def create_tracker(track_sock, filename, description, port):

    file_path = './Files/' + filename
    flag = os.path.exists(file_path)
    if flag:
        statinfo = os.stat(file_path)  #File Size
        file_size = statinfo.st_size

        md5 = calculate_md5(file_path)

        # Creating dict object with command and tracker data
        message = {"command": "createTracker",
                   "data": {"fileName": filename,
                            "fileSize": file_size,
                            "description": description,
                            "md5": md5,
                            "peers": [{"ip": client_ip,
                                       "port": port,
                                       "start": 0,
                                       "end": file_size,
                                       "time": time.time()
                                      }]
                            }
                    }

        # Converting message dict to json string
        message = json.dumps(message, message, sort_keys=False,
                             indent=4, separators=(',', ': '))

        # Sending message to the tracker server
        track_sock.send(message)

        # Checking message receival/return
        print track_sock.recv(1024)

    else:
        print "The requested file '" + filename + "' does not exist"

def update_tracker(track_sock, filename, port):
    message = {
                "command": "updateTracker",
                "data": {"fileName": filename,
                         "peers": [{
                                    "ip": client_ip,
                                    "start": 5,
                                    "end": 10,
                                    "time": time.time()
                                  }]
                        }
              }

    message = json.dumps(message, message, sort_keys=False,
                         indent=4, separators=(',', ': '))

    track_sock.send(message)

    print track_sock.recv(1024)

def get_tracker_list(track_sock):

    list_file = 'list_file.txt'

    message = {"command": "LIST",
               "data": {}
               }

    message = json.dumps(message, message, sort_keys=False, indent=4, separators=(',', ': '))

    track_sock.send(message)
    var = track_sock.recv(1024)
    var = json.loads(var)

    with open(list_file, "w") as f:
        for i in var:
            f.write(i)

def GET(track_sock, filename):
    file_path = './Trackers/' + filename + '.track'
    GET = {"command": "GET",
           "data": {"fileName": filename}}

    GET = json.dumps(GET, GET)
    track_sock.send(GET)
    var = track_sock.recv(1024)

    if var != "Fail":
    	var = json.loads(var)
    	if os.path.isfile(file_path):
    		open(file_path, 'w').close()
    		with open(file_path, 'a+') as f:
    			json.dump(var, f, sort_keys=False,
                          indent=4, separators=(',', ': '))
    	else:
    		with open(file_path, 'a+') as f:
    			json.dump(var,f, sort_keys=False,
                          indent=4, separators=(',', ': '))
        return 1
    else:
        return 0

def download_file(track_sock, filename):
    success = GET(track_sock, filename)
    print "GET success"
    if success:
        file_path = './Trackers/' + filename + '.track'
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                track_info = json.load(f)
                print "launching thread to download"
                t1 = threading.Thread(target=get_segment,
                                     args=(filename, 0,
                                           track_info['fileSize'],
                                           track_info['peers'])).start()
    else:
        print "     No tracker for file by that name."

def get_segment(filename, start, end, available_peers):
    peers = []
    # iterates through all peers
    for i in range(len(available_peers)):
        # if current peer has entire scope for the desired segment
        if available_peers[i]["start"] <= start and available_peers[i]["end"] >= end:
            # push it into the array of peer info
            peers.append(available_peers[i])
    # if any peers have the entire segment
    if len(peers) > 0:
        # set start point to start of segment
        point0 = start
        # calculate max segment size by splitting desired segment into number of peers
        mss = int(math.floor((end-start)/len(peers)))
        # iterate through all but last of peers with entire segment
        test = (len(peers)-1)
        for i in range(len(peers)-1):
            # update end point to be 1 mss from the current start point
            point1 = point0 + mss
            # spin off a thread to download the segment from the current peer (i)
            threading.Thread(download_segment, (filename, point0, point1, available_peers, peers[i]))
            # update new start point to be 1 past old end point
            point0 = point1 + 1
        # download last remaining segment (smaller than mss)
        download_segment(filename, point0, end, available_peers, peers[len(peers)-1])
    # if no peers have the entire segment
    else:
        # split desired segment range in half
        mid = int(math.floor((start+end)/2))
        # call get segment on the two halves
        threading.Thread(get_segment, (filename, start, mid, available_peers))
        threading.Thread(get_segment, (filename, mid+1, end, available_peers))
    return
    # target_peer = available_peers[0]
    # download_segment(filename, start, int(math.floor(end/2)), available_peers, target_peer)
    # download_segment(filename, int(math.floor(end/2)), end, available_peers, target_peer)

def download_segment(filename, start, end, peers, target):
    host_ip = target['ip']
    host_port = target['port']
    print "attempting to connect to host socket"
    host_sock = socket(AF_INET, SOCK_STREAM)
    host_sock.connect((host_ip, host_port))
    print "Sending download message"
    message = {"filename": filename, "start": start, "end": end}
    message = json.dumps(message, message, sort_keys=False,
                         indent=4, separators=(',', ': '))
    host_sock.send(message)
    response = host_sock.recv(1024)
    # if file was present on host
    if response == "1":
        # notify of readiness to receive file
        host_sock.send("1")
        file_path = './Files/' + filename
        open(file_path, 'wb').close()
        with open(file_path, 'r+b') as f:
            point0 = start
            steps = int(math.floor((end-start)/1024))
            for i in range(steps):
                f.seek(point0, 0)
                data = host_sock.recv(1024)
                host_sock.send("1")
                f.write(data)
                point0 = point0 + 1024
            f.seek(point0, 0)
            data = host_sock.recv(end - point0)
            host_sock.send("1")
            f.write(data)
            print "Exiting file write loop"
    else:
        print response

def host_run(host_ip, host_port):
    host_sock = socket(AF_INET, SOCK_STREAM)
    host_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    host_bound = False
    while not host_bound:
        try:
            host_sock.bind((host_ip, host_port))
            host_bound = True
        except:
            pass

    print "    CLIENT: Host server running"
    host_sock.listen(5)
    while True:
        print "Host waiting for connection"
        peer, address = host_sock.accept()
        print "Host accepted connection"
        peer.settimeout(60)
        threading.Thread(target = send_file,
                                  args = (peer, address)).start()
    return

def send_file(peer, address):
    print "Host receiving message"
    message = peer.recv(1024)
    message = json.loads(message)
    print "Message: " + str(message)
    filename = message["filename"]
    start = message["start"]
    end = message["end"]
    print start
    print end
    file_path = './Files/' + filename
    if os.path.isfile(file_path):
        peer.send("1")
        print "Received confirmation to send file"
        message = peer.recv(1024)
        if message == "1":
            with open(file_path, 'rb') as f:
                point0 = start
                steps = int(math.floor((end-start)/1024))
                for i in range(steps):
                    f.seek(point0, 0)
                    peer.send(f.read(1024))
                    temp = peer.recv(1024)
                    point0 = point0 + 1024
                f.seek(point0, 0)
                peer.send(f.read(end - point0))
                temp = peer.recv(1024)
            print "Sending end notification"
    else:
        peer.send("0")
    return

def main():
    if (len(sys.argv) == 4 and int(sys.argv[3]) >= portMin and int(sys.argv[3]) <= portMax):

        # Grabbing desired port number from arguments list
        server_ip = sys.argv[1]
        server_port = int(sys.argv[2])
        host_port = int(sys.argv[3])

    else:
        # Prompt for valid port number
        print "Please enter the server IP address"
        server_ip = input()
        print "  Please enter the server port number (surrounded by \"\")"
        server_port = input()
        print "  Please enter a port number between %d and %d" % (portMin, portMax)
        host_port = input()

    # Loop until a valid port number is input
    while (host_port < portMin or host_port > portMax):
		print "  Please enter a port number between %d and %d" % (portMin, portMax)
		server_port = input()

    # Running threaded server with specified port number
    host_ip = ni.ifaddresses('eth0')[2][0]['addr']
    host_socket = socket(AF_INET, SOCK_STREAM)
    host_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    host_available = False
    while not host_available:
        try:
            host_socket.bind((host_ip, host_port))
            host_available = True
            host_socket.close()
        except:
            print "Host port in use. Enter new port number: "
            host_port = input()

    # launching threaded server to host connections from peers
    threading.Thread(target=host_run, args=(host_ip, host_port)).start()

    tracker_socket = socket(AF_INET, SOCK_STREAM)
    tracker_socket.connect((server_ip, server_port))

    print '    CLIENT: Connection to tracker established'

    choice = ''

    while choice != 'exit':
        print "Enter a command (createTracker, updateTracker, GET, LIST, exit): "
        choice = raw_input('     ')

        if choice == 'createTracker':
            print "     File name: "
            filename = input()
            create_tracker(tracker_socket, filename, 512, host_port)
        elif choice == 'updateTracker':
            print "     File name: "
            filename = input()
            update_tracker(tracker_socket, filename, host_port)
        elif choice == 'GET':
            print "     File name: "
            filename = input()
            GET(tracker_socket, filename)
        elif choice == 'LIST':
            get_tracker_list(tracker_socket)
        elif choice =='DOWNLOAD':
            print "     File name: "
            filename = input()
            download_file(tracker_socket, filename)
        elif choice == 'exit':
            print "PEACE lil homie"
        else:
            print "Invalid input!"
        #update_tracker(tracker_socket, 'fileNAme.txt', 8001)
        #create_tracker(tracker_socket, "fileNAme.txt", 512, 8001)
        # # Sending message to socket
        # print '  CLIENT: Input message'
        # message = raw_input('    ')
        # tracker_socket.send(message)
        #
        # print tracker_socket.recv(1024)

    # Closing socket when finished
    tracker_socket.close()


if __name__ == '__main__':
    main()
