from dotenv import dotenv_values

config = dotenv_values('.env')
EMAIL_LOGIN = config['EMAIL_LOGIN']
EMAIL_PASSWORD = config['EMAIL_PASSWORD']

FILE_XLSX = '//192.168.20.100/Administrative server/РАБОТА АДМИНИСТРАТОРА/ОРГАНИЗАЦИЯ IT ЭКЗАМЕНОВ/ЭКЗАМЕНЫ ЦИФРОВОЙ ПУТЬ/Нумерация_Экзамены.xlsx'
PAGE_NAME = 'Экзамены'

columns = {
    'Number': 'A',
    'DateExam': 'B',
    'AbrExam': 'C',
    'NameRus': 'D',
    'NameEng': 'E',
    'Email': 'F',
}

# Куда отправлять Email:
Emails_managers = (
    'p.moiseenko@itexpert.ru',
    'a.katkov@itexpert.ru',
    'a.rybalkin@itexpert.ru',
    #  'g.savushkin@itexpert.ru',
)

OUT_DIR = './output/'

LOG_FILE = './log.txt'

pickle_users = './users.pk'
