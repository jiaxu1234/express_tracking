#coding=gbk
import requests as rs
import sys
import json
import sys #要重新载入sys。因为 Python 初始化后会删除 sys.setdefaultencoding 这个方法
# import easygui
reload(sys)
sys.setdefaultencoding('gbk')

def getexnum():
    if len(sys.argv) > 1:
        exnum = sys.argv[1]
    # exnum = easygui.enterbox(msg=u'请输入您要查询的快递单号:', title=u'快递查询 ', default='', strip=True, image=None, root=None)
    exnum = raw_input("请输入您要查询的快递单号:")
    return exnum

def geturl(exnum):
    url = "http://www.kuaidi100.com/autonumber/auto?num=" + exnum
    return url

def getwuliu(url):
    res = rs.get(url)
    js = json.loads(res.text)
    if js:
        length = len(js)
        wl = []
        for i in range(length):
            wl.append(js[i]['comCode'])
        return wl

def getkd(exnum, wl):
    wlength = len(wl)
    kdata = [[] for i in range(wlength)]
    for i in range(wlength):
        kdurl = "http://www.kuaidi100.com/query?type=" + wl[i] + "&postid=" + exnum
        kres = rs.get(kdurl)
        kjs = json.loads(kres.text)
        if kjs['status'] != '200':
            pass
        else:
            kqty = len(kjs['data'])
            for j in range(kqty):
                kdata[i].append([kjs['data'][j]['time'], kjs['data'][j]['context']])
    return kdata

if __name__ == '__main__':
    print '''
    **************************************************************
                Welcome to Express Checking System!
    **************************************************************
    '''
    dict = {'ems': '邮政速递', 'yunda': '韵达快递', 'shunfeng': '顺丰速运','ups': 'UPS','rufengda': '如风达',
            'yuantong': '圆通速递', 'baishiwuliu': '百世快递', 'jd': '京东', 'ztky': '中铁快运', 'xinfengwuliu': '信丰物流',
            'quanyikuaidi': '全一快递', 'shentong': '申通快递', 'youzhengguonei': '邮政国内小包', 'aae': 'AAE全球专递',
            'dhl': 'DHL中国件', 'zhaijisong': '宅急送', 'lianbangkuaidi': '联邦快递', 'dhlen': 'dhlen', 'pjbest': '品骏快递',
            'ueq': '优宜趣(UEQ) 快递','zhongtiewuliu': '中铁物流', 'tnt': 'TNT', 'xinbangwuliu': '新邦物流', 'zhongtong': '中通快递',
            'annengwuliu': '安能物流', 'tntuk': 'tntuk', 'debangwuliu': '德邦物流', 'quanfengkuaidi': '全峰快递', 'dpduk': 'dpduk',
            'kuayue': '跨越速递', 'emsguoji': 'EMS国际件', 'upsen': 'upsen', 'wanxiangwuliu': '万象物流', 'longbanwuliu': '龙邦物流',
            'jiajiwuliu': '佳吉快运', 'ocs': 'OCS', 'kuaijiesudi': '快捷快递', 'guotongkuaidi': '国通快递', 'dpd': 'dpd',
            'tiandihuayu': '天地华宇', 'citylink': 'citylink国际快递', 'huitongkuaidi': '汇通快递', 'youshuwuliu': '优速物流',
            'rufengda': '顺捷丰达','cnpex': '中邮快递', 'zengyisudi': '增益速递', 'fedexus': 'FedEx美国件',
            'dpdgermany': 'DPD Germany', 'japanposten': '日本邮政', 'zgyzt': '中国邮政', 'speedpost': 'speedpost',
            'dhlde': 'dhl德国快递', 'suer': '速尔快递', 'lasership': 'lasership', 'italysad': 'italysad',
            'fedex': 'FedEx美国件','aramex': 'Aramex', 'sfift': 'sfift', 'ibenben': 'ibenben',
            'lianhaowuliu': '联昊通', 'chukou1': '出口易', 'tiantian': '天天快递', 'nsf': 'nsf',
            'fedexcn': 'FedEx中国', 'tnten': 'tnten', 'ucs': 'ucs', 'uluckex': '优联吉运',
            'usps': 'USPS', 'jiayunmeiwuliu': '加运美', 'feikangda': '飞康达物流','jiajikuaidi': '佳吉快运','shunjiefengda': '顺捷丰达',
            }

    flag = True
    while flag:
        exnum = getexnum()
        if not exnum:
            print "快递单号不可为空"
            # easygui.msgbox(msg=u"快递单号不可为空", title=u'快递查询', ok_button='OK', image=None, root=None)
            continue
        else:
            for e in exnum:
                if ord(e) < 48 or ord(e) > 57:
                    print "快递单号应该是数字呦"
                    flag = False
                    break
        if flag:
            url = geturl(exnum)
            wuliu = getwuliu(url)
            try:
                kdata = getkd(exnum, wuliu)
            except:
                print '不好意思没有找到，请认真核对'
                continue
            for i in range(len(kdata)):
                wuliu[i] = dict[wuliu[i]]
                if kdata[i] == []:
                    print ("快递公司: ").encode('gbk') + wuliu[i] + ":  不好意思没有找到，请认真核对"
                    # easygui.msgbox(msg=u'快递公司:'+ wuliu[i] + u':  不好意思没有找到，请认真核对', title=u'快递查询', ok_button='OK', image=None, root=None)
                else:
                    print "快递公司: " + wuliu[i]
                    for r in kdata[i]:
                        print  r[0] + "  " + r[1]
        else:
            flag = True