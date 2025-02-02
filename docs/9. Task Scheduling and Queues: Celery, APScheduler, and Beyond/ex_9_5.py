from apscheduler.schedulers.background import BackgroundScheduler
import time

def my_periodic_task():
    print("Periodic task executed!")

scheduler = BackgroundScheduler()
scheduler.add_job(my_periodic_task, 'interval', seconds=5)
scheduler.start()

# Keep the script running to allow the scheduled task to execute
while True:
    time.sleep(1)
