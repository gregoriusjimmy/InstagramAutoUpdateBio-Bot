from apscheduler.schedulers.blocking import BlockingScheduler
import main
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=10)
def timed_job():
    print("running main")
    main.updateBio()


sched.start()
