from pathlib import Path

BASE_PATH = Path(
    '//192.168.20.100/Administrative server/РАБОТА АДМИНИСТРАТОРА/ОРГАНИЗАЦИЯ IT ЭКЗАМЕНОВ/ЭКЗАМЕНЫ ЦИФРОВОЙ ПУТЬ')

FILE_XLSX = BASE_PATH / 'Нумерация_Экзамены.xlsx'
OUT_DIR = BASE_PATH / 'сертификаты'
TEMPLATE_FOLDER = BASE_PATH / 'template_cert_png'

OUT_DIR.mkdir(parents=True, exist_ok=True)

LOG_FILE = Path('./log.txt')
PICKLE_USERS = Path('./users.pk')
PICKLE_FILE_MODIFY = Path('./time_file_modify.pk')

