#coding:utf-8

import  wx, wx.aui
from    tools import    Registr2ip,Ip2registr,ConnectDev,Reg2Word,Word2Reg
from tools import Saved






class GSMSetting(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"GSM")


        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"Адрес сервера GSM1"))
        self.label_2 = wx.StaticText(self, wx.ID_ANY, (u"Адрес сервера GSM2"))
        self.label_3 = wx.StaticText(self, wx.ID_ANY, (u"Порт сервера GSM1"))
        self.label_4 = wx.StaticText(self, wx.ID_ANY, (u"Порт сервера GSM2"))
        self.label_5 = wx.StaticText(self, wx.ID_ANY, (u"APN 1"))
        self.label_6 = wx.StaticText(self, wx.ID_ANY, (u"APN 2"))
        self.label_7 = wx.StaticText(self, wx.ID_ANY, (u"User 1"))
        self.label_8 = wx.StaticText(self, wx.ID_ANY, (u"User 2"))
        self.label_9 = wx.StaticText(self, wx.ID_ANY, (u"Password 1"))
        self.label_10 = wx.StaticText(self, wx.ID_ANY, (u"Password 2"))

        self.label_11 = wx.StaticText(self, wx.ID_ANY, (u"Адрес сервера основной"))
        self.label_12 = wx.StaticText(self, wx.ID_ANY, (u"Порт сервера основной"))

        self.label_13 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.label_14 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.label_15 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.label_16 = wx.StaticText(self, wx.ID_ANY, (u""))


        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_2 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_3 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_4 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_5 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_6 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_7 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_8 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_9 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_10 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_11 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))
        self.text_ctrl_12 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        p = wx.Panel(self)


        grid_sizer_1 = wx.FlexGridSizer(9, 4, 1, 0)

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

        grid_sizer_1.Add(self.label_7, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_7, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_8, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_8, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_9, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_9, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_10, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_10, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_13, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_14, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_15, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_16, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.label_11, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_11, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.label_12, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.text_ctrl_12, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.btn, 0, wx.TOP|wx.ALIGN_RIGHT, 20)
        grid_sizer_1.Add(self.btn1, 0, wx.TOP|wx.ALIGN_LEFT, 20)


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid_sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)
        self.SetSizer(sizer)

        wx.CallAfter(self.Layout)



        self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)





    def Write(self,event):


        client = ConnectDev()
        client.connect()


        ### IP адрес сервера основной (4,5)
        ### IP адрес сервера GSM1(6,7)
        ### IP адрес сервера GSM2 (8,9)

        result = []

        result.extend(Ip2registr(self.text_ctrl_11.GetValue()))
        result.extend(Ip2registr(self.text_ctrl_1.GetValue()))
        result.extend(Ip2registr(self.text_ctrl_2.GetValue()))
        rq=client.write_registers(4,result,unit=1)

        ### Порт сервера основной (12)
        ### Порт сервера GSM1 (13)
        ### Порт сервера GSM2 (14)

        result = [int(self.text_ctrl_12.GetValue(),10),int(self.text_ctrl_3.GetValue(),10),int(self.text_ctrl_4.GetValue(),10)]
        rq=client.write_registers(12,result,unit=1)

        result = []
        result.extend(Word2Reg(self.text_ctrl_5.GetValue(),16))
        result.extend(Word2Reg(self.text_ctrl_6.GetValue(),16))
        result.extend(Word2Reg(self.text_ctrl_7.GetValue(),8))
        result.extend(Word2Reg(self.text_ctrl_8.GetValue(),8))
        result.extend(Word2Reg(self.text_ctrl_9.GetValue(),8))
        result.extend(Word2Reg(self.text_ctrl_10.GetValue(),8))

        rq=client.write_registers(16,result,unit=1)

        client.close()

        Saved(self)







    def Read(self, event):


        client = ConnectDev()
        client.connect()

        ### IP адрес сервера основной (4,5)
        ### IP адрес сервера GSM1(6,7)
        ### IP адрес сервера GSM2 (8,9)

        rr = client.read_holding_registers(address=4,count=6,unit=1)
        result = rr.registers
        self.text_ctrl_11.SetValue(Registr2ip([result[0],result[1]]))
        self.text_ctrl_1.SetValue(Registr2ip([result[2],result[3]]))
        self.text_ctrl_2.SetValue(Registr2ip([result[4],result[5]]))

        ### Порт сервера основной (12)
        ### Порт сервера GSM1 (13)
        ### Порт сервера GSM2 (14)

        rr = client.read_holding_registers(address=12,count=3,unit=1)
        result = rr.registers
        self.text_ctrl_12.SetValue("%s" % result[0])
        self.text_ctrl_3.SetValue("%s" % result[1])
        self.text_ctrl_4.SetValue("%s" % result[2])

        ### APN,User,Password
        rr = client.read_holding_registers(address=16,count=64,unit=1)
        result = rr.registers

        self.text_ctrl_5.SetValue(Reg2Word(result[0:16]))
        self.text_ctrl_6.SetValue(Reg2Word(result[16:32]))
        self.text_ctrl_7.SetValue(Reg2Word(result[32:40]))
        self.text_ctrl_8.SetValue(Reg2Word(result[40:48]))
        self.text_ctrl_9.SetValue(Reg2Word(result[48:56]))
        self.text_ctrl_10.SetValue(Reg2Word(result[56:64]))

        client.close()