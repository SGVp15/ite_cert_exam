import pandas as pd

from Contact import Contact
from config import OUT_DIR, FILE_XLSX
from utils.translit import replace_month_to_number


def get_contact_from_excel(filename=FILE_XLSX) -> list[Contact]:
    df = pd.DataFrame(pd.read_excel(filename, sheet_name=0, ))
    df = df.dropna()
    contacts = []
    for row in df.values:
        contact = Contact()
        # "№ сертификата	Дата экзамена	Курс	ФИО слушателя на русском	ФИО слушателя на латинице	email	Полное название	Английское название"
        contact.number = int(clean_export_excel(row[0]))
        contact.date_exam = clean_export_excel(row[1])
        contact.abr_exam = clean_export_excel(row[2])
        contact.name_rus = clean_export_excel(row[3])
        contact.name_eng = clean_export_excel(row[4])
        contact.email = clean_export_excel(row[5])
        contact.exam_rus = clean_export_excel(row[6])

        contact.template = contact.abr_exam + '.png'
        date_exam = f"{contact.date_exam}"
        date_exam = date_exam.replace(' ', '')
        date_exam = replace_month_to_number(date_exam)
        date_exam = str('.'.join(date_exam.split('.')[::-1]))
        contact.dir_name = date_exam

        certificate = 'Сертификат'

        file_out_png = f"{OUT_DIR}/{date_exam}/{certificate}_{contact.abr_exam}_{date_exam}_" \
                       f"{contact.name_rus}_{contact.number}_{contact.email}.png"

        contact.file_out_png = file_out_png

        contacts.append(contact)
    return contacts


def clean_export_excel(s):
    s = str(s)
    s = s.replace(',', ', ')
    # s = re.sub(r'\s{2,}', ' ', s)
    s = s.strip()
    if s in ('None', '#N/A'):
        s = ''
    return s
