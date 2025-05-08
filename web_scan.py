# -*- coding: UTF-8 -*-
# @Project ：HeartK 
# @File    ：web_scan.py
# Author   ：0xsdeo
# Date     ：2025/2/13 15:17
import config
import urllib3
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

urllib3.disable_warnings()


def get_host_js(host):
    try:
        re = requests.get(host, headers=config.headers, verify=False, timeout=config.wait_time)
        soup = BeautifulSoup(re.text, 'html.parser')
        script_tags = soup.find_all('script')
        link_tags = soup.find_all('link')

        src_list = []
        js_code = []
        for i in script_tags:
            src = i.get('src')
            if src:
                src_list.append(src)
            else:
                code = i.get_text(strip=True)
                if code:
                    js_code.append(code)

        for i in link_tags:
            href = i.get('href')
            if href and '.js' in href:
                src_list.append(href)

        parsed_url = urlparse(host)
        protocol = parsed_url.scheme
        index = 0
        for i in src_list:
            if i[:2] == '//':
                src_list[index] = protocol + ':' + i
            elif 'http://' in i or 'https://' in i:
                index += 1
                continue
            else:
                src_list[index] = host + '/' + i
            index += 1
    except Exception as e:
        if 'HTTPSConnectionPool' in str(e) or 'HTTPConnectionPool' in str(e):
            print(f"web_scan脚本第17行{host}请求失败")
        else:
            print(f"web_scan脚本第54行出现异常，异常信息：{e}")
        return None, None

    js_code.append(re.text)

    return src_list, js_code


def get_hostname(host):
    parsed = urlparse(host)
    netloc = parsed.netloc
    pure_domain = netloc.split(":")[0] if ":" in netloc else netloc
    if parsed.port:
        pure_domain = pure_domain + "_" + str(parsed.port)
    return pure_domain
