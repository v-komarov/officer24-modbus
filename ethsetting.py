#coding:utf-8

from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from    tools import    Registr2ip,Ip2registr

import  wx, wx.aui
import  shelve


CFG_FILE = 'cfg.data'





class EthSetting(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Ethernet")

        db = shelve.open(CFG_FILE)
        self.dev = db['dev']
        db.close()


        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"IP устройства"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (u"маска устройства"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (u"IP адрес сервера"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, (u"Порт сервера"))
        self.label_5 = wx.StaticText(self, wx.ID_ANY, (u"Шлюз"))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, (u"Использовать Ethernet"))
        self.label_7 = wx.StaticText(self, wx.ID_ANY, (u"Использовать DHCP"))


        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.cb1 = wx.CheckBox(self, -1, "")
        self.cb2 = wx.CheckBox(self, -1, "")


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        p = wx.Panel(self)
        #wx.StaticText(p, -1,"двыдвыдвыдвлдвл")
        #p.SetBackgroundColour('light blue')


        grid_sizer_1 = wx.FlexGridSizer(8, 2, 1, 0)

        ### Использовать Ethernet и DHCP
        grid_sizer_1.Add(self.label_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_7, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2, 0, wx.ALL, 10)

        ### IP устройства, шлюз
        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_5, 0, wx.ALL, 10)

        ### Адрес и порт сервера
        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_4, 0, wx.ALL, 10)

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


        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)
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


        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)
        client.connect()


        ### IP адрес сервера
        rr = client.read_holding_registers(address=10,count=2,unit=1)
        result = rr.registers
        self.text_ctrl_3.SetValue(Registr2ip(result))

        ### Порт сервера
        rr = client.read_holding_registers(address=15,count=1,unit=1)
        result = rr.registers
        port = hex(result[0])
        port_string = "%s" % int(port,16)
        self.text_ctrl_4.SetValue(port_string)

        ### Шлюз
        rr = client.read_holding_registers(address=148,count=2,unit=1)
        result = rr.registers
        self.text_ctrl_5.SetValue(Registr2ip(result))

        ### Использовать Etherner
        rr = client.read_holding_registers(address=146,count=1,unit=1)
        result = rr.registers
        if result[0] == 1:
            self.cb1.SetValue(True)
        else:
            self.cb1.SetValue(False)



        ### Использовать DHCP
        rr = client.read_holding_registers(address=147,count=1,unit=1)
        result = rr.registers
        if result[0] == 1:
            self.cb2.SetValue(True)
        else:
            self.cb2.SetValue(False)


        ### IP адрес устройства
        rr = client.read_holding_registers(address=152,count=2,unit=1)
        result = rr.registers
        self.text_ctrl_1.SetValue(Registr2ip(result))


        ### Маска устройства
        rr = client.read_holding_registers(address=150,count=2,unit=1)
        result = rr.registers
        self.text_ctrl_2.SetValue(Registr2ip(result))


        client.close()