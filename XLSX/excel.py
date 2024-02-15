import re

from openpyxl import load_workbook

from Contact import Contact
from config import FILE_XLSX, columns, PAGE_NAME, OUT_DIR
from utils.translit import replace_month_to_number


def get_contact_from_excel(rows_excel: list[int] = [2, ]) -> list[Contact]:
    # Прочитать XLSX file -> [Contacts]
    filename = FILE_XLSX
    file_excel = load_workbook(filename=filename, data_only=True)
    contacts = []
    for i in range(2, 10000):
        contact = Contact()
        try:
            contact.number = int(clean_export_excel(read_excel(file_excel, column=columns['Number'], row=i)))
            contact.abr_exam = clean_export_excel(read_excel(file_excel, column=columns['AbrExam'], row=i))
            contact.email = clean_export_excel(read_excel(file_excel, column=columns['Email'], row=i))
            contact.name_rus = clean_export_excel(read_excel(file_excel, column=columns['NameRus'], row=i))
            contact.name_eng = clean_export_excel(read_excel(file_excel, column=columns['NameEng'], row=i))
            contact.date_exam = clean_export_excel(read_excel(file_excel, column=columns['DateExam'], row=i))
            contact.template = contact.abr_exam + '.png'
            if contact.email in ('', None):
                continue
        except Exception as e:
            print(e)
            continue
        # Создаем папки по курсам
        dir_name = f"{contact.date_exam}"
        dir_name = dir_name.replace(' ', '')
        dir_name = replace_month_to_number(dir_name)
        dir_name = str('.'.join(dir_name.split('.')[::-1]))
        contact.dir_name = dir_name

        certificate = 'Сертификат'

        file_out_png = f"{OUT_DIR}{dir_name}/{certificate}_{dir_name}_" \
                       f"{contact.name_rus}_{contact.number}_{contact.email}.png"

        file_out_png = file_out_png.replace(' ', '_')
        file_out_png = replace_month_to_number(file_out_png)
        contact.file_out_png = file_out_png

        contacts.append(contact)

    return contacts


def read_excel(excel, column, row):
    sheet_ranges = excel[PAGE_NAME]
    return str(sheet_ranges[f'{column}{row}'].value)


def clean_export_excel(s):
    s = s.replace(',', ', ')
    s = re.sub(r'\s{2,}', ' ', s)
    s = s.strip()
    if s in ('None', '#N/A'):
        s = ''
    return s
