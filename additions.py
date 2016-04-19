#coding:utf-8


import	wx
import  shelve
import sys


from pymodbus.client.sync import ModbusSerialClient as ModbusClient


CFG_FILE = 'cfg.data'
db = shelve.open(CFG_FILE)
dev = db['dev']
db.close()






class Settings(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Дополнительные настройки")


        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"Офицер вкл./выкл."))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (u"Вкл./выкл. сообщений постоновки/снятия зон"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (u"Идентификация панели"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, (u"Чувствительность охранных зон"))
        self.label_5 = wx.StaticText(self, wx.ID_ANY, (u"Период запросов присутствия к серверу в сек"))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, (u"Уровень падения сигнала модема\nдля отправки сообщения на сервер"))
        self.label_7 = wx.StaticText(self, wx.ID_ANY, (u"Уровень сигнала модема для сообщения\nниже которого будет отправлено\nсообщение на сервер"))

        self.cb1 = wx.CheckBox(self, -1, "")
        self.cb2 = wx.CheckBox(self, -1, "")
        self.sc1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc3 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc4 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc5 = wx.SpinCtrl(self, -1, "", (30, 30))

        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)

        self.sc2.SetRange(50,1000)
        self.sc2.SetRange(0,60)
        self.sc2.SetRange(5,90)
        self.sc2.SetRange(0,98)

        grid_sizer_1 = wx.FlexGridSizer(8, 2, 1, 0)

        grid_sizer_1.Add(self.label_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc1, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc2, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc3, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc4, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_7, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc5, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.btn, 0, wx.TOP|wx.ALIGN_RIGHT, 20)
        grid_sizer_1.Add(self.btn1, 0, wx.TOP|wx.ALIGN_LEFT, 20)


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid_sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)
        self.SetSizer(sizer)

        wx.CallAfter(self.Layout)

        self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)




    def Write(self, event):

        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()

        rq=client.write_registers(1127,[self.sc1.GetValue()],unit=1)


        if self.cb1.GetValue():
            b = "1"
        else:
            b = "0"
        if self.cb2.GetValue():
            b = "1"+b
        else:
            b = "0"+b

        rq=client.write_registers(1117,[self.sc2.GetValue(),int(b,2)],unit=1)

        rq=client.write_registers(1138,[self.sc3.GetValue(),self.sc4.GetValue(),self.sc5.GetValue()],unit=1)


        client.close()





    def Read(self, event):


        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()

        rr = client.read_holding_registers(address=1117,count=2,unit=1)
        result = rr.registers

        self.sc2.SetValue(result[0])

        if ("00"+(bin(result[1]))[2:])[-1] == '1':
            self.cb1.SetValue(True)
        else:
            self.cb1.SetValue(False)

        if ("00"+(bin(result[1]))[2:])[-2] == '1':
            self.cb2.SetValue(True)
        else:
            self.cb2.SetValue(False)


        rr = client.read_holding_registers(address=1127,count=1,unit=1)
        result = rr.registers

        self.sc1.SetValue(result[0])

        rr = client.read_holding_registers(address=1138,count=3,unit=1)
        result = rr.registers

        self.sc3.SetValue(result[0])
        self.sc4.SetValue(result[1])
        self.sc5.SetValue(result[2])

        client.close()