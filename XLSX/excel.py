import datetime
import re
from pathlib import Path

import dateparser

from Cert_Contact import Cert_Contact
from UTILS.translit import replace_month_to_number
from XLSX.my_excel import read_excel_file
from config import OUT_DIR, FILE_XLSX


def get_contact_from_cer_excel(filename=FILE_XLSX) -> list[Cert_Contact]:
    rows = read_excel_file(filename).get('Экзамены')
    cert_contacts = []
    for row in rows:
        cert_contact = Cert_Contact()
        # "№ сертификата	Дата экзамена	Курс	ФИО слушателя на русском	ФИО слушателя на латинице	email	Полное название	Английское название"
        try:
            cert_contact.number = int(clean_export_excel(row[0]))
            cert_contact.date_exam = dateparser.parse(clean_export_excel(row[1]),
                                                      settings={'DATE_ORDER': 'DMY'})
            cert_contact.abr_exam = clean_export_excel(row[2])
            cert_contact.name_rus = clean_export_excel(row[3])
            cert_contact.name_eng = clean_export_excel(row[4])
            cert_contact.email = clean_export_excel(row[5])
            cert_contact.exam_rus = clean_export_excel(row[6])
        except (ValueError, IndexError):
            continue

        if not cert_contact.date_exam:
            continue

        try:
            cert_contact.can_create_cert = clean_export_excel(row[11])
            '''"Создать сертификат? 
                1 - создать,
                [пусто] - автоматически создается после 2 дней, 
                9 - не создавать"
            '''
        except (ValueError, IndexError):
            cert_contact.can_create_cert = 0

        try:
            cert_contact.template = cert_contact.abr_exam + '.png'
            date_exam = f"{cert_contact.date_exam.strftime('%Y-%m-%d')}"

            cert_contact.file_out_png = Path(OUT_DIR, cert_contact.date_exam.strftime('%Y'),
                                             cert_contact.date_exam.strftime('%m'),
                                             f"{cert_contact.abr_exam}_{date_exam}_{cert_contact.name_rus}"
                                             f"_{cert_contact.number}_{cert_contact.email}.png")

        except (ValueError, IndexError, AttributeError):
            continue

        if datetime.datetime.now() >= cert_contact.date_exam + datetime.timedelta(days=2):
            cert_contacts.append(cert_contact)
    return cert_contacts


def clean_export_excel(s):
    s = str(s)
    s = s.replace(',', ', ')
    s = re.sub(r'\s{2,}', ' ', s)
    s = s.strip()
    if s in ('None', '#N/A'):
        s = ''
    return s
