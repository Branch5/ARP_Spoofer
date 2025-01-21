#This is a terminal tool to spoof ARP packet flow to intervene data traversal between two devices on a network.

ARP (Address Resolution Protocol) is a protocol that allows IP addresses to be linked to MAC addresses to allow for network communication.
ARP is used so that clients can identify other connected clients on the same network and discover them and their MAC addresses.
ARP tables are stored on each computer that link IP addresses to their corresponding MAC addresses on the network.
This tool edits/updates those ARP tables to redirect the data packets to the attacker's machine.
The data packets go from the sender, through the attacker, to the receiver and vice-versa.


I used OPTPARSE at first but updated the code with ARGEPARSE for Python3 compatability.
