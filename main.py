import os
import pickle
import time

import logging

from Contact import Contact
from Email import EmailSending
from XLSX.excel import get_contact_from_excel
from config import OUT_DIR, pickle_users, FILE_XLSX, pickle_file_modify
from create_png import create_png
from utils.Progress_bar import progress

logging.basicConfig(level=logging.INFO, filename="log.txt", filemode="a",
                    format="%(asctime)s %(levelname)s %(message)s")


def main():
    old_users = []
    new_users = []

    new_users = get_contact_from_excel()

    try:
        user: Contact
        old_users = pickle.load(open(pickle_users, 'rb'))
    except FileNotFoundError as e:
        logging.error(e)

    new_users = [user for user in new_users if user not in old_users]

    for contact in new_users:
        os.makedirs(os.path.join(OUT_DIR, contact.dir_name), exist_ok=True)

    for i, user in enumerate(new_users):
        os.makedirs(os.path.join(OUT_DIR, user.dir_name), exist_ok=True)
        create_png(user)
        print(f'[{i + 1}/{len(new_users)}]\t{user.file_out_png}')
        logging.info(f'[{i + 1}/{len(new_users)}]\t{user.file_out_png}')

    files_cert = []
    for user in new_users:
        files_cert.append(user.file_out_png)
    if files_cert:
        EmailSending(to=['an.kuznetsov@itexpert.ru'], cc=['g.savushkin@itexpert.ru', 'o.kuprienko@itexpert.ru'],
                     subject='Сертификаты', files_path=files_cert).send_email()
        logging.info(
            f"EmailSending to=['an.kuznetsov@itexpert.ru'], cc=['g.savushkin@itexpert.ru', 'o.kuprienko@itexpert.ru']")
    all_users = [*new_users, *old_users]
    pickle.dump(all_users, open(pickle_users, 'wb'))

    for user in new_users:
        text = f"""Добрый день, {user.name_rus}!
Проверка пройдена, Вы успешно сдали экзамен "{user.exam_rus}", поздравляем!
Сертификат будет загружен в ЛК IT Expert в раздел "Мои экзамены" в течение недели.
"""
        EmailSending(to=[user.email, ], bcc=['g.savushkin@itexpert.ru', 'o.kuprienko@itexpert.ru'],
                     subject=f'Экзамен "{user.abr_exam}" проверка пройдена', text=text).send_email()
        time.sleep(1)
        logging.info(f'EmailSending {user.email}')


def get_time_file_modify_old():
    try:
        info = pickle.load(open(pickle_file_modify, 'rb'))
    except FileNotFoundError:
        return ''
    return info


if __name__ == '__main__':
    _sleep_time = 60
    while True:
        while True:
            time_file_modify = get_time_file_modify_old()
            time_file_modify_now = 0
            try:
                time_file_modify_now = os.path.getmtime(FILE_XLSX)
            except (FileNotFoundError, IOError) as e:
                print(e)

            if time_file_modify != time_file_modify_now:
                break
            for i in range(_sleep_time):
                progress(text='sleep ', percent=int(i * 100 / _sleep_time))
                time.sleep(1)
        try:
            main()
            pickle.dump(os.path.getmtime(FILE_XLSX), open(pickle_file_modify, 'wb'))
        except Exception as e:
            logging.error(e)
