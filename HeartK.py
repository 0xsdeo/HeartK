# -*- coding: UTF-8 -*-
# @Project ：HeartK 
# @File    ：HeartK.py
# Author   ：0xsdeo
# Date     ：2025/1/17 14:48
import os
import json
import execjs
import chardet
import argparse


def print_data_count(js, data):
    print(f'{js}共搜索到：' +
          (str(len(data['sfz'])) + '个sfz\t' if data['sfz'] is not None else "0个sfz\t") +
          (str(len(data['mobile'])) + '个mobile\t' if data['mobile'] is not None else "0个mobile\t") +
          (str(len(data['mail'])) + '个mail\t' if data['mail'] is not None else "0个mail\t") +
          (str(len(data['ip'])) + '个ip\t' if data['ip'] is not None else "0个ip\t") +
          (str(len(data['ip_port'])) + '个ip_port\t' if data['ip_port'] is not None else "0个ip_port\t") +
          (str(len(data['domain'])) + '个domain\t' if data['domain'] is not None else "0个domain\t") +
          (str(len(data['path'])) + '个path\t' if data['path'] is not None else "0个path\t") +
          (str(len(data['incomplete_path'])) + '个incomplete_path\t' if data['incomplete_path'] is not None else "0个incomplete_path\t") +
          (str(len(data['url'])) + '个url\t' if data['url'] is not None else "0个url\t") +
          (str(len(data['jwt'])) + '个jwt\t' if data['jwt'] is not None else "0个jwt\t") +
          (str(len(data['algorithm'])) + '个algorithm\t' if data['algorithm'] is not None else "0个algorithm\t") +
          (str(len(data['secret'])) + '个secret\t' if data['secret'] is not None else "0个secret\t") +
          (str(len(data['static'])) + '个static\t' if data['static'] is not None else "0个static\t")
          )


def Data_Deduplication(key, info_dict):  # 数据去重
    if info_dict[key] is not None and isinstance(info_dict[key], list):
        info_dict[key] = list(set(info_dict[key]))


def Detection_encoding(path):  # 获取文件编码
    with open(path, mode='rb') as f:
        data = f.read()
        return chardet.detect(data)['encoding']


def add_data(key, value, info_dict):  # 将js_info_list列表中的每个敏感信息都放到一个字典里
    if value is not None and info_dict[key] is None:
        info_dict[key] = value
    elif value is not None and isinstance(info_dict[key], list):
        info_dict[key].extend(value)


def scan(scan_list):
    with open("js/background.js", "r", encoding="utf-8") as background:
        background_js = execjs.compile(background.read())
        if isinstance(scan_list, list):
            for i in scan_list:
                encoding = Detection_encoding(i)
                if encoding is not None:
                    try:
                        with open(f"{i}", "r", encoding=encoding) as f:
                            info = background_js.call("get_info", f.read())
                            js_info_list.append(info)
                            print_data_count(i, info)
                    except UnicodeDecodeError as u:
                        print(f"{i}文件编码获取失败：,{u}")
                    except Exception as e:
                        print(f"scan函数异常，异常信息：{e}")
                else:
                    print(f"{i}文件内容为空")
        else:
            encoding = Detection_encoding(scan_list)
            if encoding is not None:
                with open(f"{scan_list}", "r", encoding=encoding) as f:
                    info = background_js.call("get_info", f.read())
                    js_info_list.append(info)


def get_js(path):  # 获取目录下所有js文件
    file_list = os.listdir(path)
    if file_list:
        for i in file_list:
            if os.path.isdir(path + f'/{i}'):
                get_js(path + f'/{i}')
            else:
                js_list.append(path + '/' + i) if i[-3:] == ".js" or i[-5:] == '.html' else i


if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("path", help="指定要扫描的路径或单个js文件路径")
    arg = arg.parse_args()

    js_list = list()  # 以列表形式存储每个js文件路径
    js_info_list = list()  # 以列表形式存储每个js文件中的敏感信息
    all_info = {
        'sfz': None,
        'mobile': None,
        'mail': None,
        'ip': None,
        'ip_port': None,
        'domain': None,
        'path': None,
        'incomplete_path': None,
        'url': None,
        'jwt': None,
        'algorithm': None,
        'secret': None,
        'static': None
    }

    if os.path.isdir(arg.path):
        get_js(arg.path)
        scan(js_list)
        for i in js_info_list:
            for k, v in i.items():
                add_data(k, v, all_info)
        for k in all_info.keys():
            Data_Deduplication(k, all_info)
    elif os.path.isfile(arg.path):
        scan(arg.path)
        for i in js_info_list:
            for k, v in i.items():
                add_data(k, v, all_info)
        for k in all_info.keys():
            Data_Deduplication(k, all_info)
    else:
        raise ValueError("指定的路径并非有效路径")

    print(f'\033[31m此次共搜索到：' +
          (str(len(all_info['sfz'])) + '个sfz\t' if all_info['sfz'] is not None else "0个sfz\t") +
          (str(len(all_info['mobile'])) + '个mobile\t' if all_info['mobile'] is not None else "0个mobile\t") +
          (str(len(all_info['mail'])) + '个mail\t' if all_info['mail'] is not None else "0个mail\t") +
          (str(len(all_info['ip'])) + '个ip\t' if all_info['ip'] is not None else "0个ip\t") +
          (str(len(all_info['ip_port'])) + '个ip_port\t' if all_info['ip_port'] is not None else "0个ip_port\t") +
          (str(len(all_info['domain'])) + '个domain\t' if all_info['domain'] is not None else "0个domain\t") +
          (str(len(all_info['path'])) + '个path\t' if all_info['path'] is not None else "0个path\t") +
          (str(len(all_info['incomplete_path'])) + '个incomplete_path\t' if all_info['incomplete_path'] is not None else "0个incomplete_path\t") +
          (str(len(all_info['url'])) + '个url\t' if all_info['url'] is not None else "0个url\t") +
          (str(len(all_info['jwt'])) + '个jwt\t' if all_info['jwt'] is not None else "0个jwt\t") +
          (str(len(all_info['algorithm'])) + '个algorithm\t' if all_info['algorithm'] is not None else "0个algorithm\t") +
          (str(len(all_info['secret'])) + '个secret\t' if all_info['secret'] is not None else "0个secret\t") +
          (str(len(all_info['static'])) + '个static\t' if all_info['static'] is not None else "0个static\t\033[0m")
          )

    print(json.dumps(all_info))