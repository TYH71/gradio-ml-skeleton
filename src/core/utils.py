'''
Python utility module
'''
from datetime import datetime
import pytz

def current_sg_time() -> datetime:
    """
    It returns the current time in Singapore
    :return: A datetime object with the current time in Singapore.
    """
    time_zone = pytz.timezone("Asia/Singapore")
    my_time = datetime.utcnow()
    return my_time.astimezone(time_zone)
