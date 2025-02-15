# -*- coding: UTF-8 -*-
# @Project ：HeartK 
# @File    ：export_report.py
# Author   ：0xsdeo
# Date     ：2025/1/20 11:15
import os


def export(data, export_path, host=""):
    popup_js = r"""
    // @Date    : 2020-09-12 16:26:48
    // @Author  : residuallaugh

    var key = ["ip","ip_port","domain","path","incomplete_path","url","static","sfz","mobile","mail","jwt","algorithm","secret"]

    let messages = {
        "popupCopy": "复制",
        "popupCopyurl": "复制URL",
        "popupTipClickBeforeCopy": "请点击原页面后再复制：）"
    };

    function getMessage(key) {
        return messages[key] || "";
    }

    function init_copy() {
        var elements = document.getElementsByClassName("copy");
        if(elements){
            for (var i=0, len=elements.length|0; i<len; i=i+1|0) {
                elements[i].textContent = getMessage("popupCopy");
                let ele_name = elements[i].name;
                let ele_id = elements[i].id;
                if (ele_id == "popupCopyurl"){
                    elements[i].textContent = getMessage("popupCopyurl");
                }
                elements[i].onclick=function () {
                    var inp =document.createElement('textarea');
                    document.body.appendChild(inp)
                    var copytext = document.getElementById(ele_name).textContent;
                    // if (ele_id == "popupCopyurl"){
                    //     Promise.all([getCurrentTab().then(function x(tab){
                    //         if(tab == undefined){
                    //             alert(getMessage("popupTipClickBeforeCopy"))
                    //             return;
                    //         }
                    //         var url = new URL(tab.url)
                    //         var path_list = copytext.split('\n')
                    //         copytext = ""
                    //         for (var i = path_list.length - 1; i >= 0; i--) {
                    //             if(path_list[i][0] == '.'){
                    //                 copytext += url.origin+'/'+path_list[i]+'\n';
                    //             }else{
                    //                 copytext += url.origin+path_list[i]+'\n';
                    //             }
                    //         }
                    //         inp.value = copytext.slice(0, -1);
                    //         inp.select();
                    //         document.execCommand('copy',false);
                    //     })]).then(res=> inp.remove())
                    //     return ;
                    // }
                    inp.value = copytext;
                    inp.select();
                    document.execCommand('copy',false);
                    inp.remove();
                }
            }
        }
    };

    function show_info(result_data) {
        for (var k in key){
            if (result_data[key[k]]){
                // console.log(result_data[key[k]])
                let container = document.getElementById(key[k]);
                while((ele = container.firstChild)){
                    ele.remove();
                }
                container.style.whiteSpace = "pre";
                for (var i in result_data[key[k]]){
                    let tips = document.createElement("div");
                    tips.setAttribute("class", "tips")
                    let link = document.createElement("a");
                    // let source = result_data['source'][result_data[key[k]][i]];
                    // if (source) {
                    //     //虽然无法避免被xss，但插件默认提供了正确的CSP，这意味着我们即使不特殊处理，javascript也不会被执行。
                    //     // source = 'javascript:console.log`1`'
                    //     link.setAttribute("href", source);
                    //     link.setAttribute("title", source);
                    // }
                    link.appendChild(tips);
                    let span = document.createElement("span");
                    span.textContent = result_data[key[k]][i]+'\n';
                    container.appendChild(link);
                    container.appendChild(span);
                }
            }
        }
    }

    init_copy();

    show_info(""" + data + ')'

    report_html = r"""<!--  
@Date    : 2020-09-12 16:26:48
@Author  : residuallaugh 
-->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
</head>
<body style="width:780px; font-size: 14px;">
    <div style="width:780px; height: 30px; margin-left: 15px;">
        <a href="report.html"><div id="Zhuye" style="width: 55px; height: 28px; float: left; text-align: center; line-height: 28px; font-size: 14px; background: #000000; color: #ffffff; border: 1px solid black;border-radius: 2px 0px 0px 2px;">主页</div></a>
    </div>
    <div style="width:780px; height: 800px; margin-left: 15px;">
        <div id="taskstatus" style="height: 34px; line-height: 34px;"></div>
        <div style="width: 256px; float: left; border-right: 1px solid #e8e8e8;">
            <div class="findsomething_title" id="popupIp">IP</div><button type="button" class="copy" name="ip">复制</button>
            <p id="ip" style="word-break:break-word;">🈚️</p>
            <div class="findsomething_title" id="popupIpPort">IP_PORT</div><button class="copy" name="ip_port">复制</button>
            <p id="ip_port" style="word-break:break-word;">🈚️</p>
            <div class="findsomething_title" id="popupDomain">域名</div><button class="copy" name="domain">复制</button>
            <p id="domain" style="word-break:break-word;">🈚️</p>
            <div class="findsomething_title" id="popupSfz">身份证</div><button class="copy" name="sfz">复制</button>
            <p id="sfz" style="">🈚️</p>
            <div class="findsomething_title" id="popupMobile">手机号</div><button class="copy" name="mobile">复制</button>
            <p id="mobile" style="">🈚️</p>
            <div class="findsomething_title" id="popupMail">邮箱</div><button class="copy" name="mail">复制</button>
            <p id="mail" style="">🈚️</p>
            <div class="findsomething_title" id="popupJwt">JWT<button class="copy" name="jwt">复制</button></div>
            <p id="jwt" style="word-break:break-word;">🈚️</p>
            <div class="findsomething_title" id="popupAlgorithm">算法</div><button class="copy" name="algorithm">复制</button>
            <p id="algorithm" style="">🈚️</p>
            <div class="findsomething_title" id="popupSecret">Secret</div><button class="copy" name="secret">复制</button>
            <p id="secret" style="">🈚️</p>
        </div>
        <div style="width: 480px; height: 800px; float: left; margin-left:16px;">
            <div class="findsomething_title" id="popupPath">Path</div><button id="path_button" class="copy" name="path">复制</button>
            <p id="path" style="">🈚️</p>
            <div class="findsomething_title" id="popupIncompletePath">IncompletePath</div><button class="copy" name="incomplete_path">复制</button>
            <p id="incomplete_path" style="">🈚️</p>
            <div class="findsomething_title" id="popupUrl">Url</div><button class="copy" name="url">复制</button>
            <p id="url" style="">🈚️</p>
            <div class="findsomething_title" id="popupStaticPath">StaticUrl</div><button class="copy" name="static">复制</button>
            <p id="static" style="">🈚️</p>
        </div>
</div>
</body>
<!-- <script src="jquery-3.6.0.min.js"></script> -->
<!--<script src="js/popup.js"> </script>-->
<script>
    """ + popup_js + r"""
</script>
<style type="text/css">
    .copy {
        border-style: none;
        background-color: #ffffff;
        float: right;
        margin-right: 16px;
        
    }
    .findsomething_title {
        font-size: 16px;
        font-weight: bold;
        border-left: 4px solid black;
        text-indent: 4px;
        height: 16px;
        line-height: 16px;
    }
    .tips {
        display: inline-block;
        border-top: 0.2px solid;
        border-right: 0.2px solid;
        width: 10px;
        height: 10px;
        border-color: #EA6000;
        transform: rotate(-135deg);
    }
    a{
        text-decoration:none;
        color:#333;
    }
    button{
        cursor: pointer
    }
</style>
</html>
"""

    if export_path and host == '':
        if os.path.isdir(export_path):
            with open(export_path + "/report.html", "w", encoding="utf-8") as report:
                report.write(report_html)
            print(f"报告已导出在{export_path}/report.html")
        else:
            raise ValueError("指定的导出报告路径并非有效路径")
    elif host != '':
        if export_path:
            if os.path.isdir(export_path):
                with open(export_path + f"/{host}.html", "w", encoding="utf-8") as report:
                    report.write(report_html)
                print(f'\033[31m', end="")
                print(f"报告已导出在{export_path}/{host}.html")
                print("\033[0m", end="")
            else:
                raise ValueError("指定的导出报告路径并非有效路径")
        else:
            path = "web_reports"
            if not os.path.exists(path):
                os.makedirs(path)
            with open(f"web_reports/{host}.html", "w", encoding="utf-8") as report:
                report.write(report_html)
            print(f'\033[31m', end="")
            print(f"报告已导出在{os.getcwd()}/web_reports/{host}.html")
            print("\033[0m", end="")
    else:
        with open("report.html", "w", encoding="utf-8") as report:
            report.write(report_html)
        print(f"报告已导出在{os.getcwd()}/report.html")
