import os

_base_path = os.path.join('//192.168.20.100', 'Administrative server', 'РАБОТА АДМИНИСТРАТОРА',
                          'ОРГАНИЗАЦИЯ IT ЭКЗАМЕНОВ', 'ЭКЗАМЕНЫ ЦИФРОВОЙ ПУТЬ')
FILE_XLSX = os.path.join(_base_path, 'Нумерация_Экзамены.xlsx')
OUT_DIR = os.path.join(_base_path, 'сертификаты')

LOG_FILE = './log.txt'

pickle_users = './users.pk'
pickle_file_modify = './time_file_modify.pk'

template_folder = './template'