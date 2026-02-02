import pickle
import time
from pathlib import Path

from CertContact import CertContact
from UTILS.Progress_bar import progress
from UTILS.log import log
from XLSX.excel import get_contact_from_cer_excel
from config import PICKLE_USERS, PICKLE_FILE_MODIFY, FILE_XLSX, SLEEP_SECONDS
from create_png import create_png


def load_old_users():
    old_users = []
    try:
        old_users = pickle.load(open(PICKLE_USERS, 'rb'))
    except FileNotFoundError as e:
        log.error(e)
    return old_users


def main():
    old_users = load_old_users()
    print(f'old_users: {len(old_users)}\n')
    new_users = get_contact_from_cer_excel()
    new_users = [user for user in new_users if user not in old_users]
    print(f'new_users: {len(new_users)}\n')

    for contact in new_users:
        contact.file_out_png.parent.mkdir(parents=True, exist_ok=True)

    successful_users = []
    for i, contact in enumerate(new_users):
        try:
            create_png(contact)
            log.info(f'[{i + 1}/{len(new_users)}]\t{contact.file_out_png}')
            successful_users.append(contact)
        except FileNotFoundError as e:
            log.error(f'{e} [{i + 1}/{len(new_users)}]\t{contact.file_out_png}')

    if len(successful_users) > 0:
        all_users = [*successful_users, *old_users]
        pickle.dump(all_users, open(PICKLE_USERS, 'wb'))
        log.info('[Create PICKLE_USERS]')


def get_time_file_modify_old():
    try:
        info = pickle.load(open(PICKLE_FILE_MODIFY, 'rb'))
    except (FileNotFoundError, IOError):
        return ''
    return info


if __name__ == '__main__':
    time_file_modify = 0
    while True:
        time_file_modify_now = Path(FILE_XLSX).stat().st_mtime

        if time_file_modify != time_file_modify_now:
            try:
                main()
            except Exception as e:
                log.error(e)
            time_file_modify = time_file_modify_now

        for i in range(SLEEP_SECONDS):
            progress(text='sleep ', percent=int(i * 100 / SLEEP_SECONDS))
            time.sleep(1)
