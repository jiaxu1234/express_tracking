#coding=gbk
import requests as rs
import sys
import json
import sys #Ҫ��������sys����Ϊ Python ��ʼ�����ɾ�� sys.setdefaultencoding �������
# import easygui
reload(sys)
sys.setdefaultencoding('gbk')

def getexnum():
    if len(sys.argv) > 1:
        exnum = sys.argv[1]
    # exnum = easygui.enterbox(msg=u'��������Ҫ��ѯ�Ŀ�ݵ���:', title=u'��ݲ�ѯ ', default='', strip=True, image=None, root=None)
    exnum = raw_input("��������Ҫ��ѯ�Ŀ�ݵ���:")
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
    dict = {'ems': '�����ٵ�', 'yunda': '�ϴ���', 'shunfeng': '˳������','ups': 'UPS','rufengda': '����',
            'yuantong': 'Բͨ�ٵ�', 'baishiwuliu': '�������', 'jd': '����', 'ztky': '��������', 'xinfengwuliu': '�ŷ�����',
            'quanyikuaidi': 'ȫһ���', 'shentong': '��ͨ���', 'youzhengguonei': '��������С��', 'aae': 'AAEȫ��ר��',
            'dhl': 'DHL�й���', 'zhaijisong': 'լ����', 'lianbangkuaidi': '������', 'dhlen': 'dhlen', 'pjbest': 'Ʒ�����',
            'ueq': '����Ȥ(UEQ) ���','zhongtiewuliu': '��������', 'tnt': 'TNT', 'xinbangwuliu': '�°�����', 'zhongtong': '��ͨ���',
            'annengwuliu': '��������', 'tntuk': 'tntuk', 'debangwuliu': '�°�����', 'quanfengkuaidi': 'ȫ����', 'dpduk': 'dpduk',
            'kuayue': '��Խ�ٵ�', 'emsguoji': 'EMS���ʼ�', 'upsen': 'upsen', 'wanxiangwuliu': '��������', 'longbanwuliu': '��������',
            'jiajiwuliu': '�Ѽ�����', 'ocs': 'OCS', 'kuaijiesudi': '��ݿ��', 'guotongkuaidi': '��ͨ���', 'dpd': 'dpd',
            'tiandihuayu': '��ػ���', 'citylink': 'citylink���ʿ��', 'huitongkuaidi': '��ͨ���', 'youshuwuliu': '��������',
            'rufengda': '˳�ݷ��','cnpex': '���ʿ��', 'zengyisudi': '�����ٵ�', 'fedexus': 'FedEx������',
            'dpdgermany': 'DPD Germany', 'japanposten': '�ձ�����', 'zgyzt': '�й�����', 'speedpost': 'speedpost',
            'dhlde': 'dhl�¹����', 'suer': '�ٶ����', 'lasership': 'lasership', 'italysad': 'italysad',
            'fedex': 'FedEx������','aramex': 'Aramex', 'sfift': 'sfift', 'ibenben': 'ibenben',
            'lianhaowuliu': '���ͨ', 'chukou1': '������', 'tiantian': '������', 'nsf': 'nsf',
            'fedexcn': 'FedEx�й�', 'tnten': 'tnten', 'ucs': 'ucs', 'uluckex': '��������',
            'usps': 'USPS', 'jiayunmeiwuliu': '������', 'feikangda': '�ɿ�������','jiajikuaidi': '�Ѽ�����','shunjiefengda': '˳�ݷ��',
            }

    flag = True
    while flag:
        exnum = getexnum()
        if not exnum:
            print "��ݵ��Ų���Ϊ��"
            # easygui.msgbox(msg=u"��ݵ��Ų���Ϊ��", title=u'��ݲ�ѯ', ok_button='OK', image=None, root=None)
            continue
        else:
            for e in exnum:
                if ord(e) < 48 or ord(e) > 57:
                    print "��ݵ���Ӧ����������"
                    flag = False
                    break
        if flag:
            url = geturl(exnum)
            wuliu = getwuliu(url)
            try:
                kdata = getkd(exnum, wuliu)
            except:
                print '������˼û���ҵ���������˶�'
                continue
            for i in range(len(kdata)):
                wuliu[i] = dict[wuliu[i]]
                if kdata[i] == []:
                    print ("��ݹ�˾: ").encode('gbk') + wuliu[i] + ":  ������˼û���ҵ���������˶�"
                    # easygui.msgbox(msg=u'��ݹ�˾:'+ wuliu[i] + u':  ������˼û���ҵ���������˶�', title=u'��ݲ�ѯ', ok_button='OK', image=None, root=None)
                else:
                    print "��ݹ�˾: " + wuliu[i]
                    for r in kdata[i]:
                        print  r[0] + "  " + r[1]
        else:
            flag = True