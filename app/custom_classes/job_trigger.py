from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger


class BuildInJobTrigger(object):
    def __new__(cls, trigger, cron_enable, **kwargs):
        register = {}
        register["Interval"] = IntervalTrigger
        print(list(kwargs.values()))
        register["Date"] = DateTrigger
        if cron_enable:
            register["Cron"] = CronTrigger.from_crontab(list(kwargs.values())[0])
            return register["Cron"]
        else:
            register["Cron"] = CronTrigger
        return register[trigger](**kwargs)
