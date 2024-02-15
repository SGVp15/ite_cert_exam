import os
import pickle
import time

from Contact import Contact
from XLSX.excel import get_contact_from_excel
from config import OUT_DIR, pickle_users
from create_png import create_png


def main():
    old_users = []
    new_users = []

    try:
        new_users = get_contact_from_excel()
    except Exception as e:
        print(e)
        return

    try:
        user: Contact
        old_users = pickle.load(open(pickle_users, 'rb'))
        new_users = [user for user in new_users if user not in old_users]
    except Exception as e:
        print(e)

    for i, user in enumerate(new_users):
        os.makedirs(OUT_DIR + user.dir_name, exist_ok=True)
        create_png(user)
        print(f'[{i + 1}/{len(new_users)}]\t{user.file_out_png}')
    all_users = [*new_users, *old_users]
    pickle.dump(all_users, open(pickle_users, 'wb'))


if __name__ == '__main__':
    while True:
        os.makedirs(OUT_DIR, exist_ok=True)
        try:
            main()
            print('sleep')
            time.sleep(60)
        except Exception as e:
            print(e)
