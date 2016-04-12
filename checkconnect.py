#coding:utf-8


import	wx
import  shelve


from pymodbus.client.sync import ModbusSerialClient as ModbusClient


CFG_FILE = 'cfg.data'
db = shelve.open(CFG_FILE)
dev = db['dev']
db.close()





def CheckConnect(self):


    try:
        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()
        rr = client.read_holding_registers(address=2064,count=4,unit=1)
        result = rr.registers
        client.close()

        dlg = wx.MessageDialog(self, u'Проверка связи прошла успешно!',u'Проверка %s' % dev,wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    except:

        dlg = wx.MessageDialog(self, u'Проверка связи завершилась неудачей!',u'Проверка %s' % dev,wx.OK | wx.ICON_ERROR)
        dlg.ShowModal()
        dlg.Destroy()
