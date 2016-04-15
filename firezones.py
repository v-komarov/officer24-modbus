#coding:utf-8


import	wx
import  shelve
import sys
import  wx.lib.mixins.listctrl  as  listmix

from    tools import Read2bytes,StrRevers,Write16key


from pymodbus.client.sync import ModbusSerialClient as ModbusClient


CFG_FILE = 'cfg.data'
db = shelve.open(CFG_FILE)
dev = db['dev']
db.close()






class FireZone1(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Пожарная зона 1")



        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"Пожарная зона 1 в разделе"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (u"Автоматический сброс 1 пож. зоны"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (u"Пожарная зона 1 вкл."))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, (u"Двойная сработка пож. 1"))


        self.sc = wx.SpinCtrl(self, -1, "", (30, 50))
        self.sc.SetRange(1,8)
        #sc.SetValue(5)


        self.cb1 = wx.CheckBox(self, -1, "")
        self.cb2 = wx.CheckBox(self, -1, "")
        self.cb3 = wx.CheckBox(self, -1, "")


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        p = wx.Panel(self)


        grid_sizer_1 = wx.FlexGridSizer(5, 2, 1, 0)

        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3, 0, wx.ALL, 10)


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


        ### IP адрес сервера
        add_string = self.text_ctrl_3.GetValue()
        rq=client.write_registers(10,Ip2registr(add_string),unit=1)


        ### Порт сервера
        port_string = self.text_ctrl_4.GetValue()
        port = int(port_string)
        rq=client.write_registers(15,[port],unit=1)


        ### Шлюз
        add_string = self.text_ctrl_5.GetValue()
        rq=client.write_registers(148,Ip2registr(add_string),unit=1)

        ### Использовать Etherner
        if self.cb1.GetValue():
            rq=client.write_registers(146,[1],unit=1)
        else:
            rq=client.write_registers(146,[0],unit=1)

        ### Использовать DHCP
        if self.cb2.GetValue():
            rq=client.write_registers(147,[1],unit=1)
        else:
            rq=client.write_registers(147,[0],unit=1)


        ### IP адрес устройства
        add_string = self.text_ctrl_1.GetValue()
        rq=client.write_registers(152,Ip2registr(add_string),unit=1)

        ### Маска устройства
        add_string = self.text_ctrl_2.GetValue()
        rq=client.write_registers(150,Ip2registr(add_string),unit=1)

        client.close()







    def Read(self, event):


        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()


        rr = client.read_holding_registers(address=1115,count=1,unit=1)
        result = rr.registers
        print result


        client.close()






class FireZone2(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Пожарная зона 2")



        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"Пожарная зона 2 в разделе"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (u"Автоматический сброс 2 пож. зоны"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (u"Пожарная зона 2 вкл."))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, (u"Двойная сработка пож. 2"))


        self.sc = wx.SpinCtrl(self, -1, "", (30, 50))
        self.sc.SetRange(1,8)
        #sc.SetValue(5)


        self.cb1 = wx.CheckBox(self, -1, "")
        self.cb2 = wx.CheckBox(self, -1, "")
        self.cb3 = wx.CheckBox(self, -1, "")


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        p = wx.Panel(self)


        grid_sizer_1 = wx.FlexGridSizer(5, 2, 1, 0)

        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3, 0, wx.ALL, 10)


        grid_sizer_1.Add(self.btn, 0, wx.TOP|wx.ALIGN_RIGHT, 20)
        grid_sizer_1.Add(self.btn1, 0, wx.TOP|wx.ALIGN_LEFT, 20)


        sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(p, 1, wx.EXPAND)
        sizer.Add(grid_sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)
        self.SetSizer(sizer)

        wx.CallAfter(self.Layout)

