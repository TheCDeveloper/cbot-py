from datetime import datetime as dt
from .query import AnswerDict, QueryType


class TimeQuery(QueryType):
    __weekday = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]


    @staticmethod
    def __get_time():
        return dt.now().strftime("%I:%M %P")

    @staticmethod
    def __get_date():
        return dt.now().strftime("%A, %d %B")

    @staticmethod
    def __get_weekday():
        return dt.now().strftime("%A")


    @staticmethod
    def add(answers: AnswerDict):
        current_time = lambda: f"The current time is {TimeQuery.__get_time()}."

        answers["what is time"] = current_time
        answers["what time is it"] = current_time
        answers["what time is it now"] = current_time
        answers["what is current time"] = current_time


        current_date = lambda: f"The current date is {TimeQuery.__get_date()}."

        answers["what is date"] = current_date
        answers["what date is today"] = current_date
        answers["what is current date"] = current_date
        answers["which date is today"] = current_date
        answers["which date is now"] = current_date
        answers["which date is it"] = current_date


        current_day = lambda: f"The current day is {TimeQuery.__get_weekday()}."

        answers["what is day"] = current_day
        answers["what day is it"] = current_day
        answers["what day is today"] = current_day
        answers["which day is it"] = current_day
        answers["which day is today"] = current_day
        answers["what week day is it"] = current_day
        answers["what week day is today"] = current_day
        answers["which week day is it"] = current_day
        answers["which week day is today"] = current_day
        answers["what is week day"] = current_day
        answers["what is week day today"] = current_day
        answers["what is week day of today"] = current_day
