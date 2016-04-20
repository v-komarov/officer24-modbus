#coding:utf-8


import	wx
import  shelve
import sys
import  wx.lib.mixins.listctrl  as  listmix

from    tools import Read2bytes,StrRevers,Write16key


from pymodbus.client.sync import ModbusSerialClient as ModbusClient


CFG_FILE = 'cfg.data'






class Keys(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Ключи")


        db = shelve.open(CFG_FILE)
        self.dev = db['dev']
        db.close()



        self.btn = wx.Button(self, wx.ID_REFRESH)
        self.btn1 = wx.Button(self, wx.ID_SAVE)
        self.btn2 = wx.Button(self,-1, u"Считать ключ")


        sizer = wx.BoxSizer(wx.VERTICAL)


        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl0 = List(self, -1, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
        sizer_1.Add(self.ctrl0,0)

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
        self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)
        self.ctrl0.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.ShowMenu, self.ctrl0)



    def Read(self, evt):

        self.ctrl0.Populate()
        self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


    def Write(self,event):
        data_key = []
        data_part = []
        for y in range(0,128):
            item = self.ctrl0.GetItem(y,1)
            data_key.extend(Write16key(item.GetText()))
            item2 = self.ctrl0.GetItem(y,2)
            data_part.append(int(item2.GetText()))


        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)
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



    #### --- Присвоение значение по выбранной строке ----
    def ReadItem(self,event):
        self.ctrl0.currentItem = event.m_itemIndex



    def	ShowMenu(self,event):

        #print event.m_itemIndex
        #print event.m_item.m_col

        self.menu=wx.Menu()
        self.menu.Append(wx.NewId(),"0")
        self.menu.Append(wx.NewId(),"1")
        self.menu.Append(wx.NewId(),"2")
        self.menu.Append(wx.NewId(),"3")
        self.menu.Append(wx.NewId(),"4")
        self.menu.Append(wx.NewId(),"5")
        self.menu.Append(wx.NewId(),"6")
        self.menu.Append(wx.NewId(),"7")
        self.menu.Append(wx.NewId(),"8")


        self.menu.Bind(wx.EVT_MENU, self.SetMenuValue)
        self.PopupMenu(self.menu)
        self.menu.Destroy()



    def SetMenuValue(self,event):
        v = self.menu.GetLabelText(event.GetId())
        self.ctrl0.SetStringItem(self.ctrl0.currentItem,2,v)




    def ReadKey(self,event):
        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)

        rr = client.read_holding_registers(address=2064,count=4,unit=1)
        result = rr.registers
        client.close()

        result = "%s%s%s%s" % (Read2bytes(result[0]),Read2bytes(result[1]),Read2bytes(result[2]),Read2bytes(result[3]))

        self.ctrl0.SetStringItem(self.ctrl0.currentItem,1,StrRevers(result))








#### --- Элемент со списком  ----
class List(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin,listmix.TextEditMixin):

    def __init__(self, parent, ID, pos=(0,0), size=(550,550), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

        listmix.ListCtrlAutoWidthMixin.__init__(self)

        self.Bind(wx.EVT_LIST_BEGIN_LABEL_EDIT, self.OnBeginLabelEdit)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.OnCheck)


        self.InsertColumn(0,u"№")
        self.InsertColumn(1,u"Ключ")
        self.InsertColumn(2,u"Раздел")

        self.SetColumnWidth(0, 50)
        self.SetColumnWidth(1, 250)
        self.SetColumnWidth(2, 250)


        db = shelve.open(CFG_FILE)
        self.dev = db['dev']
        db.close()



    #### --- Отображение списка ---
    def Populate(self):
        self.DeleteAllItems()

        #### --- Массив идентификаторов строк ---
        self.kod_record = []

        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)
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






        ### --- Получение списка ---
        for row in  range(1,129):
            index = self.InsertStringItem(sys.maxint, "")
            self.SetStringItem(index, 0, "%s" % row)

            b8 = data_key[0:4]
            del data_key[0:4]

            result = "%s%s%s%s" % (Read2bytes(b8[0]),Read2bytes(b8[1]),Read2bytes(b8[2]),Read2bytes(b8[3]))

            self.SetStringItem(index,1 , StrRevers(result))

            part = data_part[0]
            del data_part[0]

            self.SetStringItem(index,2 , "%s" % (part))


            #### --- Заполнение массива идентификаторов строк ---
            self.kod_record.append(row)



        #### --- текущая первая строка ---
        self.currentItem=0


        listmix.TextEditMixin.__init__(self)




    def OnBeginLabelEdit(self, event):
        if event.m_col == 0 or event.m_col == 2:
            event.Veto()
        else:
            event.Skip()




    def OnCheck(self, event):

        if event.m_col == 1:
            print event.GetLabel()
        elif event.m_col == 2:
            print event.GetLabel()

















class MasterKey(wx.aui.AuiMDIChildFrame):
    def __init__(self, parent):
        wx.aui.AuiMDIChildFrame.__init__(self, parent, -1, title=u"Мастер ключ")


        db = shelve.open(CFG_FILE)
        self.dev = db['dev']
        db.close()



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
        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)

        rr = client.read_holding_registers(address=158,count=4,unit=1)
        result = rr.registers
        client.close()

        result = "%s%s%s%s" % (Read2bytes(result[0]),Read2bytes(result[1]),Read2bytes(result[2]),Read2bytes(result[3]))

        self.text_ctrl_1.SetValue(StrRevers(result))






    def Write(self,event):
        result = self.text_ctrl_1.GetValue()

        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)
        rq=client.write_registers(158,Write16key(result),unit=1)

        client.close()




    def ReadKey(self,event):
        client = ModbusClient(method='rtu', port='%s' % self.dev, baudrate='115200', timeout=1)

        rr = client.read_holding_registers(address=2064,count=4,unit=1)
        result = rr.registers
        client.close()

        result = "%s%s%s%s" % (Read2bytes(result[0]),Read2bytes(result[1]),Read2bytes(result[2]),Read2bytes(result[3]))

        self.text_ctrl_1.SetValue(StrRevers(result))








