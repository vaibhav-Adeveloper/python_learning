import datetime
import time

try:
    while True:
        current_Time = datetime.datetime.now()
        print(f"\rCurrent Time: {current_Time}", end='', flush=True)
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock Stopped")