from birthday_wisher import BirthdayWisher
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

app = Flask(__name__)

bday_client = BirthdayWisher()
scheduler = BackgroundScheduler()
job = scheduler.add_job(bday_client.check_matching_dates, 'cron', day_of_week ='mon-sun', hour=0, minute=1)
scheduler.start()

@app.route('/')
def home():
    return 'application is running...'

# if __name__ == '__main__':
#     app.run()    