#coding:utf-8

import wx
import dbhash


from pymodbus.client.sync import ModbusSerialClient as ModbusClient



CFG_FILE = 'cfg.data'




def GetDev():
    db = dbhash.open(CFG_FILE,'c')
    if db.has_key('dev') == False:
        db['dev'] = u''

    dev = db['dev']
    db.close()

    return dev


def SetDev(dev):

    db = dbhash.open(CFG_FILE,'c')
    db['dev'] = dev
    db.close()

    return True




def ConnectDev():

    client = ModbusClient(method='rtu', port='%s' % GetDev(), baudrate='115200', timeout=1)

    return client




def Registr2ip(result):

    adr1 = (hex(result[0])+"0000")[2:6]
    adr2 = (hex(result[1])+"0000")[2:6]
    a = int(adr1[0:2],16)
    b = int(adr1[2:4],16)
    c = int(adr2[0:2],16)
    d = int(adr2[2:4],16)
    addr_string = "%s.%s.%s.%s" % (a,b,c,d)

    return addr_string



def Ip2registr(ip_string):

    adr = ip_string.split('.')
    a = ("00"+(hex(int(adr[0]))[2:]))[-2:]
    b = ("00"+(hex(int(adr[1]))[2:]))[-2:]
    c = ("00"+(hex(int(adr[2]))[2:]))[-2:]
    d = ("00"+(hex(int(adr[3]))[2:]))[-2:]

    result = [int(a+b,16),int(c+d,16)]

    return result





def SaveConfig(self):


    try:
        client = ModbusClient(method='rtu', port='%s' % GetDev(), baudrate='115200', timeout=1)
        client.connect()
        rq=client.write_registers(2048,[1],unit=1)
        client.close()

        dlg = wx.MessageDialog(self, u'Запись прошла успешно!',u'Запись',wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    except:

        dlg = wx.MessageDialog(self, u'Запись завершилась неудачей!',u'Запись',wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()




def Read2bytes(result):
        data = ("0000"+(hex(result))[2:])[-4:]
        a = data[0:2]
        b = data[2:4]
        a = list(data[0:2])
        b = list(data[2:4])
        a.reverse()
        b.reverse()
        result = "".join(a)+"".join(b)
        return result



def Write16key(result):
        r = StrRevers(result)

        a = list(r[0:2])
        b = list(r[2:4])
        c = list(r[4:6])
        d = list(r[6:8])
        e = list(r[8:10])
        f = list(r[10:12])
        g = list(r[12:14])
        h = list(r[14:16])

        a.reverse()
        b.reverse()
        c.reverse()
        d.reverse()
        e.reverse()
        f.reverse()
        g.reverse()
        h.reverse()

        first = int("".join(a)+"".join(b),16)
        second = int("".join(c)+"".join(d),16)
        third = int("".join(e)+"".join(f),16)
        fourth = int("".join(g)+"".join(h),16)

        result = [first,second,third,fourth]

        return result





def StrRevers(result):
        a = list(result)
        a.reverse()
        b = "".join(a)
        return b



### Определение адреса бита
def GetAddressBit(bits):

    a = "0"*8 + bits
    b = 8
    for item in list(a[-8:]):
        if item == "1":
            return b
        b = b - 1

    return 0


### Установка по адресу бита
def SetAddressBit(bits):

    a = ["0","0","0","0","0","0","0","0"]
    if bits != 0:
        a[-(bits)] = "1"

    return "".join(a)

