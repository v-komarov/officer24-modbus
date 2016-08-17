#coding:utf-8


import	wx
import sys
import  wx.lib.mixins.listctrl  as  listmix
import wx.lib.scrolledpanel as scrolled


from    tools import Read2bytes,StrRevers,Write16key,ConnectDev
from tools import Saved





class Keys(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Ключи")



        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)
        self.btn2 = wx.Button(self,-1, u"Считать ключ")
        self.btn3 = wx.Button(self, wx.ID_CLEAR)


        sizer = wx.BoxSizer(wx.VERTICAL)

        # Текущий элемент
        self.fieldnow = None

        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        panel1 = scrolled.ScrolledPanel(self, -1, size=(550, 550), style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panel1" )
        fgs1 = wx.FlexGridSizer(cols=4, vgap=4, hgap=4)
        label = []
        self.keys = []
        label2 = []
        self.sections = []
        for i in range(0,128):
            label.append(wx.StaticText(panel1, -1, u"Ключ %s" % (i+1)))
            self.keys.append(wx.TextCtrl(panel1, -1, '', size=(200,-1)))
            label2.append(wx.StaticText(panel1, -1, u"Раздел"))
            self.sections.append(wx.SpinCtrl(panel1, -1, "", (10, -1)))
            self.sections[i].SetRange(0,8)

            fgs1.Add(label[i], flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border=10)
            fgs1.Add(self.keys[i], flag=wx.RIGHT, border=10)
            fgs1.Add(label2[i], flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border=10)
            fgs1.Add(self.sections[i], flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL | wx.LEFT, border=10)

            self.keys[i].Bind(wx.EVT_KILL_FOCUS, self.OnTextCtrlKillFocus)
            self.keys[i].Bind(wx.EVT_SET_FOCUS, self.OnTextCtrlSetFocus)


        panel1.SetSizer( fgs1 )
        panel1.SetAutoLayout(1)
        panel1.SetupScrolling()

        sizer_1.Add(panel1,0)
        sizer.Add(sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)


        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.btn,0)
        sizer_2.Add(self.btn1,0)
        sizer_2.Add(self.btn2,0)
        sizer_2.Add(self.btn3,0)
        sizer.Add(sizer_2,0, wx.ALL|wx.ALIGN_LEFT, border=20)


        self.SetSizer(sizer)
        wx.CallAfter(self.Layout)


        self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.ReadKey, self.btn2)
        self.Bind(wx.EVT_BUTTON, self.ClearKey, self.btn3)





    def OnTextCtrlKillFocus(self,event):
        self.fieldnow.SetBackgroundColour("")
        #self.fieldnow[event.GetEventObject()] = False



    def OnTextCtrlSetFocus(self,event):
        self.fieldnow = event.GetEventObject()
        self.fieldnow.SetBackgroundColour("Yellow")





    def ClearKey(self,evt):

        if self.fieldnow:
            self.fieldnow.SetValue("0000000000000000")





    def Read(self,evt):

        client = ConnectDev()
        client.connect()

        ### Ключи пользователей
        ### Регистр 162 , читать 8 * 128 = 1024
        data_key = []
        adr = 512
        reg = 162
        step = 64

        while adr > 0 :
            rr = client.read_holding_registers(address=reg,count=step,unit=1)
            result = rr.registers
            adr = adr - step
            reg = reg + step
            data_key.extend(result)

        ### Разделы пользователей
        data_part = []
        adr = 128
        reg = 930
        step = 64

        while adr > 0 :
            rr = client.read_holding_registers(address=reg,count=step,unit=1)
            result = rr.registers
            adr = adr - step
            reg = reg + step
            data_part.extend(result)

        client.close()



        for i in range(0,128):

            b8 = data_key[0:4]
            del data_key[0:4]
            result = "%s%s%s%s" % (Read2bytes(b8[0]),Read2bytes(b8[1]),Read2bytes(b8[2]),Read2bytes(b8[3]))
            self.keys[i].SetValue(result)

            part = data_part[0]
            del data_part[0]
            self.sections[i].SetValue(part)





    def Write(self,evt):
        data_key = []
        data_part = []
        for i in range(0,128):
            data_key.extend(Write16key(self.keys[i].GetValue()))
            data_part.append(int(self.sections[i].GetValue()))


        client = ConnectDev()
        client.connect()

        ### Ключи пользователей
        ### Регистр 162 , читать 8 * 128 = 1024
        adr = 512
        reg = 162
        step = 64

        while adr > 0 :
            result = data_key[:step]
            del data_key[:step]
            rq=client.write_registers(reg,result,unit=1)
            adr = adr - step
            reg = reg + step


        ### Разделы пользователей
        adr = 128
        reg = 930
        step = 64

        while adr > 0 :
            result = data_part[:step]
            del data_part[:step]
            rq=client.write_registers(reg,result,unit=1)
            adr = adr - step
            reg = reg + step

        client.close()

        Saved(self)





    def ReadKey(self,event):

        client = ConnectDev()
        client.connect()

        rr = client.read_holding_registers(address=2064,count=4,unit=1)
        result = rr.registers
        client.close()

        result = "%s%s%s%s" % (Read2bytes(result[0]),Read2bytes(result[1]),Read2bytes(result[2]),Read2bytes(result[3]))

        if self.fieldnow:
            self.fieldnow.SetValue(result)










class MasterKey(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Мастер ключ")


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)
        self.btn2 = wx.Button(self,-1, u"Считать ключ")


        self.label_1 = wx.StaticText(self, wx.ID_ANY, (u"Мастер ключ"))
        self.text_ctrl_1 = wx.TextCtrl(self, wx.ID_ANY, "", size=(200,-1))



        sizer = wx.BoxSizer(wx.VERTICAL)


        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)

        sizer_1.Add(self.label_1,0,wx.TOP|wx.ALIGN_LEFT, border=15)
        sizer_1.Add(self.text_ctrl_1,0,wx.ALL|wx.ALIGN_LEFT, border=10)

        sizer.Add(sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.btn,0)
        sizer_2.Add(self.btn1,0)
        sizer_2.Add(self.btn2,0)
        sizer.Add(sizer_2,0, wx.ALL|wx.ALIGN_LEFT, border=20)


        self.SetSizer(sizer)
        wx.CallAfter(self.Layout)


        self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.ReadKey, self.btn2)



    def Read(self, evt):
        client = ConnectDev()
        client.connect()

        rr = client.read_holding_registers(address=158,count=4,unit=1)
        result = rr.registers
        client.close()

        result = "%s%s%s%s" % (Read2bytes(result[0]),Read2bytes(result[1]),Read2bytes(result[2]),Read2bytes(result[3]))

        self.text_ctrl_1.SetValue(StrRevers(result))






    def Write(self,event):
        result = self.text_ctrl_1.GetValue()

        client = ConnectDev()
        client.connect()

        rq=client.write_registers(158,Write16key(result),unit=1)

        client.close()

        Saved(self)



    def ReadKey(self,event):
        client = ConnectDev()
        client.connect()

        rr = client.read_holding_registers(address=2064,count=4,unit=1)
        result = rr.registers
        client.close()

        result = "%s%s%s%s" % (Read2bytes(result[0]),Read2bytes(result[1]),Read2bytes(result[2]),Read2bytes(result[3]))

        self.text_ctrl_1.SetValue(StrRevers(result))
















