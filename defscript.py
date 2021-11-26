# Basic script to warn about arp spoofing taking place
#!/usr/bin/env/python
from scapy.all import *
import subprocess
from getmac import get_mac_address
router_ip="192.168.1.1"
current_ip=raw_input("enter your ip")
a=ARP(op=1,pdst="192.168.1.1")
b=sr1(a)
b[0].show()
current_mac=raw_input("enter mac from above packet display :")
original_mac=b.hwsrc
while True:
          current_mac=get_mac_address(ip="192.168.1.1")
          if current_mac!=original_mac:
                           
                            helper=ARP(op=2,pdst=current_ip,psrc=router_ip)
                            send(helper)
                            fix_router=ARP(op=2,pdst="192.168.1.1")
                            send(fix_router)
                            os.system("arp -d 192.168.1.1")
                            os.system("ping 192.168.1.1")
else:
    sleep(2)

