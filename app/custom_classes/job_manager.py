import time

from db.database import SessionLocal
from app.services.scrap_news import ScrapNewsService

# from db.schemas import CharacterCreate, OcrDataUpdate, ClassLabelCreate


class BaseJobManager(object):
    def __init__(self):
        self.db = SessionLocal()

    @staticmethod
    def execute():
        pass


class PrintJobManager(BaseJobManager):
    def __init__(self):
        super().__init__()

    def print_hello_activity(self, should_run):
        """Work Flow Start"""
        print("test scheduler running......................")
        time.sleep(2)
        """Work Flow End"""

    @staticmethod
    def execute():
        PrintJobManager().print_hello_activity(should_run=True)
