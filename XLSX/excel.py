import re
from pathlib import Path

import dateparser

from Contact import Contact
from UTILS.translit import replace_month_to_number
from XLSX.my_excel import read_excel_file
from config import OUT_DIR, FILE_XLSX


def get_contact_from_cer_excel(filename=FILE_XLSX) -> list[Contact]:
    rows = read_excel_file(filename).get('Экзамены')
    contacts = []
    for row in rows:
        contact = Contact()
        # "№ сертификата	Дата экзамена	Курс	ФИО слушателя на русском	ФИО слушателя на латинице	email	Полное название	Английское название"
        try:
            contact.number = int(clean_export_excel(row[0]))
            contact.date_exam = dateparser.parse(clean_export_excel(row[1]), settings={'DATE_ORDER': 'DMY'})
            contact.abr_exam = clean_export_excel(row[2])
            contact.name_rus = clean_export_excel(row[3])
            contact.name_eng = clean_export_excel(row[4])
            contact.email = clean_export_excel(row[5])
            contact.exam_rus = clean_export_excel(row[6])
        except (ValueError, IndexError):
            continue
        try:
            contact.can_create_cert = clean_export_excel(row[11])
            '''"Создать сертификат? 
                1 - создать,
                [пусто] - автоматически создается после 2 дней, 
                9 - не создавать"
            '''
        except (ValueError, IndexError):
            contact.can_create_cert = 0
        try:
            contact.template = contact.abr_exam + '.png'
            date_exam = f"{contact.date_exam.strftime('%Y-%m-%d')}"
            date_exam = date_exam.replace(' ', '')
            date_exam = replace_month_to_number(date_exam)
            date_exam = str('.'.join(date_exam.split('.')[::-1]))
            contact.dir_name = date_exam

            contact.file_out_png = Path(OUT_DIR, contact.date_exam.strftime('%Y'),
                                        contact.date_exam.strftime('%m'),
                                        f"{contact.abr_exam}_{date_exam}_{contact.name_rus}"
                                        f"_{contact.number}_{contact.email}.png")
            contacts.append(contact)
        except (ValueError, IndexError, AttributeError):
            continue
    return contacts


def clean_export_excel(s):
    s = str(s)
    s = s.replace(',', ', ')
    s = re.sub(r'\s{2,}', ' ', s)
    s = s.strip()
    if s in ('None', '#N/A'):
        s = ''
    return s
