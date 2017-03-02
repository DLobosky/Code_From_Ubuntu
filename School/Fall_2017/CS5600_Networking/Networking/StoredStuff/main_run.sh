# Global constant for the base port number and the heartbeat
BASE=8000
HEART_BEAT=60

# Makes the ToRun folder
mkdir ~/Networking/ ToRun

# Makes all the peer folders in ToRun
mkdir ~/Networking/ToRun/Peer1
mkdir ~/Networking/ToRun/Peer2
mkdir ~/Networking/ToRun/Peer3
mkdir ~/Networking/ToRun/Peer4
mkdir ~/Networking/ToRun/Peer5
mkdir ~/Networking/ToRun/Peer6
mkdir ~/Networking/ToRun/Peer7
mkdir ~/Networking/ToRun/Peer8
mkdir ~/Networking/ToRun/Peer9
mkdir ~/Networking/ToRun/Peer10
mkdir ~/Networking/ToRun/Peer11
mkdir ~/Networking/ToRun/Peer12
mkdir ~/Networking/ToRun/Peer13
mkdir ~/Networking/ToRun/TrackingServer

#Makes the File and Trackers folders for each peer and the client.py and config file to each peer
mkdir ~/Networking/ToRun/Peer1/Files
mkdir ~/Networking/ToRun/Peer1/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer1/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer1/
mkdir ~/Networking/ToRun/Peer2/Files
mkdir ~/Networking/ToRun/Peer2/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer2/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer2/
mkdir ~/Networking/ToRun/Peer3/Files
mkdir ~/Networking/ToRun/Peer3/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer3/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer3/
mkdir ~/Networking/ToRun/Peer4/Files
mkdir ~/Networking/ToRun/Peer4/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer4/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer4/
mkdir ~/Networking/ToRun/Peer5/Files
mkdir ~/Networking/ToRun/Peer5/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer5/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer5/
mkdir ~/Networking/ToRun/Peer6/Files
mkdir ~/Networking/ToRun/Peer6/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer6/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer6/
mkdir ~/Networking/ToRun/Peer7/Files
mkdir ~/Networking/ToRun/Peer7/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer7/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer7/
mkdir ~/Networking/ToRun/Peer8/Files
mkdir ~/Networking/ToRun/Peer8/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer8/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer8/
mkdir ~/Networking/ToRun/Peer9/Files
mkdir ~/Networking/ToRun/Peer9/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer9/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer9/
mkdir ~/Networking/ToRun/Peer10/Files
mkdir ~/Networking/ToRun/Peer10/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer10/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer10/
mkdir ~/Networking/ToRun/Peer11/Files
mkdir ~/Networking/ToRun/Peer11/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer11/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer11/
mkdir ~/Networking/ToRun/Peer12/Files
mkdir ~/Networking/ToRun/Peer12/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer12/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer12/
mkdir ~/Networking/ToRun/Peer13/Files
mkdir ~/Networking/ToRun/Peer13/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer13/
cp ~/StoredStuff/client.cfg ~/Networking/ToRun/Peer13/

# Copies the threaded_server.py file to the TrackingServer folder in ToRun
cp ~/StoredStuff/threaded_server.py ~/Networking/ToRun/TrackingServer/


#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------

#START TIMER = 0

#start server
python ~/Networking/server.py BASE

# This takes the heartbeat from the heartbeat file and adds it to the config file
while IFS='' read -r line || [ -n "$line" ]; 
do
    echo "$line" >> 'StoredStuff/config.cfg'
done < "StoredStuff/heartbeat.txt"

# Assigning small and large files to Peer1 and Peer2
cp ~/StoredStuff/smallfile.txt ~/Networking/ToRun/Peer1/Files
cp ~/StoredStuff/test_img.jpg ~/Networking/ToRun/Peer1/Files
cp ~/StoredStuff/smallfile.txt ~/Networking/ToRun/Peer2/Files
cp ~/StoredStuff/test_img.jpg ~/Networking/ToRun/Peer2/Files


# Starts Peer1
BASE=$((BASE+1))
python ~/Networking/client.py BASE

# Determines the PID of the running client.py and sets it ProcessID_1
ProcessID_1="$(pgrep client.py)"

# Starts Peer2
BASE=$((BASE+1))
python ~/Networking/client.py BASE

# Determines the PID of the running client.py and sets it ProcessID_2
ProcessID_2="$(pgrep client.py)"


sleep 30


# Starts Peers 3 - 7
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE


sleep 60echo


# Starts Peers 8 - 13
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE
BASE=$((BASE+1))
python ~/Networking/client.py BASE


# Kills ProcessID_1
kill "${ProcessID_1}"

# Kills ProcessID_2
kill "${ProcessID_2}"




#-------------NOTES----------------

#while IFS='' read -r line || [ -n "$line" ]; 
#do
#    echo "$line" >> 'StoredStuff/Stuff_For_Testing/output.txt'
#done < "StoredStuff/client.cfg"

OUTPUT="$(ls -1)"
echo "${OUTPUT}"