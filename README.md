<h1 align="center">HeartK</h1>

![HeartK](https://socialify.git.ci/0xsdeo/HeartK/image?description=1&font=Jost&forks=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F174475975%3Fv%3D4&owner=1&pattern=Floating+Cogs&stargazers=1&theme=Dark)

## 项目介绍

本项目基于残笑大佬的<a href="https://github.com/momosecurity/FindSomething">FindSomething</a>插件进行的本地移植版，可对指定的目录下的所有html、js文件或单个html、js文件进行扫描并获取敏感信息，也可对指定的站点列表进行批量扫描。

## 必看说明

1. 本项目基于node.js环境，如无node.js环境请自行安装，官网：`https://nodejs.org/zh-cn/download/`
2. 工具扫描完毕后会将敏感信息导出在指定的目录或运行工具的目录下的`report.html`中。
3. 使用前请在工具根目录执行`pip install -r requirements.txt`安装依赖文件。
4. 如果没有指定导出报告的路径，批量扫描网站后的报告会自动保存到工具目录下的`web_reports`文件夹下。
5. 在config中可修改wait_time(请求网站的超时时间，默认为5秒，5秒未响应自动跳过)和请求头headers。
6. 进行批量扫描前将要扫描的站点导入到一个文本文件中，该文本文件需具有以下格式：
> 1. 每个站点需独占一行。
> 2. 每个站点必须有协议头，也就是形如`http://xxx.xxx.com`的格式。

## 快速上手

使用时必须指定要扫描的目录、js/html文件或存储了站点列表的文本文件：
```shell
HeartK.py scan_path
```

输出详细信息指定-d，可选项：
```shell
HeartK.py scan_path -d
```

指定要导出报告的路径，不指定默认导出在运行工具的目录下，可选项：
```shell
HeartK.py scan_path -e export_path
```
或
```shell
HeartK.py scan_path --export export_path
```

## 注意事项

1. **如要指定导出报告的路径，只写目录即可，不要指定文件名。**
2. 本项目导出的报告中移除了残笑大佬的配置项：
![1737379288373](image/README/1737379288373.png)
3. **网站请求失败或js请求失败可能是由于触发了风控机制导致的。**

## 本地扫描效果图

![1737378610051](image/README/1737378610051.png)
![1737378564084](image/README/1737378564084.png)

## 批量扫描网站效果图

![1739632689415](image/README/1739632689415.png)
![1739632646313](image/README/1739632646313.png)
![1739632731222](image/README/1739632731222.png)

## 鸣谢

本项目离不开残笑大佬的帮助与支持，在此鸣谢。

## Contact

如有bug或其他问题可提交issues，或者关注公众号Spade sec联系我。

## 更新历史

- v1.1.1

> 修复了<a href="https://github.com/0xsdeo/HeartK/issues/3">输出的报告文件命名不规范</a>的问题，现扫描同个ip的不同端口的url时，导出的报告文件名会将端口号加在文件名的最后。

感谢`XingHuoLiaoYuanBaby`师傅提出问题。

- v1.1.0

> 新增网站批量扫描功能，支持从指定站点列表中请求并扫描获取敏感信息。

- v1.0.1

> 当遇到无法解码的字节时，忽略掉这些无法解码的字节，以防止文件读不完整。