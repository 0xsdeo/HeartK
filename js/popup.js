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

// show_info()