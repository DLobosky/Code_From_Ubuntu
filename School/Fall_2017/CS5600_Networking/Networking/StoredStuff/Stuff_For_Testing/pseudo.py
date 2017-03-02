time = 0 seconds

start server
start peer 1
start peer 2

# Needs a config file individual to each peer

assign peer 1 small file
assign peer 2 large file

time = 30 seconds

start peer 3
start peer 4
start peer 5
start peer 6
start peer 7

download small and large files to peer 3-7

execute LIST and GET commands # All communication messages need to be printed to the machine
GET command again # For the second file


time = 90 seconds

start peer 8
start peer 9
start peer 10
start peer 11
start peer 12

time = 90 seconds

download small and large files to peer 8-12

execute LIST and GET commands # All communication messages need to be printed to the machine
GET command again # For the second file

after file download completion
terminate peer 1 and peer 2
post termination messages to the screen 



