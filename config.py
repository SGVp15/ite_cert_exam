import os

BASE_PATH = os.path.join('//192.168.20.100', 'Administrative server', 'РАБОТА АДМИНИСТРАТОРА',
                         'ОРГАНИЗАЦИЯ IT ЭКЗАМЕНОВ', 'ЭКЗАМЕНЫ ЦИФРОВОЙ ПУТЬ')
FILE_XLSX = os.path.join(BASE_PATH, 'Нумерация_Экзамены.xlsx')
OUT_DIR = os.path.join(BASE_PATH, 'сертификаты')
TEMPLATE_FOLDER = os.path.join(BASE_PATH, 'templates')

SEND_EMAIL = True
EMAIL_WEB_MANAGER = ['an.kuznetsov@itexpert.ru', ]
EMAIL_BCC = ['exam@itexpert.ru', ]

os.makedirs(OUT_DIR, exist_ok=True)

LOG_FILE = './log.txt'

PICKLE_USERS = './users.pk'
PICKLE_FILE_MODIFY = './time_file_modify.pk'
