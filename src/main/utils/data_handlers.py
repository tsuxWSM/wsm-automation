from datetime import datetime, timedelta
from random import randint


class DateTimeHandler:

    @staticmethod
    def get_future_date_usa_format():
        """Returns a random date in range of ten days from current date and returns it in USA date format"""
        days = randint(1, 10)
        return datetime.date(datetime.now() + timedelta(days=days)).strftime('%m/%d/%Y')

    @staticmethod
    def get_past_date_usa_format():
        """Returns a random date in range of ten days from current date and returns it in USA date format"""
        days = randint(1, 10)
        return datetime.date(datetime.now() - timedelta(days=days)).strftime('%m/%d/%Y')

    @staticmethod
    def is_past_date(str_date: str):
        date_format = '%m/%d/%Y'
        return datetime.now() > datetime.strptime(str_date, date_format)
