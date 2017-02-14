#!/usr/bin/env python
# coding=utf-8
#proxy={'http':'0.0.0.0:8087',}
import requests
from requests import Session
from bs4 import BeautifulSoup
cookie={'RK':"dUHKqSj/cg",
        'pgv_info':"ssid=s9907881740",
        'pgv_pvid':"8997132090",
        'pt2gguin':"o0850747813",
        'ptcz':"f4f46c6ba189372ebdee3fc2a06db7f4b6711ac8bca2bbf6c2b7de22142015c2",
        'ptisp':"cm",
        'qqmusic_fromtag':"6",
        'qqmusic_key':"@2TS1VQHo2",
        'qqmusic_uin':"0850747813",
        'skey':"@2TS1VQHo2",
        'uin':"o0850747813",
        'Loading':"Yes",
        'QZ_FE_WEBP_SUPPORT':"0",
        'qz_screen':"1366x768",
        'pt4_token':"08eRm6AniykWLso66a8fnuMK3FrfKPvmNSyq5ORTohE_",
        '__Q_w_s__QZN_TodoMsgCnt':"1",
        'cpu_performance_v8':"27",


}
head={
    'Host':"qzonestyle.gtimg.cn",
    'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0",
    'Accept':"*/*",
    'Accept-Language':"en-US,en;q=0.5",
    'Referer':"http://user.qzone.qq.com/850747813",
    'DNT':"1",
    'Connection':"keep-alive",
}
response = requests.get("http://user.qzone.qq.com/850747813",cookies=cookie,timeout=5,headers=head)
soup=BeautifulSoup(response.text,"lxml")
print(soup)
#help(BeautifulSoup)
