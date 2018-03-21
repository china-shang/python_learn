#!/usr/bin/env python
# coding=utf-8


import sys
import requests
import json
import pymysql
from requests import Session
import threading


with open("test.t","r") as f:
    data=json.loads(f.read())

list1=data["items_list"]
uin_list=[]
uin_dict=dict()

for i in list1:
    uin_list.append(i["uin"])


lock=threading.Lock()
thread_list=[]


class Qzone:
    header={
    'Host':'user.qzone.qq.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept':'*/*',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Referer': 'https://user.qzone.qq.com/850747813/main',
    'Cookie':'pgv_pvid=8475491000; pgv_info=ssid=s294161228; ptisp=cm; pgv_pvi=4031504384; pgv_si=s9458216960; ptui_loginuin=850747813; pt2gguin=o0850747813; uin=o0850747813; skey=@mrlBiDMUe; RK=idDAvSjleg; ptcz=0f122b0921183cb19474e9c9182807656c6ddb67caa7b47a4dc632af88eb08ce; p_uin=o0850747813; pt4_token=CHq-wL0EURezLa601H5NzHAul*s0z10CQC3351rjpqU_; p_skey=5q3tqaYjlpx8PXSM0PeRu2wmkyHrrzUzT0ItEsHMxsg_; Loading=Yes; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=0; cpu_performance_v8=2; __Q_w_s_hat_seed=1; __Q_w_s__QZN_TodoMsgCnt=1',
    'DNT':'1',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',

    }
    header_like={
    'Host':'user.qzone.qq.com',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding':'gzip, deflate, br',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie':'pgv_pvid=8475491000; pgv_info=ssid=s294161228; ptisp=cm; pgv_pvi=4031504384; pgv_si=s9458216960; ptui_loginuin=850747813; pt2gguin=o0850747813; uin=o0850747813; skey=@mrlBiDMUe; RK=idDAvSjleg; ptcz=0f122b0921183cb19474e9c9182807656c6ddb67caa7b47a4dc632af88eb08ce; p_uin=o0850747813; pt4_token=CHq-wL0EURezLa601H5NzHAul*s0z10CQC3351rjpqU_; p_skey=5q3tqaYjlpx8PXSM0PeRu2wmkyHrrzUzT0ItEsHMxsg_; Loading=Yes; qz_screen=1366x768; QZ_FE_WEBP_SUPPORT=0; cpu_performance_v8=2; __Q_w_s_hat_seed=1; __Q_w_s__QZN_TodoMsgCnt=1',
    'DNT':'1',
    'Connection':'keep-alive',
    'Upgrade-Insecure-Requests':'1',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',


    }
    like_url='https://user.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/likes/internal_dolike_app?g_tk=1503882933&qzonetoken=9ba33be70993216df3e57475ff841b9322819e9fc2bce769369366d743698d3076e9cb2263071d84bacb'
    like_url='https://user.qzone.qq.com/proxy/domain/w.qzone.qq.com/cgi-bin/likes/internal_dolike_app?g_tk=1503882933&qzonetoken=2828596f2319f101b62d37357f250feef2e37252d7df861a5ed6664e50006369832e30a1ca71880ddfde'
    like_data='qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F850747813%2Finfocenter%3Fvia%3Dtoolbar&opuin=850747813&unikey=http%3A%2F%2Fuser.qzone.qq.com%2F850747813%2Fmood'+ '%2Fa561b5320dd795586a3b0300'+'.1%5E%7C%7C%5Ehttp%3A%2F%2Fb267.photo.store.qq.com%2Fpsb%3F%2FV12iWiLH2Ood42%2F2SJs.cNgoG5hlu5*twrUWDGe9XlFQj.sW3mIq9HFARE%21%2Fb%2FdAsBAAAAAAAA%26bo%3D6gOXBQAAAAAFEEg%21%5E%7C%7C%5E0&curkey=http%3A%2F%2Fuser.qzone.qq.com%2F850747813%2Fmood'+ '%2Fa561b5320dd795586a3b0300'+'.1%5E%7C%7C%5Ehttp%3A%2F%2Fb267.photo.store.qq.com%2Fpsb%3F%2FV12iWiLH2Ood42%2F2SJs.cNgoG5hlu5*twrUWDGe9XlFQj.sW3mIq9HFARE%21%2Fb%2FdAsBAAAAAAAA%26bo%3D6gOXBQAAAAAFEEg%21%5E%7C%7C%5E0&from=-100&fupdate=1&face=0'

    def generateLikeUrl(self,tid,who=577304866):
        #like_data='qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2Fproxy%2Fdomain%2Fic2.qzone.qq.com%2Fcgi-bin%2Ffeeds%2Ffeeds_html_module%3Fi_uin%3D'+str(who)+'%26i_login_uin%3D850747813%26style%3D19%26version%3D8%26needDelOpr%3Dtrue%26hideExtend%3Dfalse%26showcount%3D15%26MORE_FEEDS_CGI%3Dhttp%253A%252F%252Fic2.qzone.qq.com%252Fcgi-bin%252Ffeeds%252Ffeeds_html_act_all%26refer%3D2&opuin=850747813&unikey=http%3A%2F%2Fuser.qzone.qq.com%2F'+str(who)+'%2Fmood%2F'+tid+'&curkey=http%3A%2F%2Fuser.qzone.qq.com%2F'+str(who)+'%2Fmood%2F'+tid+'&from=1&appid=311&typeid=0&abstime=1515397027&fid='+tid+'&active=0&fupdate=1'
        like_data='qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F'+tid+'&opuin=850747813&unikey=http%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F'+tid+'.1&curkey=http%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F'+tid+'.1&from=-100&fupdate=1&face=0'
        like_data1='qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F22f968227806d25985740b00&opuin=850747813&unikey=http%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F22f968227806d25985740b00.1&curkey=http%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F22f968227806d25985740b00.1&from=-100&fupdate=1&face=0'
        like_data='qzreferrer=https%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F'+tid+'&opuin=850747813&unikey=http%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F'+tid+'.1&curkey=http%3A%2F%2Fuser.qzone.qq.com%2F577304866%2Fmood%2F'+tid+'.1&from=-100&fupdate=1&face=0'
        print(len(tid))
        test='2F22f968227806d25985740b00'
        if('2F22f968227806d25985740b00'.startswith(tid) or '2F22f968227806d25985740b00'.endswith(tid)):
            print(like_data)
            print(like_data1)
            if(like_data!=like_data1):
                print("bug bug ")
                print(like_data,like_data1)
                
            #sys.exit()


        return like_data

    def __init__(self):
        self.con=None
        self.url='https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?ftype=0&sort=0&g_tk=1503882933&callback=_preloadCallback&code_version=1&format=json&need_private_comment=1&qzonetoken=80110bfd3cb85ff54db6f7194f8501c665e6ff8d08762b59975f6e2dcafe816eb35cb14b65ce4f2edb5c'

        self.params={
            "pos":260,
            "num":20,
            "replynum":100,
            #"uin":"577304866",
            "uin":"1334640144",
            "sort":0,
            "ftype":0,
        }

        self.connectMysql()
    def like(self,tid):
        print(tid)
        r=requests.post(url=self.like_url,data=self.generateLikeUrl(tid),headers=self.header_like)
        print(r.text)




    def connectMysql(self):
        self.con=pymysql.Connect(user="root",
                       password="123456",
                       database="qqzone",
                       charset="utf8",
                       host="localhost")
        self.con.autocommit(True)
        self.cur=self.con.cursor()

    def insertUser(self,user):
        #if len(user["id"])>14:
            #return 
        #print(user["id"])
        self.cur.execute("SELECT * from `user` where `id`=%s",user["id"])
        result=self.cur.fetchone()
        if(result):
            #print("has user: "+user["name"])
            return 
        else:
            self.cur.execute('INSERT INTO `user` (`id`,`name`) VALUES(%s,%s)',(user["id"],user["name"][:15]))
            print("has insert user: "+user["name"])
    
    def insertComment(self,cmt):
        self.cur.execute("SELECT * from `comment` where `id`=%s",cmt["id"])
        result=self.cur.fetchone()
        if(result):
            #print("has user: "+user["name"])
            return 

        self.cur.execute("INSERT INTO `comment` (`id`,`uin`, `content`, `createTime`, `createTime2`, `create_time`, `messageid`, `replynum`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)",
                         (cmt.get("id",None),cmt.get("uin",None),cmt.get("content",None)[:300], cmt.get("createTime",None),cmt.get("createTime2",None), cmt.get("created_time",None),cmt.get("messageid",None),cmt.get("reply_num",None),))


    def insertMessage(self,msg):
        self.count+=1
        self.cur.execute("SELECT * from `message` where `id`=%s",msg["tid"])
        result=self.cur.fetchone()
        if(result):
            #print("has meg: "+msg["tid"])
            return False
        else:
            self.cur.execute('INSERT INTO `message` (`id`, `cmtnum`, `pictotal`, `content`, `uin`, `createTime`, `create_time`) VALUES(%s,%s,%s,%s,%s,%s,%s)',(msg["tid"], msg["cmtnum"], msg.get("pictotal",None), msg["content"][:300], msg["uin"], msg["createTime"], msg["created_time"],))
            print("insert message Success")
            return True
    def insertReply(self,reply):

        try:
            self.cur.execute("INSERT INTO `reply` (`id`,`uin`, `content`, `createTime`, `createTime2`, `create_time`, `commentid`, `who`,`auto`) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (reply.get("id",None),reply.get("uin",None),reply.get("content",None), reply.get("createTime",None),reply.get("createTime2",None), reply.get("created_time",None),reply.get("commentid",None),reply.get("who",None),reply.get("auto",None),))
        except Exception as e:
            print(e)
            return False
    def insertPic(self,pic):
        pass
    
    def fetchAll(self,uin):

        global uin_dict
        global lock
        self.params["uin"]=uin
        self.params["pos"]=0
        self.count=0

        print("start"+str(uin))
        response = requests.get(
            self.url,
            params=self.params,
            headers=self.header)
        s=response.text
        print(s)

        data=json.loads(s)
        #self.total=data["total"]

        #while self.params.get("pos")+self.params.get("num")<self.total:
            #print("pos",self.params["pos"])
        #try:
        while self.run():
            #try:
            #except Exception as e:
                #print("---------------------------------EXCEPTION----------------------------")
            #print(e)
            self.params["pos"]+=20
        #except Exception as e:
            #print(e)
        #finally:
            #with lock:
                #uin_dict[uin]=self.count


    def run(self):

        response = requests.get(
            self.url,
            params=self.params,
            headers=self.header)

        s=response.text
        print(response.json())
        #print(s)

        data=json.loads(s)

        user={}
        datalist=data.get("msglist",None)
        print(datalist)
        if(datalist is None):
            print(data)
            return False
        for msg_t in datalist:
            user["id"]=msg_t["uin"]
            self.like(msg_t["tid"])
            user["name"]=msg_t["name"]
            self.insertUser(user)
            if not self.insertMessage(msg_t):
                continue
            #print(msg_t["content"])
            if(msg_t["cmtnum"]>0):
                for cmt_t in msg_t["commentlist"]:
                    #print(cmt_t["content"])
                    #print(cmt_t["createTime2"])
                    cmt_t["messageid"]=msg_t["tid"]
                    cmt_t["id"]=msg_t["tid"]+str(cmt_t["tid"])
                    user["name"]=cmt_t["name"]
                    user["id"]=cmt_t["uin"]
                    self.insertUser(user)
                    self.insertComment(cmt_t)
                    if(cmt_t["reply_num"]>0):
                        for reply_t in cmt_t["list_3"]:
                            #print(k["content"].split("}")[1])
                            #print(reply["content"])
                            if(reply_t["content"]):
                                handle=self.handle_reply(reply_t)
                                reply_t["auto"]=handle[2]
                                reply_t["who"]=handle[0]
                                reply_t["content"]=handle[-1]
                                reply_t["commentid"]=cmt_t["id"]
                                self.insertReply(reply_t)
                                print(handle)
                                #print(reply_t["createTime2"])
        return True


    def handle_reply(self,reply):
        try:
            s=reply["content"]
            if(s.find("uin:")!=-1):
                uin=s.split("uin:")[1].split(",",1)[0]
                nick=s.split("nick:")[1].split(",")[0]
                user={"id":uin,
                     "name":nick}
                self.insertUser(user)
                if(s.find("auto")!=-1):
                    auto=s.split("auto:")[1].split("}")[0]
                else:
                    auto=0
                text=s.rsplit("}",1)[1].split(",")[0]
                return [uin,nick,auto,text]
            else:
                return [None,None,None,s]

        except Exception as e:
            print(s)
            print(e)
            return [None,None,None,s]
qzon=Qzone()
qzon.fetchAll(577304866)
#qzon.like('a561b53254660650eed40900')

#def mutiThreadRun():

    #global lock
    #global uin_list
    #qzon=Qzone()

    #while len(uin_list)>0:
        #with lock:
            #if(len(uin_list)>0):
                #uin=uin_list.pop(0)
                #print("uin=",uin)
            #else:
                #qzon.con.close()
                #qzon.cur.close()
                #return 
        #qzon.fetchAll(uin)
    #return 

#for i in range(2):
    #t=threading.Thread(target=mutiThreadRun)
    #thread_list.append(t)
    #t.start()

#try:
    #for i in thread_list:
        #i.join()
#except Exception as e:
    #print(e)
#finally:
    #for i in uin_dict:
        #print(i,":",uin_dict[i])

