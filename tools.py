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

    adr1 = (hex(result[0])[2:]).rjust(4,"0")
    adr2 = (hex(result[1])[2:]).rjust(4,"0")
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



def Reg2Word(data):

    result = ""

    for item in data:
        if item == 0:
            return result
        a = (hex(item)[2:]).ljust(4,"0")
        b = a[0:2]
        c = a[2:4]
        result = result + chr(int(b,16)) + chr(int(c,16))

    return ""



def Word2Reg(data,RegCount):

    result = [0] * RegCount
    l = []
    word = list(data)


    for w in word:
        l.append(hex(ord(w)))



    if len(l)%2 == 0:
        l.append('0x0')
        l.append('0x0')
    else:
        l.append('0x0')


    wordlen = len(l)/2

    for i in range(0,wordlen):
        result[i] = int( ((l[0])[2:].rjust(2,"0") + (l[1])[2:].rjust(2,"0")),16)
        del l[0]
        del l[0]

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





### Сообщение записано
def Saved(self):

    dlg = wx.MessageDialog(self, u'Значения записаны в регистры',u'Сообщение',wx.OK | wx.ICON_INFORMATION)
    dlg.ShowModal()
    dlg.Destroy()




### Запись ключа шифрования
def Key2Reg(key):

    reg = [0,0,0,0]

    key = key.ljust(8," ")
    key = list(key[:8])



    reg[0] = int(hex(ord(key[0])) + hex(ord(key[1]))[2:],16)
    reg[1] = int(hex(ord(key[2])) + hex(ord(key[3]))[2:],16)
    reg[2] = int(hex(ord(key[4])) + hex(ord(key[5]))[2:],16)
    reg[3] = int(hex(ord(key[6])) + hex(ord(key[7]))[2:],16)

    return reg




def Reg2Key(reg):

    word = ""

    for item in reg:
        a = hex(item)[2:]
        if len(a) == 1:

            word = word + chr(int(hex(item)[2:].rjust(2,"0"),16))
            word = word + chr(int("00",16))

        elif len(a) == 2:

            word = word + chr(int(hex(item)[2:],16))
            word = word + chr(int("00",16))

        elif len(a) == 3:

            word = word + chr(int(hex(item)[2:4],16))
            word = word + chr(int(hex(item)[4:5].rjust(2,"0"),16))

        elif len(a) == 4:

            word = word + chr(int(hex(item)[2:4],16))
            word = word + chr(int(hex(item)[4:6],16))


    return word