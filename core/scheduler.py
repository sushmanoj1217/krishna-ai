from apscheduler.schedulers.background import BackgroundScheduler
import time

# Example scheduled jobs
def trading_job():
    print(f"[{time.strftime('%H:%M:%S')}] 📈 Trading Master job running...")

def course_job():
    print(f"[{time.strftime('%H:%M:%S')}] 🎓 Course Maker job running...")

def marketing_job():
    print(f"[{time.strftime('%H:%M:%S')}] 📢 Marketing job running...")

def website_job():
    print(f"[{time.strftime('%H:%M:%S')}] 🌐 Website Manager job running...")

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Example jobs with intervals (seconds for testing)
    scheduler.add_job(trading_job, 'interval', seconds=10, id="trading_job")
    scheduler.add_job(course_job, 'interval', seconds=15, id="course_job")
    scheduler.add_job(marketing_job, 'interval', seconds=20, id="marketing_job")
    scheduler.add_job(website_job, 'interval', seconds=25, id="website_job")

    scheduler.start()
    print("✅ Scheduler started with 4 jobs.")
