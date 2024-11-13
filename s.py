import time
import zenoh
import random

def main():
    session = zenoh.open(zenoh.Config())
    while True:
        temperature = random.uniform(20.0, 30.0)
        session.put('home/kitchen/sensor/temp', str(temperature).encode('utf-8'))
        time.sleep(2)  # Publish every 2 seconds

if __name__ == "__main__":
    main()
