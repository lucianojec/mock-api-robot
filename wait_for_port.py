import socket
import sys
import time

host = "localhost"
port = int(sys.argv[1])
timeout = 10
start = time.time()

while True:
    try:
        with socket.create_connection((host, port), timeout=1):
            print("Porta disponível!")
            sys.exit(0)
    except OSError:
        time.sleep(0.5)
        if time.time() - start > timeout:
            print("Timeout esperando pela porta.")
            sys.exit(1)
