# -*- coding: UTF-8 -*-
# @Project ：HeartK 
# @File    ：HeartK.py
# Author   ：0xsdeo
# Date     ：2025/1/17 14:48
import os
import execjs
import argparse


def scan(scan_list):
    with open("js/background.js", "r", encoding="utf-8") as background:
        background_js = execjs.compile(background.read())
        for i in scan_list:
            with open(f"{i}", "r", encoding="utf-8") as f:
                info = background_js.call("get_info",f.read())
                js_info.append(info)
                print(info)


def get_js(path):
    file_list = os.listdir(path)
    if file_list:
        for i in file_list:
            if os.path.isdir(path + f'/{i}'):
                get_js(path + f'/{i}')
            else:
                js_list.append(path + '/' + i) if i[-3:] == ".js" else i


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("path", help="指定要扫描的路径")
    arg = arg.parse_args()

    js_list = list()
    js_info = list()

    if os.path.isdir(arg.path):
        get_js(arg.path)
        scan(js_list)
    else:
        raise ValueError("指定的路径并非有效路径")
