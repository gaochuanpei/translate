# -*- coding: utf-8 -*-
import requests
import urllib.request
import urllib.parse
import json
import easygui as g
import execjs
import langid
from js文件.google import Py4Js
from js文件.baidu import Py4Js_baidu
def isConnected():
    try:
        html = requests.get("http://www.baidu.com",timeout=10)
    except:
        return False
    return True

def openUrl(url,data,head):
    data = urllib.parse.urlencode(data).encode('utf-8')    
    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    return target
def youdao():
    try:
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'
        data = {}
        data['i'] = content
        data['from'] = 'AUTO'
        data['to'] = 'AUTO'
        data['smartresult'] = 'dict'
        data['client'] = 'fanyideskweb'
        data['salt'] = '1522746794246'
        data['sign'] = '5550bebd1d567eb2fc2b43b5ae004814'
        data['doctype'] = 'json'
        data['version'] = '2.1'
        data['keyfrom'] = 'fanyi.web'
        data['action'] = 'FY_BY_REALTIME'
        data['typoResult'] = 'false'
        target=openUrl(url,data,head)
        return target['translateResult'][0][0]['tgt']
    except:
        return "有道翻译服务器有毛病"
def baidu():
    try:
        #with open("./js文件/baidu.js") as f:
        #    jsData = f.read()
        js_baidu = Py4Js_baidu()
        sign=js_baidu.getSign(content)
        #sign = execjs.compile(jsData).call("e",content)
        #print(sign)
        url = "https://fanyi.baidu.com/v2transapi"
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'
        head['Cookie']='REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BIDUPSID=D3E0482889EF29068BEB5860344981E7; PSTM=1551770564; BAIDUID=D3E0482889EF29068327ADAAB2D2D29E:FG=1; BDUSS=0Mzc1Y3NkVVZ0ZSSkVqYVF4NmRka0J0cldrMnNkUVRRSWhyT0N0NFFJVGJJckJjQVFBQUFBJCQAAAAAAAAAAAEAAAAd9olIu7Xs4c~Iyfrh6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANuViFzblYhcV; MCITY=-148%3A; DOUBLE_LANG_SWITCH=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1420_28939_21113_29064_28518_29099_28830_28584_26350_20718; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1558336394,1558943735,1559005656,1559007925; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1559007925; yjs_js_security_passport=9bf33a2f212962a224873c577603c10d63056ef6_1559007833_js; locale=zh; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22de%22%2C%22text%22%3A%22%u5FB7%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D'
        data = {}
        data['query'] = content
        data['from'] = DataFrom
        data['to'] = DataTo
        data['transtype'] = 'translang'
        data['simple_means_flag'] = '3'
        data['sign']=sign
        data['token']='edc2bdea555d5e8f10677f73ba80be23'
        target=openUrl(url,data,head)

        #target = json.loads(html)
        return target['trans_result']['data'][0]['dst']
    except:
        return "百度翻译服务器有毛病"
def google():
    try:
        js = Py4Js()
        tk = js.getTk(content)
        #print(tk)
        url = "http://translate.google.cn/translate_a/single?client=t&sl=auto&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s"%(DataTo_Google,tk,content)
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'	
        head['method'] = 'GET'
        r=requests.get(url,headers=head)
        result=json.loads(r.text)
        return result[0][0][0]
    except:
        return "谷歌翻译服务器有问题"

def jinshan():
    try:
        url = "http://fy.iciba.com/ajax.php?a=fy"
        head = {}
        head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 BIDUBrowser/8.7 Safari/537.36'
        head['method'] = 'POST'
        data = {}
        data['w'] = content
        data['f'] = 'auto'
        data['t'] = 'auto'
        target=openUrl(url,data,head)
        #print(target)
        if ('out' in target['content']):
            return target['content']['out']
        elif('word_mean' in target['content']):
            return target['content']['word_mean'][0]
        else:
            return ""
    except:
        return "金山翻译网站服务器有毛病"
ok = isConnected()
if(ok == False):
    g.msgbox("你没联网，查个弟弟翻译")
    exit()
while True:
    content = g.enterbox(msg = "请输入需要翻译的内容:",title = '小川翻译')
    if (content):
        result_youdao=""
        result_baidu=""
        result_google=""
        result_jinshan=""
        result_chuan="Sum up the above translation~3~"
        DataFrom=langid.classify(content)[0]
        DataTo = "en"
        DataTo_Google = "en"
        if (DataFrom != "zh"):
            DataFrom = "en"
            DataTo = "zh"
            DataTo_Google = "zh-CN"
            result_chuan="自己去总结上方翻译~3~"
        result_youdao=youdao()
        result_baidu=baidu()
        result_goole=google()
        result_jinshan=jinshan()
        msg = "翻译结果---来自小川"
        title = "翻译来喽~3~"
        fieldNames = ["有道翻译","百度翻译","谷歌翻译","金山翻译","川式翻译"]
        fieldValues = []
        fieldValues = g.multenterbox(msg,title,fieldNames,values=(result_youdao,result_baidu,result_goole,result_jinshan,result_chuan))
        #content2 = g.enterbox(msg = "翻译结果",title = '小川翻译',default=result_youdao)
        #print(fieldValues[0])
        if(not fieldValues):
            break
        #g.msgbox(msg = "翻译结果：%s"%(target['translateResult'][0][0]['tgt']))
    else:
        break


