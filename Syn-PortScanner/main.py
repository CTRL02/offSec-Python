from datetime import datetime
import math
import pyfiglet
import threading
from colorama import init, Fore, Style
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr, sr1


def redFont(text):
    text = "{}{}{}{}".format(Style.BRIGHT, Fore.RED, message, Fore.RESET)
    return text


def ScanTarget(target, start, end):
    for port in range(start, end + 1):
        packet = IP(dst=target) / TCP(dport=port, flags="S")  # packet to be sent to target
        response = sr1(packet, timeout=1, verbose=False)
        if response and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # SYN-ACK
                print(f"Port {port} is open")


def boxify(text, color):
    lines = text.split('\n')
    max_length = max(len(line) for line in lines)
    box_top = "{}{}+{}+{}".format(Fore.RESET, color, '-' * (max_length + 2), Fore.RESET)
    box_bottom = box_top
    boxed_text = ["{}{}| {} |{}".format(Fore.RESET, color, line.ljust(max_length), Fore.RESET) for line in lines]
    return "{}\n{}\n{}".format(box_top, '\n'.join(boxed_text), box_bottom)


ascii_banner = Fore.GREEN + pyfiglet.figlet_format("PORT SCANNER") + Fore.RESET
boxed_banner = boxify(ascii_banner, color=Fore.GREEN)
print(boxed_banner)
small_ascii = Fore.BLUE + pyfiglet.figlet_format("By Philo\CTRL02", font="small")
print(small_ascii)
print("\n\n\n")
message = "Please enter the target and Range of ports Port-Port: "
print(redFont(message), "\n")
Input = input()
Input = Input.split(' ')
target = Input[0]
PortRange = Input[1].split('-')
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

threads = []
NoPorts = int(PortRange[1]) - int(PortRange[0])
NoThreads = NoPorts / 15  # 1 thread per 50 ports
start = int(PortRange[0])
for i in range(1, math.ceil(NoThreads) + 1):
    PortHandler = threading.Thread(target=ScanTarget, args=(target, start, start + 15))
    threads.append(PortHandler)
    PortHandler.start()
    start += 16

for thread in threads:  # ensure all threads finishes before program exits
    thread.join()


print("Scanning completed at:" + str(datetime.now()))