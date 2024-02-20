from flask_socketio import SocketIO
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.redis import RedisJobStore


jobstores = {
    'default': RedisJobStore(
        host='redis',
        port=6379,
        db=0
    )
}


scheduler = BackgroundScheduler(jobstores=jobstores, timezone="america/sao_paulo")


socketio = SocketIO()