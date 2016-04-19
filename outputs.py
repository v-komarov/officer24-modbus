#coding:utf-8


import	wx
import  shelve
import sys
import  wx.lib.mixins.listctrl  as  listmix


from pymodbus.client.sync import ModbusSerialClient as ModbusClient


CFG_FILE = 'cfg.data'
db = shelve.open(CFG_FILE)
dev = db['dev']
db.close()




mode_enter = {
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





        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)


        sizer = wx.BoxSizer(wx.VERTICAL)


        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl0 = List(self, -1, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
        sizer_1.Add(self.ctrl0,0)

        sizer.Add(sizer_1,0, wx.ALL|wx.ALIGN_LEFT, border=20)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.btn,0)
        sizer_2.Add(self.btn1,0)
        sizer.Add(sizer_2,0, wx.ALL|wx.ALIGN_LEFT, border=20)


        self.SetSizer(sizer)
        wx.CallAfter(self.Layout)


        self.Bind(wx.EVT_BUTTON, self.Read, self.btn)
        self.Bind(wx.EVT_BUTTON, self.Write, self.btn1)
        self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)
        self.ctrl0.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu, self.ctrl0)
        self.ctrl0.Bind(wx.EVT_LIST_COL_CLICK, self.ReadCol, self.ctrl0)


    def Read(self, evt):
        self.ctrl0.Populate()
        self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


    def Write(self,event):

        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()


        client.close()



    #### --- Присвоение значение по выбранной строке ----
    def ReadItem(self,event):
        self.ctrl0.currentItem = event.m_itemIndex


    def ReadCol(self,event):
        self.ctrl0.currentCol = event.m_col




    def	ShowMenu(self,event):

        if self.ctrl0.currentCol in range(1,8) and self.ctrl0.currentItem == 0:
            self.menu=wx.Menu()

            for k in mode_enter.keys():
                self.menu.Append(wx.NewId(),k)

            self.menu.Bind(wx.EVT_MENU, self.SetMenuValue)
            self.PopupMenu(self.menu)
            self.menu.Destroy()

        if self.ctrl0.currentCol in range(1,8) and self.ctrl0.currentItem in range(2,9):

            self.menu=wx.Menu()
            self.menu.Append(wx.NewId(),"Нет")
            self.menu.Append(wx.NewId(),"Да")

            self.menu.Bind(wx.EVT_MENU, self.SetMenuValue)
            self.PopupMenu(self.menu)
            self.menu.Destroy()



    def SetMenuValue(self,event):
        s = self.menu.GetLabelText(event.GetId())
        h = self.ctrl0.currentCol

        self.ctrl0.SetStringItem(self.ctrl0.currentItem,h,s)











#### --- Элемент со списком  ----
class List(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin,listmix.TextEditMixin,listmix.CheckListCtrlMixin):

    def __init__(self, parent, ID, pos=(0,0), size=(1200,350), style=wx.LC_REPORT|wx.LC_HRULES|wx.LC_VRULES):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

        #listmix.ListCtrlAutoWidthMixin.__init__(self)
        #listmix.CheckListCtrlMixin.__init__(self)

        self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnBeginLabelEdit)
        self.Bind(wx.EVT_LIST_COL_CLICK, self.OnSelected)

        self.InsertColumn(0,u"")
        self.InsertColumn(1,u"1")
        self.InsertColumn(2,u"2")
        self.InsertColumn(3,u"3")
        self.InsertColumn(4,u"4")
        self.InsertColumn(5,u"5")
        self.InsertColumn(6,u"6")
        self.InsertColumn(7,u"7")
        self.InsertColumn(8,u"")

        self.SetColumnWidth(0, 100)
        self.SetColumnWidth(1, 145)
        self.SetColumnWidth(2, 145)
        self.SetColumnWidth(3, 145)
        self.SetColumnWidth(4, 145)
        self.SetColumnWidth(5, 145)
        self.SetColumnWidth(6, 145)
        self.SetColumnWidth(7, 145)
        self.SetColumnWidth(8, 10)





    #### --- Отображение списка ---
    def Populate(self):
        self.DeleteAllItems()

        #### --- Массив идентификаторов строк ---
        self.kod_record = []

        client = ModbusClient(method='rtu', port='%s' % dev, baudrate='115200', timeout=1)
        client.connect()


        client.close()


        title = [
            u'Режим',
            u'Время,сек',
            u'Раздел 1',
            u'Раздел 2',
            u'Раздел 3',
            u'Раздел 4',
            u'Раздел 5',
            u'Раздел 6',
            u'Раздел 7',
        ]


        ### --- Получение списка ---
        for row in  range(0,9):
            index = self.InsertStringItem(sys.maxint, "")

            #### --- Заполнение массива идентификаторов строк ---
            self.kod_record.append(row)
            self.SetStringItem(index, 0, "%s" % title[row])

        #### --- текущая первая строка ---
        self.currentItem=0


        listmix.TextEditMixin.__init__(self)
        listmix.CheckListCtrlMixin.__init__(self)



    def OnBeginLabelEdit(self, event):
        if event.m_col == 0 or self.currentItem != 1:
            event.Veto()
        else:
            event.Skip()



    def OnSelected(self,event):
        print event.m_col,event.m_itemIndex

