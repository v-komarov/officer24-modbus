#coding:utf-8

import  wx
import usb
import sys
import shelve
import commands



CFG_FILE = 'cfg.data'



#### --- Список USB ---
class ListUsb(wx.Dialog):
    def __init__(
            self, parent, ID, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE
            ):


        pre = wx.PreDialog()
        pre.Create(parent, ID, title, pos, size, style)

        self.PostCreate(pre)

        tID = wx.NewId()


#### --- Заголовок ---
        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, -1, u"COM порты")
        label.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        sizer.Add(label, 0, wx.ALIGN_LEFT|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)
        self.ctrl0 = List(pre, tID, style=wx.LC_REPORT|wx.LC_SORT_ASCENDING)
        box.Add(self.ctrl0, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20,-1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.RIGHT|wx.TOP, 5)



#### --- Кнопки ---
        btn = wx.Button(self, wx.ID_FIND)
        btn1 = wx.Button(self, wx.ID_SAVE)
        btn2 = wx.Button(self, wx.ID_CLOSE)

        box = wx.BoxSizer(wx.HORIZONTAL)
        box.Add(btn, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn1, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        box.Add(btn2, 1, wx.ALIGN_CENTRE|wx.ALL, 5)
        sizer.Add(box, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

        self.Bind(wx.EVT_BUTTON, self.Find, btn)
        self.Bind(wx.EVT_BUTTON, self.Save, btn1)
        self.Bind(wx.EVT_BUTTON, self.Cancel, btn2)
        self.ctrl0.Bind(wx.EVT_LIST_ITEM_SELECTED, self.ReadItem, self.ctrl0)






    ### --- Кнопка Cancel ----
    def Cancel(self,event):
        self.Destroy()



    def Find(self, event):
        self.ctrl0.Populate()
        self.ctrl0.SetItemState(0, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


    #### --- Присвоение значение по выбранной строке ----
    def ReadItem(self,event):
        self.ctrl0.currentItem = event.m_itemIndex



    def Save(self, event):
        dev = self.ctrl0.GetItem(self.ctrl0.currentItem,0).GetText()
        db = shelve.open(CFG_FILE)
        db['dev'] = dev
        db.close()

        self.Destroy()




#### --- Элемент со списком  ----
class List(wx.ListCtrl):

    def __init__(self, parent, ID, pos=(0,0), size=(450,350), style=0):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)

        self.InsertColumn(0,u"DEV")

        self.SetColumnWidth(0, 450)


    #### --- Отображение списка ---
    def Populate(self):
        self.DeleteAllItems()

        #### --- Массив идентификаторов строк ---
        self.kod_record = []

	    ### --- Получение списка ---
        for row in  DevUsb():
            index = self.InsertStringItem(sys.maxint, "")
            self.SetStringItem(index, 0, row)



	    #### --- Заполнение массива идентификаторов строк ---
	    self.kod_record.append(row)

        #### --- текущая первая строка ---
        self.currentItem=0





def DevUsb():

    data = commands.getoutput('python -m serial.tools.list_ports').split()[:-3]

#    for dev in usb.core.find(find_all=True):
        #print " idVendor: %d (%s)" % (dev.idVendor, hex(dev.idVendor))
        #print
# " idProduct: %d (%s)" % (dev.idProduct, hex(dev.idProduct))
#        d = {}
#        d['dev'] = '%s' % dev.idVendor
#        data.append(d)


    return data



