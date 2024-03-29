import os
import pickle
import time

from Contact import Contact
from Email import EmailSending
from XLSX.excel import get_contact_from_excel
from config import OUT_DIR, pickle_users, FILE_XLSX, pickle_file_modify
from create_png import create_png
from utils.Progress_bar import progress


def main():
    old_users = []
    new_users = []

    try:
        new_users = get_contact_from_excel()
    except FileNotFoundError:
        print(f"File not found: {FILE_XLSX}")
        return

    try:
        user: Contact
        old_users = pickle.load(open(pickle_users, 'rb'))
        new_users = [user for user in new_users if user not in old_users]
    except Exception as e:
        print(e)

    for i, user in enumerate(new_users):
        os.makedirs(os.path.join(OUT_DIR, user.dir_name), exist_ok=True)
        create_png(user)
        print(f'[{i + 1}/{len(new_users)}]\t{user.file_out_png}')

    files_cert = []
    for user in new_users:
        files_cert.append(user.file_out_png)
    if files_cert:
        EmailSending(to=['an.kuznetsov@itexpert.ru'], cc=['g.savushkin@itexpert.ru', 'o.kuprienko@itexpert.ru'],
                     subject='Сертификаты', files_path=files_cert).send_email()

    all_users = [*new_users, *old_users]
    pickle.dump(all_users, open(pickle_users, 'wb'))


def get_time_file_modify():
    try:
        info = pickle.load(open(pickle_file_modify, 'rb'))
    except FileNotFoundError:
        return ''
    return info


if __name__ == '__main__':
    while True:
        time_file_modify = get_time_file_modify()
        try:
            if time_file_modify == os.path.getmtime(FILE_XLSX):
                continue
        except Exception as e:
            print(e)
        finally:
            for i in range(60):
                progress(text='sleep ', percent=int(i * 100 / 60))
                time.sleep(1)
        os.makedirs(OUT_DIR, exist_ok=True)
        try:
            main()
            pickle.dump(os.path.getmtime(FILE_XLSX), open(pickle_file_modify, 'wb'))
        except Exception as e:
            print(e)
