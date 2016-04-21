#coding:utf-8


import	wx
from tools import ConnectDev


mode_enter = {
    u'':0,
    u'Охрана':1,
    u'Тревога':2,
    u'Пожар':3,
    u'Питание':4,
    u'ПНЦ':5,
    u'Доступ':6,
    u'Выключение вентиляции':7,
    u'Тревога + пожар':8,
    u'Готовность':9,
    u'Пожар + строб':10,
    u'Панель + строб':11,
    u'Биппер':12,
    u'Статус охраны':13,
    u'Дистанционное управление':14,
    u'Термостат':15,
    u'Свет на вход':16,
    u'Питание пожарных датчиков':17,
    u'Отключение 220':20
}




class OutPuts(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Выходы")


        self.head_0 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_1 = wx.StaticText(self, wx.ID_ANY, (u"1"))
        self.head_2 = wx.StaticText(self, wx.ID_ANY, (u"2"))
        self.head_3 = wx.StaticText(self, wx.ID_ANY, (u"3"))
        self.head_4 = wx.StaticText(self, wx.ID_ANY, (u"4"))
        self.head_5 = wx.StaticText(self, wx.ID_ANY, (u"5"))
        self.head_6 = wx.StaticText(self, wx.ID_ANY, (u"6"))
        self.head_7 = wx.StaticText(self, wx.ID_ANY, (u"7"))

        self.left_1 = wx.StaticText(self, wx.ID_ANY, (u"Режим"))
        self.ch_1 = wx.wx.ComboBox(self, -1, "", (-1,-1), (130, -1), mode_enter.keys(), wx.CB_DROPDOWN|wx.CB_READONLY)
        self.ch_2 = wx.wx.ComboBox(self, -1, "", (-1,-1), (130, -1), mode_enter.keys(), wx.CB_DROPDOWN|wx.CB_READONLY)
        self.ch_3 = wx.wx.ComboBox(self, -1, "", (-1,-1), (130, -1), mode_enter.keys(), wx.CB_DROPDOWN|wx.CB_READONLY)
        self.ch_4 = wx.wx.ComboBox(self, -1, "", (-1,-1), (130, -1), mode_enter.keys(), wx.CB_DROPDOWN|wx.CB_READONLY)
        self.ch_5 = wx.wx.ComboBox(self, -1, "", (-1,-1), (130, -1), mode_enter.keys(), wx.CB_DROPDOWN|wx.CB_READONLY)
        self.ch_6 = wx.wx.ComboBox(self, -1, "", (-1,-1), (130, -1), mode_enter.keys(), wx.CB_DROPDOWN|wx.CB_READONLY)
        self.ch_7 = wx.wx.ComboBox(self, -1, "", (-1,-1), (130, -1), mode_enter.keys(), wx.CB_DROPDOWN|wx.CB_READONLY)

        self.left_2 = wx.StaticText(self, wx.ID_ANY, (u"Время,сек"))
        self.sc_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc_3 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc_4 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc_5 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc_6 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc_7 = wx.SpinCtrl(self, -1, "", (30, 30))

        self.sc_1.SetRange(0,255)
        self.sc_2.SetRange(0,255)
        self.sc_3.SetRange(0,255)
        self.sc_4.SetRange(0,255)
        self.sc_5.SetRange(0,255)
        self.sc_6.SetRange(0,255)
        self.sc_7.SetRange(0,255)

        self.left_3 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 1"))
        self.cb1_1 = wx.CheckBox(self, -1, "")
        self.cb1_2 = wx.CheckBox(self, -1, "")
        self.cb1_3 = wx.CheckBox(self, -1, "")
        self.cb1_4 = wx.CheckBox(self, -1, "")
        self.cb1_5 = wx.CheckBox(self, -1, "")
        self.cb1_6 = wx.CheckBox(self, -1, "")
        self.cb1_7 = wx.CheckBox(self, -1, "")

        self.left_4 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 2"))
        self.cb2_1 = wx.CheckBox(self, -1, "")
        self.cb2_2 = wx.CheckBox(self, -1, "")
        self.cb2_3 = wx.CheckBox(self, -1, "")
        self.cb2_4 = wx.CheckBox(self, -1, "")
        self.cb2_5 = wx.CheckBox(self, -1, "")
        self.cb2_6 = wx.CheckBox(self, -1, "")
        self.cb2_7 = wx.CheckBox(self, -1, "")

        self.left_5 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 3"))
        self.cb3_1 = wx.CheckBox(self, -1, "")
        self.cb3_2 = wx.CheckBox(self, -1, "")
        self.cb3_3 = wx.CheckBox(self, -1, "")
        self.cb3_4 = wx.CheckBox(self, -1, "")
        self.cb3_5 = wx.CheckBox(self, -1, "")
        self.cb3_6 = wx.CheckBox(self, -1, "")
        self.cb3_7 = wx.CheckBox(self, -1, "")

        self.left_6 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 4"))
        self.cb4_1 = wx.CheckBox(self, -1, "")
        self.cb4_2 = wx.CheckBox(self, -1, "")
        self.cb4_3 = wx.CheckBox(self, -1, "")
        self.cb4_4 = wx.CheckBox(self, -1, "")
        self.cb4_5 = wx.CheckBox(self, -1, "")
        self.cb4_6 = wx.CheckBox(self, -1, "")
        self.cb4_7 = wx.CheckBox(self, -1, "")

        self.left_7 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 5"))
        self.cb5_1 = wx.CheckBox(self, -1, "")
        self.cb5_2 = wx.CheckBox(self, -1, "")
        self.cb5_3 = wx.CheckBox(self, -1, "")
        self.cb5_4 = wx.CheckBox(self, -1, "")
        self.cb5_5 = wx.CheckBox(self, -1, "")
        self.cb5_6 = wx.CheckBox(self, -1, "")
        self.cb5_7 = wx.CheckBox(self, -1, "")

        self.left_8 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 6"))
        self.cb6_1 = wx.CheckBox(self, -1, "")
        self.cb6_2 = wx.CheckBox(self, -1, "")
        self.cb6_3 = wx.CheckBox(self, -1, "")
        self.cb6_4 = wx.CheckBox(self, -1, "")
        self.cb6_5 = wx.CheckBox(self, -1, "")
        self.cb6_6 = wx.CheckBox(self, -1, "")
        self.cb6_7 = wx.CheckBox(self, -1, "")

        self.left_9 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 7"))
        self.cb7_1 = wx.CheckBox(self, -1, "")
        self.cb7_2 = wx.CheckBox(self, -1, "")
        self.cb7_3 = wx.CheckBox(self, -1, "")
        self.cb7_4 = wx.CheckBox(self, -1, "")
        self.cb7_5 = wx.CheckBox(self, -1, "")
        self.cb7_6 = wx.CheckBox(self, -1, "")
        self.cb7_7 = wx.CheckBox(self, -1, "")

        self.left_10 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 8"))
        self.cb8_1 = wx.CheckBox(self, -1, "")
        self.cb8_2 = wx.CheckBox(self, -1, "")
        self.cb8_3 = wx.CheckBox(self, -1, "")
        self.cb8_4 = wx.CheckBox(self, -1, "")
        self.cb8_5 = wx.CheckBox(self, -1, "")
        self.cb8_6 = wx.CheckBox(self, -1, "")
        self.cb8_7 = wx.CheckBox(self, -1, "")


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        p = wx.Panel(self)


        grid_sizer_1 = wx.FlexGridSizer(12, 8, 1, 0)

        grid_sizer_1.Add(self.head_0, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.head_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.head_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.head_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.head_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.head_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.head_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.head_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.ch_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.ch_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.ch_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.ch_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.ch_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.ch_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.ch_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.sc_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb1_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb2_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb3_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb4_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb4_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb4_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb4_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb4_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb4_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb4_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_7, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb5_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb5_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb5_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb5_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb5_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb5_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb5_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_8, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb6_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb6_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb6_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb6_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb6_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb6_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb6_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_9, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb7_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb7_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb7_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb7_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb7_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb7_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb7_7, 0, wx.ALL, 10)

        grid_sizer_1.Add(self.left_10, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb8_1, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb8_2, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb8_3, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb8_4, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb8_5, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb8_6, 0, wx.ALL, 10)
        grid_sizer_1.Add(self.cb8_7, 0, wx.ALL, 10)



        grid_sizer_1.Add(self.btn, 0, wx.TOP|wx.ALIGN_RIGHT, 20)
        grid_sizer_1.Add(self.btn1, 0, wx.TOP|wx.ALIGN_LEFT, 20)


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid_sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)
        self.SetSizer(sizer)

        wx.CallAfter(self.Layout)


        self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)






    def Write(self, event):

        client = ConnectDev()
        client.connect()

        r = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

        r[0] = mode_enter[self.ch_1.GetValue()]
        r[1] = mode_enter[self.ch_2.GetValue()]
        r[2] = mode_enter[self.ch_3.GetValue()]
        r[3] = mode_enter[self.ch_4.GetValue()]
        r[4] = mode_enter[self.ch_5.GetValue()]
        r[5] = mode_enter[self.ch_6.GetValue()]
        r[6] = mode_enter[self.ch_7.GetValue()]
        r[7] = self.sc_1.GetValue()
        r[8] = self.sc_2.GetValue()
        r[9] = self.sc_3.GetValue()
        r[10] = self.sc_4.GetValue()
        r[11] = self.sc_5.GetValue()
        r[12] = self.sc_6.GetValue()
        r[13] = self.sc_7.GetValue()

        rq=client.write_registers(1066,r,unit=1)

        bb = [0,0,0,0,0,0,0]
        cc = ['','','','','','','']

        for item in range(0,7):

            a = eval("self.cb1_%s.GetValue()" % (item+1))
            b = eval("self.cb2_%s.GetValue()" % (item+1))
            c = eval("self.cb3_%s.GetValue()" % (item+1))
            d = eval("self.cb4_%s.GetValue()" % (item+1))
            e = eval("self.cb5_%s.GetValue()" % (item+1))
            f = eval("self.cb6_%s.GetValue()" % (item+1))
            g = eval("self.cb7_%s.GetValue()" % (item+1))
            h = eval("self.cb8_%s.GetValue()" % (item+1))



            if a:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]
            if b:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]
            if c:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]
            if d:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]
            if e:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]
            if f:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]
            if g:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]
            if h:
                cc[item] = "1"+cc[item]
            else:
                cc[item] = "0"+cc[item]


        for i in range(0,7):
            bb[i] = int(cc[i],2)

        rq=client.write_registers(1128,bb,unit=1)

        client.close()





    def Read(self, event):


        client = ConnectDev()
        client.connect()

        rr = client.read_holding_registers(address=1066,count=14,unit=1)
        result = rr.registers

        list_keys = mode_enter.keys()
        list_values = mode_enter.values()

        self.ch_1.SetValue(list_keys[list_values.index(result[0])])
        self.ch_2.SetValue(list_keys[list_values.index(result[1])])
        self.ch_3.SetValue(list_keys[list_values.index(result[2])])
        self.ch_4.SetValue(list_keys[list_values.index(result[3])])
        self.ch_5.SetValue(list_keys[list_values.index(result[4])])
        self.ch_6.SetValue(list_keys[list_values.index(result[5])])
        self.ch_7.SetValue(list_keys[list_values.index(result[6])])
        self.sc_1.SetValue(result[7])
        self.sc_2.SetValue(result[8])
        self.sc_3.SetValue(result[9])
        self.sc_4.SetValue(result[10])
        self.sc_5.SetValue(result[11])
        self.sc_6.SetValue(result[12])
        self.sc_7.SetValue(result[13])

        rr = client.read_holding_registers(address=1128,count=7,unit=1)
        result = rr.registers


        for item in range(0,7):
            i = bin(result[item])[2:]
            a = "00000000"+i
            b = a[-8:]


            if b[7] == "1":
                eval("self.cb1_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb1_%s.SetValue(False)" % (item+1))

            if b[6] == "1":
                eval("self.cb2_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb2_%s.SetValue(False)" % (item+1))

            if b[5] == "1":
                eval("self.cb3_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb3_%s.SetValue(False)" % (item+1))

            if b[4] == "1":
                eval("self.cb4_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb4_%s.SetValue(False)" % (item+1))

            if b[3] == "1":
                eval("self.cb5_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb5_%s.SetValue(False)" % (item+1))

            if b[2] == "1":
                eval("self.cb6_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb6_%s.SetValue(False)" % (item+1))

            if b[1] == "1":
                eval("self.cb7_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb7_%s.SetValue(False)" % (item+1))

            if b[0] == "1":
                eval("self.cb8_%s.SetValue(True)" % (item+1))
            else:
                eval("self.cb8_%s.SetValue(False)" % (item+1))


        client.close()