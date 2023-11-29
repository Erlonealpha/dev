import requests
from bs4 import BeautifulSoup
from ping3 import ping, verbose_ping
from concurrent.futures import ThreadPoolExecutor
import os

def respone_(ip):
    respones = requests.get(f'https://{ip}')
    if respones.status_code == 200:
        soup = BeautifulSoup(respones, 'html.parser')
        soup.title.string.strip() if soup.title else 'not title'

def ping_ip(ip):
    sec = ping(ip, timeout=0.05)
    if sec:
        re_ip_list.append(ip)
        print(f'{ip} is reabled, time: {sec}')
    else:
        ip_ =int(ip.split('.')[3])
        if ip_ % 20 == 0:
            print(f"{ip} is not reabled")


def main_ping():
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(ping_ip, ip) for ip in ip_list]
    for future in futures:
        future.result()


if __name__ == '__main__':
    tr = 18
    ip_list = []
    re_ip_list = []
    content_dict = {}
    ip_list =[f'172.{tr}.{x}.{y}' for x in range(1,256) for y in range(1,256)]

    main_ping()
    if os.path.exists('./work'):
        os.mkdir('./work')
    with open('./work') as f:
        for ip in ip_list:
            f.write(f'{ip}\n')