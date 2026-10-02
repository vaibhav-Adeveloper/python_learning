import datetime
import time
import threading
import sys

def pythonLearn():
    future_date = datetime.datetime(2025, 6, 30, 12, 30, 30)
    while True:
        time_left = future_date - datetime.datetime.now()
        if time_left.total_seconds() <= 0:
            break
        # Save cursor, move to line 1, update
        sys.stdout.write("\033[s")  # Save cursor position
        sys.stdout.write("\033[1;1H")  # Move to row 1, column 1
        sys.stdout.write(f"\rPython Countdown: {str(time_left).split('.')[0]}   ")
        sys.stdout.write("\033[u")  # Restore cursor position
        sys.stdout.flush()
        time.sleep(1)

def webDLearn():
    future_date = datetime.datetime(2025, 7, 30, 12, 30, 30)
    while True:
        time_left = future_date - datetime.datetime.now()
        if time_left.total_seconds() <= 0:
            break
        # Save cursor, move to line 2, update
        sys.stdout.write("\033[s")
        sys.stdout.write("\033[2;1H")  # Move to row 2, column 1
        sys.stdout.write(f"\rMERN Countdown:   {str(time_left).split('.')[0]}   ")
        sys.stdout.write("\033[u")
        sys.stdout.flush()
        time.sleep(1)

# Print 2 blank lines to reserve space
print("\n" * 2)

# Start both countdowns in parallel
t1 = threading.Thread(target=pythonLearn)
t2 = threading.Thread(target=webDLearn)

t1.start()
t2.start()

t1.join()
t2.join()

print("\nBoth countdowns completed.")
