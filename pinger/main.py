from icmplib import ping
from icmplib.exceptions import NameLookupError

target_host = "192.168.200.200"

try:
    host = ping(target_host, count=5, interval=0.2, timeout=1, privileged=False)

    if host.is_alive:
        print(f"{target_host} is alive!")
        print(f"Packets sent: {host.packets_sent}")
        print(f"Packets received: {host.packets_received}")
        print(f"Packet loss: {host.packet_loss}%")
        print(f"Average Round-Trip Time: {host.avg_rtt} ms")
    else:
        print(f"{target_host} is not reachable.")

except NameLookupError:
    print(f"Could not resolve hostname: {target_host}")
except Exception as e:
    print(f"An error occurred: {e}")