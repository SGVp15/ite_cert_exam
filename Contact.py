import datetime
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Contact_Template:
    number: str
    abr_exam: str
    email: str
    name_rus: str
    name_eng: str
    date_exam: str
    exam_rus: str
    exam_eng: str
    file_out_png: str
    template: str
    dir_name: str


class Contact:
    def __init__(self, number: int = 0, abr_exam: str = '', email: str = '',
                 name_rus: str = '', name_eng: str = '', date_exam: datetime.datetime | None = None,
                 exam_rus: str = '', exam_eng: str = '', file_out_png: Path = '',
                 template: str = '', dir_name: str = ''):
        self.number = number
        self.abr_exam: str = abr_exam.upper()
        self.email: str = email.lower()
        self.name_rus: str = name_rus
        self.name_eng: str = name_eng
        self.date_exam: datetime.datetime = date_exam
        self.exam_rus: str = exam_rus
        self.exam_eng: str = exam_eng
        self.file_out_png: Path = file_out_png
        self.template: str = template
        self.dir_name: str = dir_name

    def __eq__(self, other):
        if (
                self.number == other.number and
                self.abr_exam == other.abr_exam and
                self.email == other.email and
                self.name_rus == other.name_rus and
                self.name_eng == other.name_eng and
                self.date_exam == other.date_exam
        ):
            return True
        return False
