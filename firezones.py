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
        self.sc.SetRange(0,8)
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


        if self.cb2.GetValue():
            b1 = '1'
        else:
            b1 = '0'
        if self.cb1.GetValue():
            b2 = '1'
        else:
            b2 = '0'
        if self.cb3.GetValue():
            b3 = '1'
        else:
            b3 = '0'

        b = "00000%s%s%s" % (b3,b2,b1)

        c = bin(self.sc.GetValue())

        #print c+b

        d = int(c+b,2)


        rq=client.write_registers(1115,[d],unit=1)


        client.close()







    def Read(self, event):


        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()


        rr = client.read_holding_registers(address=1115,count=1,unit=1)
        result = rr.registers



        a = (bin(result[0]))[2:]
        b = a[-8:]
        c = a[-16:-8]

        #print a,b,c

        ### Пожарная зона в разделе
        c1 = int(c,2)
        ## Пожарная зона вкл
        b1 = b[-1]
        ## Авт. сброс пожарной зоны
        b2 = b[-2]
        ## Двойная сработка пож.
        b3 = b[-3]

        self.sc.SetValue(c1)
        if b1 == '1':
            self.cb2.SetValue(True)
        else:
            self.cb2.SetValue(False)
        if b2 == '1':
            self.cb1.SetValue(True)
        else:
            self.cb1.SetValue(False)
        if b3 == '1':
            self.cb3.SetValue(True)
        else:
            self.cb3.SetValue(False)

        client.close()






class FireZone2(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Пожарная зона 2")



        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"Пожарная зона 2 в разделе"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (u"Автоматический сброс 2 пож. зоны"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (u"Пожарная зона 2 вкл."))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, (u"Двойная сработка пож. 2"))


        self.sc = wx.SpinCtrl(self, -1, "", (30, 50))
        self.sc.SetRange(0,8)


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


        if self.cb2.GetValue():
            b1 = '1'
        else:
            b1 = '0'
        if self.cb1.GetValue():
            b2 = '1'
        else:
            b2 = '0'
        if self.cb3.GetValue():
            b3 = '1'
        else:
            b3 = '0'

        b = "00000%s%s%s" % (b3,b2,b1)

        c = bin(self.sc.GetValue())

        #print c+b

        d = int(c+b,2)


        rq=client.write_registers(1116,[d],unit=1)


        client.close()




    def Read(self, event):


        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()


        rr = client.read_holding_registers(address=1116,count=1,unit=1)
        result = rr.registers



        a = (bin(result[0]))[2:]
        b = a[-8:]
        c = a[-16:-8]

        #print a,b,c

        ### Пожарная зона в разделе
        c1 = int(c,2)
        ## Пожарная зона вкл
        b1 = b[-1]
        ## Авт. сброс пожарной зоны
        b2 = b[-2]
        ## Двойная сработка пож.
        b3 = b[-3]

        self.sc.SetValue(c1)
        if b1 == '1':
            self.cb2.SetValue(True)
        else:
            self.cb2.SetValue(False)
        if b2 == '1':
            self.cb1.SetValue(True)
        else:
            self.cb1.SetValue(False)
        if b3 == '1':
            self.cb3.SetValue(True)
        else:
            self.cb3.SetValue(False)

        client.close()


