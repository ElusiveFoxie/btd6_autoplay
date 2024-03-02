import time
import threading

def stopwatch():
    """A simple function to simulate a stopwatch."""
    count = 0
    while True:
        print(f"Timer: {count}")
        count += 1
        time.sleep(1)  # Wait for 1 second

stopwatch_thread = threading.Thread(target=stopwatch, daemon=True)

stopwatch_thread.start()

while(True):
    time.sleep(1)