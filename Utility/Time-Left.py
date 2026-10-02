import datetime
import time
import threading

def pythonLearn():
    try:
        future_date = datetime.datetime(2025, 6, 30, 12,30,30, 0)
        print(f"\rTime left to Command Python: {future_date - datetime.datetime.now()}", end='', flush=True)
        time.sleep(1)
        if (future_date - datetime.datetime.now()).seconds == 0:
            return
    except KeyboardInterrupt:
        print("\nYou must have command Python")
    else:
        pythonLearn()

def webDLearn():
    try:
        future_date = datetime.datetime(2025, 7, 30, 12,30,30, 0)
        print(f"\rTime left to Command MERN stack: {future_date - datetime.datetime.now()}", end='', flush=True)
        time.sleep(1)
        if (future_date - datetime.datetime.now()).seconds == 0:
            return
    except KeyboardInterrupt:
        print("\nYou must have learn MERN stack")
    else:
        webDLearn()


thread1 = threading.Thread(target=pythonLearn)
thread2 = threading.Thread(target=webDLearn)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Both function execution is finished")
