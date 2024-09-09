import os
import pickle
import time

from UTILS.files import check_update_file_excel_decorator
from UTILS.log import log

from Contact import Contact
from Email import EmailSending
from XLSX.excel import get_contact_from_excel
from config import OUT_DIR, PICKLE_USERS, FILE_XLSX, PICKLE_FILE_MODIFY, EMAIL_BCC, EMAIL_WEB_MANAGER
from create_png import create_png
from UTILS.Progress_bar import progress


@check_update_file_excel_decorator
def main():
    old_users = []
    new_users = get_contact_from_excel()

    try:
        old_users = pickle.load(open(PICKLE_USERS, 'rb'))
    except FileNotFoundError as e:
        log.error(e)

    new_users = [user for user in new_users if user not in old_users]

    for contact in new_users:
        os.makedirs(os.path.join(OUT_DIR, contact.dir_name), exist_ok=True)

    for i, user in enumerate(new_users):
        os.makedirs(os.path.join(OUT_DIR, user.dir_name), exist_ok=True)
        create_png(user)
        log.info(f'[{i + 1}/{len(new_users)}]\t{user.file_out_png}')

    files_cert = []
    for user in new_users:
        files_cert.append(user.file_out_png)

    if files_cert:
        try:
            EmailSending(to=EMAIL_WEB_MANAGER, cc=EMAIL_BCC,
                         subject='Сертификаты', files_path=files_cert).send_email()
            log.info(
                f"EmailSending to={EMAIL_WEB_MANAGER}, cc={EMAIL_BCC}")
        except Exception as e:
            log.error(e)

    all_users = [*new_users, *old_users]
    pickle.dump(all_users, open(PICKLE_USERS, 'wb'))

    for user in new_users:
        text = f"""Добрый день, {user.name_rus}!
Проверка пройдена, Вы успешно сдали экзамен "{user.exam_rus}", поздравляем!
Сертификат будет загружен в ЛК IT Expert в раздел "Мои экзамены" в течение недели.
"""
        try:
            EmailSending(to=[user.email, ], bcc=EMAIL_BCC,
                         subject=f'Вы успешно сдали экзамен {user.abr_exam}.', text=text).send_email()
            log.info(
                f"EmailSending to= {user.email},bcc={EMAIL_BCC}")
        except Exception as e:
            log.error(e)

        time.sleep(1)


def get_time_file_modify_old():
    try:
        info = pickle.load(open(PICKLE_FILE_MODIFY, 'rb'))
    except (FileNotFoundError, IOError):
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
            pickle.dump(os.path.getmtime(FILE_XLSX), open(PICKLE_FILE_MODIFY, 'wb'))
        except Exception as e:
            log.error(e)
