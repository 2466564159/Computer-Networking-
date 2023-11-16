from socket import * 
from datetime import datetime

client_socket = socket(AF_INET, SOCK_DGRAM)
RTTS = []

for i in range(1, 11):
    now = datetime.now()
    ping_str = f"Ping {i} {now.strftime('%H:%M:%S:%f')}"
    
    try:
        client_socket.settimeout(1)
        client_socket.sendto(ping_str.encode(), ('127.0.0.1', 12000))
        message = client_socket.recv(1024)
        RTT = round((datetime.now().timestamp() - now.timestamp()) * 1000, 2)
        RTTS.append(RTT)
        print(f"{message.decode()} RTT: {RTT}ms")
    except timeout:
        print("Request timed out")
        

MIN_RTT = 99999
MAX_RTT = 0
SUM_RTT = 0
for RTT in RTTS:
    if RTT > MAX_RTT:
        MAX_RTT = RTT
    elif RTT < MIN_RTT:
        MIN_RTT = RTT
    SUM_RTT = SUM_RTT + RTT
    
print(f"\nMIN_RTT: {MIN_RTT}ms\nMAX_RTT: {MAX_RTT}ms\nAVG_RTT: {SUM_RTT/len(RTTS)}ms\nPER:{(len(RTTS)/10)*100}%")