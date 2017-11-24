#!/usr/bin/env python
# coding=utf-8
# proxy={'http':'0.0.0.0:8087',}
import requests
from requests import Session
from bs4 import BeautifulSoup
# cookie={
#'pgv_pvi':'1257658368',
#'pgv_si':'s7049339904',
#'pgv_pvid':'2829898740',
#'pgv_info':'ssid=s5389852900',
#'ptisp':'ssid=s5389852900',
#'ptui_loginuin':'1229273502',
#'pt2gguin':'o1229273502',
#'uin':'o1229273502',
#'skey':'o1229273502',
#'RK':'o1229273502',
#'ptcz':'62d41e7b3799865bcdb6e8dec213674eea807abdfbe7cef84187840fbb4e2c12',
#'p_uin':'o1229273502',
#'p_skey':'AgSweQO0K3zDqJB17YF9C-McmrxQqxxypYMuFHlQJ*Q_',
#'pt4_token':'0Cb8OkPwzCNo8U2teMrjlEDV6xbpdwXRz9F*yQgh9ls_',
#'Loading':'Yes',
#'1229273502_todaycount':'0',
#'1229273502_totalcount':'33',
#'qz_screen':'1366x768',
#'QZ_FE_WEBP_SUPPORT':'0',
#'cpu_performance_v8':'34',
#'__Q_w_s__QZN_TodoMsgCnt':'1',
#'__Q_w_s_hat_seed':'1',

#}
# head={
#'Host':"qzonestyle.gtimg.cn",
#'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0",
#'Accept':"*/*",
#'Accept-Language':"en-US,en;q=0.5",
#'DNT':"1",
#'Connection':"keep-alive",
#}
cookie = {
    'pgv_pvi': '1257658368',
    'pgv_si': 's7049339904',
    'pgv_pvid': '2829898740',
    'pgv_info': 'ssid=s5389852900',
    'ptisp': 'ssid=s5389852900',
    'ptui_loginuin': '1229273502',
    'pt2gguin': 'o1229273502',
    'uin': 'o1229273502',
    'skey': 'o1229273502',
    'RK': 'o1229273502',
    'ptcz': '62d41e7b3799865bcdb6e8dec213674eea807abdfbe7cef84187840fbb4e2c12',
    'p_uin': 'o1229273502',
    'p_skey': 'AgSweQO0K3zDqJB17YF9C-McmrxQqxxypYMuFHlQJ*Q_',
    'pt4_token': '0Cb8OkPwzCNo8U2teMrjlEDV6xbpdwXRz9F*yQgh9ls_',
    'Loading': 'Yes',
    '1229273502_todaycount': '0',
    '1229273502_totalcount': '33',
    'qz_screen': '1366x768',
    'QZ_FE_WEBP_SUPPORT': '0',
    'cpu_performance_v8': '34',
    '__Q_w_s__QZN_TodoMsgCnt': '1',
    '__Q_w_s_hat_seed': '1',
}
header = {
    'Host': "user.qzone.qq.com",
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "en-US,en;q=0.5",
    'Accept-Encoding': "gzip, deflate, br",
    'Referer': "https://user.qzone.qq.com/1229273502",
    'DNT': "1",
    'Connection': "keep-alive",
}

header = {
    'Host': "user.qzone.qq.com",
    'User-Agent': "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "en-US,en;q=0.5",
    'Accept-Encoding': "gzip, deflate, br",
    'DNT': "1",
    'Cookie': "pgv_pvi=1257658368; pgv_si=s7049339904; pgv_pvid=2829898740; pgv_info=ssid=s5389852900; ptisp=ctc; ptui_loginuin=1229273502; pt2gguin=o1229273502; uin=o1229273502; skey=@OlN43LNIM; RK=T01uSeA7RN; ptcz=62d41e7b3799865bcdb6e8dec213674eea807abdfbe7cef84187840fbb4e2c12; p_uin=o1229273502; p_skey=7ESD-MdUcaUY4GjpeeB9KLTFmzEinNczp5xiucb9Ssc_; pt4_token=9h-Yz9wp7JH5oXxXNR7GcITxG6eMGR4s*nmPs*gTjJs_; Loading=Yes; 1229273502_todaycount=0; 1229273502_totalcount=33; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=0; cpu_performance_v8=42; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; g_ut=1",
    'Connection': "keep-alive",
    'Referer': " https://qzs.qzone.qq.com",
    'Upgrade-Insecure-Requests': " 1",
    'Cache-Control': " max-age=0",
    'If-Modified-Since': " Thu, 15 Jun 2017 07:33:12 GMT",
}
cookie = {
    'pgv_si': 's7049339904',
    'pgv_pvid': '2829898740',
    'pgv_info': 'ssid=s5389852900',
    'ptisp': 'ssid=s5389852900',
    'ptui_loginuin': '1229273502',
    'pt2gguin': 'o1229273502',
    'uin': 'o1229273502',
    'skey': 'o1229273502',
    'RK': 'o1229273502',
    'ptcz': '62d41e7b3799865bcdb6e8dec213674eea807abdfbe7cef84187840fbb4e2c12',
    'p_uin': 'o1229273502',
    'p_skey': 'AgSweQO0K3zDqJB17YF9C-McmrxQqxxypYMuFHlQJ*Q_',
    'pt4_token': '0Cb8OkPwzCNo8U2teMrjlEDV6xbpdwXRz9F*yQgh9ls_',
    'Loading': 'Yes',
    '1229273502_todaycount': '0',
    '1229273502_totalcount': '33',
    'qz_screen': '1366x768',
    'QZ_FE_WEBP_SUPPORT': '0',
    'cpu_performance_v8': '34',
    '__Q_w_s__QZN_TodoMsgCnt': '1',
    '__Q_w_s_hat_seed': '1',
}
help(requests)
header = {
    'Host': 'user.qzone.qq.com',
    #'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
    #'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/52.0.2743.116 Safari/537.36',

    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Cookie': 'pgv_pvi=1257658368; pgv_si=s7049339904; pgv_pvid=2829898740; pgv_info=ssid=s5389852900; ptisp=ctc; ptui_loginuin=1229273502; pt2gguin=o1229273502; uin=o1229273502; skey=@OlN43LNIM; RK=T01uSeA7RN; ptcz=62d41e7b3799865bcdb6e8dec213674eea807abdfbe7cef84187840fbb4e2c12; p_uin=o1229273502; p_skey=7ESD-MdUcaUY4GjpeeB9KLTFmzEinNczp5xiucb9Ssc_; pt4_token=9h-Yz9wp7JH5oXxXNR7GcITxG6eMGR4s*nmPs*gTjJs_; Loading=Yes; 1229273502_todaycount=0; 1229273502_totalcount=33; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=0; cpu_performance_v8=42; __Q_w_s__QZN_TodoMsgCnt=1; __Q_w_s_hat_seed=1; g_ut=1',
    'Connection': 'keep-alive',
    'Referer': 'https://qzs.qzone.qq.com/qzone/v5/loginsucc.html?para=izone&from=iqq&specifyurl=http%3A%2F%2Fuser.qzone.qq.com%2F1229273502',
    'Upgrade-Insecure-Requests': '1',
    'Cache-Control': 'max-age=0',
    'If-Modified-Since': 'Thu, 15 Jun 2017 07:33:12 GMT',
}
response = requests.get(
    "http://user.qzone.qq.com/1229273502",
    cookies=cookie,
    headers=header)
soup = BeautifulSoup(response.text, "lxml")
print(soup.text)
