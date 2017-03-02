BASE=8000

mkdir ~/Networking/ ToRun

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

mkdir ~/Networking/ToRun/Peer1/Files
mkdir ~/Networking/ToRun/Peer1/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer1/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer1/
mkdir ~/Networking/ToRun/Peer2/Files
mkdir ~/Networking/ToRun/Peer2/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer2/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer2/
mkdir ~/Networking/ToRun/Peer3/Files
mkdir ~/Networking/ToRun/Peer3/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer3/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer3/
mkdir ~/Networking/ToRun/Peer4/Files
mkdir ~/Networking/ToRun/Peer4/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer4/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer4/
mkdir ~/Networking/ToRun/Peer5/Files
mkdir ~/Networking/ToRun/Peer5/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer5/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer5/
mkdir ~/Networking/ToRun/Peer6/Files
mkdir ~/Networking/ToRun/Peer6/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer6/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer6/
mkdir ~/Networking/ToRun/Peer7/Files
mkdir ~/Networking/ToRun/Peer7/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer7/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer7/
mkdir ~/Networking/ToRun/Peer8/Files
mkdir ~/Networking/ToRun/Peer8/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer8/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer8/
mkdir ~/Networking/ToRun/Peer9/Files
mkdir ~/Networking/ToRun/Peer9/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer9/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer9/
mkdir ~/Networking/ToRun/Peer10/Files
mkdir ~/Networking/ToRun/Peer10/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer10/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer10/
mkdir ~/Networking/ToRun/Peer11/Files
mkdir ~/Networking/ToRun/Peer11/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer11/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer11/
mkdir ~/Networking/ToRun/Peer12/Files
mkdir ~/Networking/ToRun/Peer12/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer12/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer12/
mkdir ~/Networking/ToRun/Peer13/Files
mkdir ~/Networking/ToRun/Peer13/Trackers
cp ~/StoredStuff/client.py ~/Networking/ToRun/Peer13/
cp ~/StoredStuff/client_config.cfg ~/Networking/ToRun/Peer13/

cp ~/StoredStuff/threaded_server.py ~/Networking/ToRun/TrackingServer/

#start server
python ~/Networking/server.py BASE

while IFS='' read -r line || [ -n "$line" ]; 
do
    echo "$line" >> '../StoredStuff/client_config.cfg'
done < "../StoredStuff/server_ip.txt"

python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_1_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_2_(itself)>



python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_3_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_4_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_5_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_6_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_7_(itself)>





python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_8_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_9_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_10_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_11_(itself)>
python ~/Networking/client.py <ip_of_server> <port_number of server> <port_number_of_client_12_(itself)>



