import time

wait_time = 1
max_retry = 5
attemps = 0

while attemps < max_retry:
    attemps+=1
    print("attemps: ", attemps, "  wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2