import requests
from bs4 import BeautifulSoup
from ping3 import ping, verbose_ping
from concurrent.futures import ThreadPoolExecutor

def respone_(ip):
    respones = requests.get(f'https://{ip}')
    if respones.status_code == 200:
        soup = BeautifulSoup(respones, 'html.parser')
        soup.title.string.strip() if soup.title else 'not title'

def ping_ip(ip):
    sec = ping(ip)
    if sec:
        ip_list.append(ip)
        print(f'{ip} is reabled')
    else:
        print(f"{ip} is not reabled")

def main_ping():
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(ping_ip, ip) for ip in ip_list]
    for future in futures:
        future.result()


if __name__ == '__man__':
    tr = 18
    ip_list = []
    re_ip_list = []
    content_dict = {}
    ip_list =[f'172.{tr}.{x}.{y}' for x in range(1,256) for y in range(1,256)]
    print(ip_list[:256])