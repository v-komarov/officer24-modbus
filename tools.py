#coding:utf-8

import wx
import  shelve


from pymodbus.client.sync import ModbusSerialClient as ModbusClient



CFG_FILE = 'cfg.data'
db = shelve.open(CFG_FILE)
dev = db['dev']
db.close()



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
        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
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
        data = (hex(result)+"0000")[2:6]
        return data

