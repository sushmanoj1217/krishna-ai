import time
from core.router import handle_telegram
from core.scheduler import start_scheduler

if __name__ == "__main__":
    print("🚀 Krishna AI starting...")
    start_scheduler()
    while True:
        handle_telegram()
        time.sleep(5)