# config.py

import argparse

def get_config():
    parser = argparse.ArgumentParser(description="Site Cloner with keyword injection")

    parser.add_argument("fqdn", help="FQDN сайта-донора, например: example.com")
    parser.add_argument("keyword", help="Ключевое слово для вставки в контент")
    parser.add_argument("host", help="IP или домен сервера")
    parser.add_argument("username", help="Имя пользователя SSH")
    parser.add_argument("password", help="Пароль SSH")
    parser.add_argument("deploy_path", help="Путь на сервере, куда загрузить архив, например /var/www/example")

    return parser.parse_args()
