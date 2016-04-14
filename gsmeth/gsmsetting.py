#coding:utf-8

import  wx, wx.aui
import  shelve

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from    tools import    Registr2ip,Ip2registr


CFG_FILE = 'cfg.data'
db = shelve.open(CFG_FILE)
dev = db['dev']
db.close()






class GSMSetting(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"GSM")


        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"Адрес сервера GSM1"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (u"Порт сервера GSM1"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (u"Адрес сервера GSM2"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, (u"Порт сервера GSM2"))
        self.label_5 = wx.StaticText(self, wx.ID_ANY, (u"Адрес сервера основной"))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, (u"Порт сервера основной"))


        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        p = wx.Panel(self)
        #wx.StaticText(p, -1,"двыдвыдвыдвлдвл")
        #p.SetBackgroundColour('light blue')


        grid_sizer_1 = wx.FlexGridSizer(7, 2, 1, 0)
        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.btn, 0, wx.TOP|wx.ALIGN_RIGHT, 20)
        grid_sizer_1.Add(self.btn1, 0, wx.TOP|wx.ALIGN_LEFT, 20)


        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(p, 1, wx.EXPAND)
        sizer.Add(grid_sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)
        self.SetSizer(sizer)

        wx.CallAfter(self.Layout)



        self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)





    def Write(self,event):


        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()


        ### IP адрес сервера GSM1
        add_string = self.text_ctrl_1.GetValue()
        rq=client.write_registers(6,Ip2registr(add_string),unit=1)


        ### Порт сервера GSM1
        port_string = self.text_ctrl_2.GetValue()
        port = int(port_string)
        rq=client.write_registers(13,[port],unit=1)


        ### IP адрес сервера GSM2
        add_string = self.text_ctrl_3.GetValue()
        rq=client.write_registers(8,Ip2registr(add_string),unit=1)


        ### Порт сервера GSM2
        port_string = self.text_ctrl_4.GetValue()
        port = int(port_string)
        rq=client.write_registers(14,[port],unit=1)


        ### IP адрес сервера основной
        add_string = self.text_ctrl_5.GetValue()
        rq=client.write_registers(4,Ip2registr(add_string),unit=1)

        ### Порт сервера основной
        port_string = self.text_ctrl_6.GetValue()
        port = int(port_string)
        rq=client.write_registers(12,[port],unit=1)


        client.close()








    def Read(self, event):


        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()


        ### IP адрес сервера GSM1
        rr = client.read_holding_registers(address=6,count=2,unit=1)
        result = rr.registers
        self.text_ctrl_1.SetValue(Registr2ip(result))

        ### Порт сервера GSM1
        rr = client.read_holding_registers(address=13,count=1,unit=1)
        result = rr.registers
        port = hex(result[0])
        port_string = "%s" % int(port,16)
        self.text_ctrl_2.SetValue(port_string)


        ### IP адрес сервера GSM2
        rr = client.read_holding_registers(address=8,count=2,unit=1)
        result = rr.registers
        self.text_ctrl_3.SetValue(Registr2ip(result))

        ### Порт сервера GSM2
        rr = client.read_holding_registers(address=14,count=1,unit=1)
        result = rr.registers
        port = hex(result[0])
        port_string = "%s" % int(port,16)
        self.text_ctrl_4.SetValue(port_string)


        ### IP адрес сервера основной
        rr = client.read_holding_registers(address=4,count=2,unit=1)
        result = rr.registers
        self.text_ctrl_5.SetValue(Registr2ip(result))

        ### Порт сервера основной
        rr = client.read_holding_registers(address=12,count=1,unit=1)
        result = rr.registers
        port = hex(result[0])
        port_string = "%s" % int(port,16)
        self.text_ctrl_6.SetValue(port_string)



        client.close()