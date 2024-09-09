import os

_base_path = os.path.join('//192.168.20.100', 'Administrative server', 'РАБОТА АДМИНИСТРАТОРА',
                          'ОРГАНИЗАЦИЯ IT ЭКЗАМЕНОВ', 'ЭКЗАМЕНЫ ЦИФРОВОЙ ПУТЬ')
FILE_XLSX = os.path.join(_base_path, 'Нумерация_Экзамены.xlsx')
OUT_DIR = os.path.join(_base_path, 'сертификаты')
TEMPLATE_FOLDER = os.path.join(_base_path, 'templates')

EMAIL_WEB_MANAGER = ['an.kuznetsov@itexpert.ru',]
EMAIL_BCC = ['g.savushkin@itexpert.ru', 'o.kuprienko@itexpert.ru']

os.makedirs(OUT_DIR, exist_ok=True)

LOG_FILE = './log.txt'

PICKLE_USERS = './users.pk'
PICKLE_FILE_MODIFY = './time_file_modify.pk'

