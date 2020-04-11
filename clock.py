from apscheduler.schedulers.blocking import BlockingScheduler
from InstagramBot import InstagramBot
import main
import os
sched = BlockingScheduler()
bot = None
isLoggedIn = False


def setup():
    ig_username = os.environ.get("IG_USERNAME")
    ig_password = os.environ.get("IG_PASSWORD")
    global bot, isLoggedIn
    bot = InstagramBot(ig_username, ig_password)
    bot.signIn()
    bot.gotoAccountEditPage()
    isLoggedIn = True


def update():
    global bot, isLoggedIn
    try:
        bot.editBio(main.getBioData())
        print("update success")
    except:

        print("update failed")
        bot.closeBrowser()
        isLoggedIn = False


@sched.scheduled_job('interval', minutes=10)
def timed_job():
    print("running clock")
    if(not isLoggedIn):
        setup()
        update()
    else:
        update()


sched.start()
