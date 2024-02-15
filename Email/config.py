from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

EMAIL_LOGIN = config['EMAIL_LOGIN']
EMAIL_PASSWORD = config['EMAIL_PASSWORD']

SMTP_SERVER = 'smtp.yandex.ru'
SMTP_PORT = 465
EMAILS_SELLER = ['a.katkov@itexpert.ru', 'a.rybalkin@itexpert.ru', 'g.savushkin@itexpert.ru']
