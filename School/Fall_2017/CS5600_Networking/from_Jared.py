from socket import *
import os
import threading

"""
<createtracker filename filesize description md5 ip-address port-number>\n
createtracker: message from tracker server to the peer program
if command successful: <createtracker succ>\n
if command unsuccessful: <createtracker fail>\n
if tracker file already exists: <createtracker ferr>\n
"""

def CreateTracker(socket) # message from peer to the tracker server

    socket.receive filename
    socket.size

    if successful createtracker success
    if unsuccessful createtracker fail
    if file exits in tracker list createtracker ferr

"""
<updatetracker filename start_bytes end_bytes ip-address port-number>\n
updatetracker: message from tracker server to the peer program
if tracker file does not exist: <updatetracker filename ferr>\n
if tracker file update successful: <updatetracker filename succ>\n
any other error / unable to update tracker file: <updatetracker filename fail>\n
"""
def UpdateTracker(socket) # message from peer to the tracker server

    socket.recieve filename


"""
<REQ LIST>\n
In reply to the LIST request the server reply message structure must be:
<REP LIST X>\n
<1 file1name file1size file1MD5>\n
<2 file2name file2size file2MD5>\n
...
<x fileXname fileXsize fileXMD5>\n
<REP LIST END>\n
"""

def LIST()  """ his command is sent by a connected peer to the tracker server to send over to
                the requesting peer the list of (tracker) files in the shared directory at the server. The
                format of the incoming message from the connected peer will be """

    file open("trackerlist.txt",'rb')
    reading = file.read(1024)
    while(reading):
        connectionSocket.send(reading)
        reading = file.read(1024)
    file.close()



"""
<GET filename.track >\n
The server's response to the GET command must be:
<REP GET BEGIN>\n
<tracker_file_content >\n
<REP GET END FileMD5>\n
"""
def GET()   """ For mid-term demo, you can download the requested file from either the tracker
                server or from another machine (make sure the file is already in that machine). """


    bool failure = false
    socket.recieve filename
    open tracker list file

    for every line in tracker list file
        if filename == line
            print found file
        else
            failure = true

    if failure == false
        connectionSocket.send("found file")
        statinfo = os.stat(filename)  #If the file being requested isn't in the tracker list
        filesize = statinfo.st_size  #Then check in the folder to see if the file still exists
        print filesize
        if filesize > 0
            failure = 0
        else

        if failure == 0
            file = open(filename,'rb')
            reading = file.read(1024)
            while(reading):
                Socket.send()
                reading = file.read(1024)
            file.close
        else:
            Socket.send()
        connectionSocket.close()
