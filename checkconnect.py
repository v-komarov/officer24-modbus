#coding:utf-8


import	wx
from tools import ConnectDev,GetDev






def CheckConnect(self):


    try:
        client = ConnectDev()
        client.connect()
        rr = client.read_holding_registers(address=2064,count=4,unit=1)
        result = rr.registers
        client.close()

        dlg = wx.MessageDialog(self, u'Проверка связи прошла успешно!',u'Проверка %s' % GetDev(),wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    except:

        dlg = wx.MessageDialog(self, u'Проверка связи завершилась неудачей!',u'Проверка %s' % GetDev(),wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()
