#coding:utf-8

import  wx
from tools import ConnectDev




class Zones(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Зоны")


        self.head_0 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_1 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_2 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_3 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_4 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_5 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_6 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_7 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_8 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_9 = wx.StaticText(self, wx.ID_ANY, (u"З"))
        self.head_10 = wx.StaticText(self, wx.ID_ANY, (u"О"))
        self.head_11 = wx.StaticText(self, wx.ID_ANY, (u"Н"))
        self.head_12 = wx.StaticText(self, wx.ID_ANY, (u"Ы"))
        self.head_13 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_14 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_15 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_16 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_17 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head_18 = wx.StaticText(self, wx.ID_ANY, (u""))


        self.head2_0 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.head2_1 = wx.StaticText(self, wx.ID_ANY, (u"Вход"))
        self.head2_2 = wx.StaticText(self, wx.ID_ANY, (u"Выход"))
        self.head2_3 = wx.StaticText(self, wx.ID_ANY, (u"1"))
        self.head2_4 = wx.StaticText(self, wx.ID_ANY, (u"2"))
        self.head2_5 = wx.StaticText(self, wx.ID_ANY, (u"3"))
        self.head2_6 = wx.StaticText(self, wx.ID_ANY, (u"4"))
        self.head2_7 = wx.StaticText(self, wx.ID_ANY, (u"5"))
        self.head2_8 = wx.StaticText(self, wx.ID_ANY, (u"6"))
        self.head2_9 = wx.StaticText(self, wx.ID_ANY, (u"7"))
        self.head2_10 = wx.StaticText(self, wx.ID_ANY, (u"8"))
        self.head2_11 = wx.StaticText(self, wx.ID_ANY, (u"9"))
        self.head2_12 = wx.StaticText(self, wx.ID_ANY, (u"10"))
        self.head2_13 = wx.StaticText(self, wx.ID_ANY, (u"11"))
        self.head2_14 = wx.StaticText(self, wx.ID_ANY, (u"12"))
        self.head2_15 = wx.StaticText(self, wx.ID_ANY, (u"13"))
        self.head2_16 = wx.StaticText(self, wx.ID_ANY, (u"14"))
        self.head2_17 = wx.StaticText(self, wx.ID_ANY, (u"15"))
        self.head2_18 = wx.StaticText(self, wx.ID_ANY, (u"16"))


        self.left_1 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 1"))
        self.sc1_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc1_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb1_1 = wx.CheckBox(self, -1, "")
        self.cb1_2 = wx.CheckBox(self, -1, "")
        self.cb1_3 = wx.CheckBox(self, -1, "")
        self.cb1_4 = wx.CheckBox(self, -1, "")
        self.cb1_5 = wx.CheckBox(self, -1, "")
        self.cb1_6 = wx.CheckBox(self, -1, "")
        self.cb1_7 = wx.CheckBox(self, -1, "")
        self.cb1_8 = wx.CheckBox(self, -1, "")
        self.cb1_9 = wx.CheckBox(self, -1, "")
        self.cb1_10 = wx.CheckBox(self, -1, "")
        self.cb1_11 = wx.CheckBox(self, -1, "")
        self.cb1_12 = wx.CheckBox(self, -1, "")
        self.cb1_13 = wx.CheckBox(self, -1, "")
        self.cb1_14 = wx.CheckBox(self, -1, "")
        self.cb1_15 = wx.CheckBox(self, -1, "")
        self.cb1_16 = wx.CheckBox(self, -1, "")


        self.left_2 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 2"))
        self.sc2_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc2_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb2_1 = wx.CheckBox(self, -1, "")
        self.cb2_2 = wx.CheckBox(self, -1, "")
        self.cb2_3 = wx.CheckBox(self, -1, "")
        self.cb2_4 = wx.CheckBox(self, -1, "")
        self.cb2_5 = wx.CheckBox(self, -1, "")
        self.cb2_6 = wx.CheckBox(self, -1, "")
        self.cb2_7 = wx.CheckBox(self, -1, "")
        self.cb2_8 = wx.CheckBox(self, -1, "")
        self.cb2_9 = wx.CheckBox(self, -1, "")
        self.cb2_10 = wx.CheckBox(self, -1, "")
        self.cb2_11 = wx.CheckBox(self, -1, "")
        self.cb2_12 = wx.CheckBox(self, -1, "")
        self.cb2_13 = wx.CheckBox(self, -1, "")
        self.cb2_14 = wx.CheckBox(self, -1, "")
        self.cb2_15 = wx.CheckBox(self, -1, "")
        self.cb2_16 = wx.CheckBox(self, -1, "")


        self.left_3 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 3"))
        self.sc3_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc3_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb3_1 = wx.CheckBox(self, -1, "")
        self.cb3_2 = wx.CheckBox(self, -1, "")
        self.cb3_3 = wx.CheckBox(self, -1, "")
        self.cb3_4 = wx.CheckBox(self, -1, "")
        self.cb3_5 = wx.CheckBox(self, -1, "")
        self.cb3_6 = wx.CheckBox(self, -1, "")
        self.cb3_7 = wx.CheckBox(self, -1, "")
        self.cb3_8 = wx.CheckBox(self, -1, "")
        self.cb3_9 = wx.CheckBox(self, -1, "")
        self.cb3_10 = wx.CheckBox(self, -1, "")
        self.cb3_11 = wx.CheckBox(self, -1, "")
        self.cb3_12 = wx.CheckBox(self, -1, "")
        self.cb3_13 = wx.CheckBox(self, -1, "")
        self.cb3_14 = wx.CheckBox(self, -1, "")
        self.cb3_15 = wx.CheckBox(self, -1, "")
        self.cb3_16 = wx.CheckBox(self, -1, "")


        self.left_4 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 4"))
        self.sc4_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc4_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb4_1 = wx.CheckBox(self, -1, "")
        self.cb4_2 = wx.CheckBox(self, -1, "")
        self.cb4_3 = wx.CheckBox(self, -1, "")
        self.cb4_4 = wx.CheckBox(self, -1, "")
        self.cb4_5 = wx.CheckBox(self, -1, "")
        self.cb4_6 = wx.CheckBox(self, -1, "")
        self.cb4_7 = wx.CheckBox(self, -1, "")
        self.cb4_8 = wx.CheckBox(self, -1, "")
        self.cb4_9 = wx.CheckBox(self, -1, "")
        self.cb4_10 = wx.CheckBox(self, -1, "")
        self.cb4_11 = wx.CheckBox(self, -1, "")
        self.cb4_12 = wx.CheckBox(self, -1, "")
        self.cb4_13 = wx.CheckBox(self, -1, "")
        self.cb4_14 = wx.CheckBox(self, -1, "")
        self.cb4_15 = wx.CheckBox(self, -1, "")
        self.cb4_16 = wx.CheckBox(self, -1, "")


        self.left_5 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 5"))
        self.sc5_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc5_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb5_1 = wx.CheckBox(self, -1, "")
        self.cb5_2 = wx.CheckBox(self, -1, "")
        self.cb5_3 = wx.CheckBox(self, -1, "")
        self.cb5_4 = wx.CheckBox(self, -1, "")
        self.cb5_5 = wx.CheckBox(self, -1, "")
        self.cb5_6 = wx.CheckBox(self, -1, "")
        self.cb5_7 = wx.CheckBox(self, -1, "")
        self.cb5_8 = wx.CheckBox(self, -1, "")
        self.cb5_9 = wx.CheckBox(self, -1, "")
        self.cb5_10 = wx.CheckBox(self, -1, "")
        self.cb5_11 = wx.CheckBox(self, -1, "")
        self.cb5_12 = wx.CheckBox(self, -1, "")
        self.cb5_13 = wx.CheckBox(self, -1, "")
        self.cb5_14 = wx.CheckBox(self, -1, "")
        self.cb5_15 = wx.CheckBox(self, -1, "")
        self.cb5_16 = wx.CheckBox(self, -1, "")


        self.left_6 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 6"))
        self.sc6_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc6_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb6_1 = wx.CheckBox(self, -1, "")
        self.cb6_2 = wx.CheckBox(self, -1, "")
        self.cb6_3 = wx.CheckBox(self, -1, "")
        self.cb6_4 = wx.CheckBox(self, -1, "")
        self.cb6_5 = wx.CheckBox(self, -1, "")
        self.cb6_6 = wx.CheckBox(self, -1, "")
        self.cb6_7 = wx.CheckBox(self, -1, "")
        self.cb6_8 = wx.CheckBox(self, -1, "")
        self.cb6_9 = wx.CheckBox(self, -1, "")
        self.cb6_10 = wx.CheckBox(self, -1, "")
        self.cb6_11 = wx.CheckBox(self, -1, "")
        self.cb6_12 = wx.CheckBox(self, -1, "")
        self.cb6_13 = wx.CheckBox(self, -1, "")
        self.cb6_14 = wx.CheckBox(self, -1, "")
        self.cb6_15 = wx.CheckBox(self, -1, "")
        self.cb6_16 = wx.CheckBox(self, -1, "")


        self.left_7 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 7"))
        self.sc7_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc7_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb7_1 = wx.CheckBox(self, -1, "")
        self.cb7_2 = wx.CheckBox(self, -1, "")
        self.cb7_3 = wx.CheckBox(self, -1, "")
        self.cb7_4 = wx.CheckBox(self, -1, "")
        self.cb7_5 = wx.CheckBox(self, -1, "")
        self.cb7_6 = wx.CheckBox(self, -1, "")
        self.cb7_7 = wx.CheckBox(self, -1, "")
        self.cb7_8 = wx.CheckBox(self, -1, "")
        self.cb7_9 = wx.CheckBox(self, -1, "")
        self.cb7_10 = wx.CheckBox(self, -1, "")
        self.cb7_11 = wx.CheckBox(self, -1, "")
        self.cb7_12 = wx.CheckBox(self, -1, "")
        self.cb7_13 = wx.CheckBox(self, -1, "")
        self.cb7_14 = wx.CheckBox(self, -1, "")
        self.cb7_15 = wx.CheckBox(self, -1, "")
        self.cb7_16 = wx.CheckBox(self, -1, "")


        self.left_8 = wx.StaticText(self, wx.ID_ANY, (u"Раздел 8"))
        self.sc8_1 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.sc8_2 = wx.SpinCtrl(self, -1, "", (30, 30))
        self.cb8_1 = wx.CheckBox(self, -1, "")
        self.cb8_2 = wx.CheckBox(self, -1, "")
        self.cb8_3 = wx.CheckBox(self, -1, "")
        self.cb8_4 = wx.CheckBox(self, -1, "")
        self.cb8_5 = wx.CheckBox(self, -1, "")
        self.cb8_6 = wx.CheckBox(self, -1, "")
        self.cb8_7 = wx.CheckBox(self, -1, "")
        self.cb8_8 = wx.CheckBox(self, -1, "")
        self.cb8_9 = wx.CheckBox(self, -1, "")
        self.cb8_10 = wx.CheckBox(self, -1, "")
        self.cb8_11 = wx.CheckBox(self, -1, "")
        self.cb8_12 = wx.CheckBox(self, -1, "")
        self.cb8_13 = wx.CheckBox(self, -1, "")
        self.cb8_14 = wx.CheckBox(self, -1, "")
        self.cb8_15 = wx.CheckBox(self, -1, "")
        self.cb8_16 = wx.CheckBox(self, -1, "")


        self.left_91 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.left_92 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.left_93 = wx.StaticText(self, wx.ID_ANY, (u"Входная зона"))
        self.cb9_1 = wx.CheckBox(self, -1, "")
        self.cb9_2 = wx.CheckBox(self, -1, "")
        self.cb9_3 = wx.CheckBox(self, -1, "")
        self.cb9_4 = wx.CheckBox(self, -1, "")
        self.cb9_5 = wx.CheckBox(self, -1, "")
        self.cb9_6 = wx.CheckBox(self, -1, "")
        self.cb9_7 = wx.CheckBox(self, -1, "")
        self.cb9_8 = wx.CheckBox(self, -1, "")
        self.cb9_9 = wx.CheckBox(self, -1, "")
        self.cb9_10 = wx.CheckBox(self, -1, "")
        self.cb9_11 = wx.CheckBox(self, -1, "")
        self.cb9_12 = wx.CheckBox(self, -1, "")
        self.cb9_13 = wx.CheckBox(self, -1, "")
        self.cb9_14 = wx.CheckBox(self, -1, "")
        self.cb9_15 = wx.CheckBox(self, -1, "")
        self.cb9_16 = wx.CheckBox(self, -1, "")


        self.left_101 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.left_102 = wx.StaticText(self, wx.ID_ANY, (u""))
        self.left_103 = wx.StaticText(self, wx.ID_ANY, (u"Проходная зона"))
        self.cb10_1 = wx.CheckBox(self, -1, "")
        self.cb10_2 = wx.CheckBox(self, -1, "")
        self.cb10_3 = wx.CheckBox(self, -1, "")
        self.cb10_4 = wx.CheckBox(self, -1, "")
        self.cb10_5 = wx.CheckBox(self, -1, "")
        self.cb10_6 = wx.CheckBox(self, -1, "")
        self.cb10_7 = wx.CheckBox(self, -1, "")
        self.cb10_8 = wx.CheckBox(self, -1, "")
        self.cb10_9 = wx.CheckBox(self, -1, "")
        self.cb10_10 = wx.CheckBox(self, -1, "")
        self.cb10_11 = wx.CheckBox(self, -1, "")
        self.cb10_12 = wx.CheckBox(self, -1, "")
        self.cb10_13 = wx.CheckBox(self, -1, "")
        self.cb10_14 = wx.CheckBox(self, -1, "")
        self.cb10_15 = wx.CheckBox(self, -1, "")
        self.cb10_16 = wx.CheckBox(self, -1, "")


#        self.sc_3 = wx.SpinCtrl(self, -1, "", (30, 30))
#        self.sc_4 = wx.SpinCtrl(self, -1, "", (30, 30))
#        self.sc_5 = wx.SpinCtrl(self, -1, "", (30, 30))
#        self.sc_6 = wx.SpinCtrl(self, -1, "", (30, 30))
#        self.sc_7 = wx.SpinCtrl(self, -1, "", (30, 30))


        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        p = wx.Panel(self)


        grid_sizer_1 = wx.FlexGridSizer(13, 19, 1, 0)

        grid_sizer_1.Add(self.head_0, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_16, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_17, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head_18, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.head2_0, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_16, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_17, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.head2_18, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc1_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc1_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb1_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc2_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc2_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb2_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc3_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc3_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb3_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc4_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc4_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb4_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc5_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc5_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb5_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc6_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc6_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb6_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc7_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc7_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb7_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc8_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.sc8_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb8_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_91, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.left_92, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.left_93, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb9_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.left_101, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.left_102, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.left_103, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_1, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_2, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_3, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_4, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_5, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_6, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_7, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_8, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_9, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_10, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_11, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_12, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_13, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_14, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_15, 0, wx.ALL, 5)
        grid_sizer_1.Add(self.cb10_16, 0, wx.ALL, 5)


        grid_sizer_1.Add(self.btn, 0, wx.TOP|wx.ALIGN_RIGHT, 20)
        grid_sizer_1.Add(self.btn1, 0, wx.TOP|wx.ALIGN_LEFT, 20)


        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(grid_sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)
        self.SetSizer(sizer)

        wx.CallAfter(self.Layout)


        #self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        #self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)

