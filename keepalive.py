#!/usr/bin/python3
import time

i = 0
while True:
    time.sleep(5)
    i += 5
    print(f"Keepalive - {i} secs.")
