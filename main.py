from config import get_config
import os
import requests
from bs4 import BeautifulSoup
import random
import shutil
import zipfile
import paramiko

def download_site(_):
    print("Пропуск скачивания — сайт уже загружен локально в ./cloned")


def insert_keywords(keyword: str):
    index_path = "cloned/index.html"
    ...


def archive_site():
    print("Архивируем сайт...")
    shutil.make_archive("site", "zip", "cloned")
    print("Архив создан: site.zip")


def upload_and_extract(host, username, password, path):
    print("Подключение к серверу и загрузка...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password)

    sftp = ssh.open_sftp()
    try:
        sftp.mkdir(path)
    except:
        pass  # Если уже есть

    sftp.put("site.zip", f"{path}/site.zip")

    stdin, stdout, stderr = ssh.exec_command(f"unzip -o {path}/site.zip -d {path}")
    print(stdout.read().decode(), stderr.read().decode())

    sftp.close()
    ssh.close()
    print("Готово!")

def main():
    args = get_config()
    download_site(args.fqdn)
    insert_keywords(args.keyword)
    archive_site()
    upload_and_extract(args.host, args.username, args.password, args.deploy_path)

if __name__ == "__main__":
    main()
