#coding:utf-8


import  wx,wx.aui
import	os
import	time
import	shelve



import	About
from	usbtool.searchusb	import	ListUsb
from    gsmeth.gsmsetting   import  GSMSetting
from    gsmeth.ethsetting   import  EthSetting
from    checkconnect        import  CheckConnect
from    tools import SaveConfig
from    userskeys   import  Keys


#----------------------------------------------------------------------
ID_Exit = wx.NewId()
ID_Close = wx.NewId()
ID_About = wx.NewId()
ID_ScanUSB = wx.NewId()
ID_Connect = wx.NewId()
ID_GSM = wx.NewId()
ID_Eth = wx.NewId()
ID_SaveConf = wx.NewId()
ID_Keys = wx.NewId()



### --- Конфигурационный файл ---
CFG_FILE = 'cfg.data'
db = shelve.open(CFG_FILE)
if db.has_key('dev') == False:
	db['dev'] = ''
db.close()






#### --- Самое верхнее окно ---

class MyParentFrame(wx.aui.AuiMDIParentFrame):
    def __init__(self):
        wx.aui.AuiMDIParentFrame.__init__(self, None, 1, u"Программирования панели", size=(1200,800),style=wx.FRAME_NO_WINDOW_MENU)


#class MyParentFrame(wx.MDIParentFrame):
#    def __init__(self):
#        wx.MDIParentFrame.__init__(self, None, 1, u"Программирования панели", size=(1200,800))

    	self.MId=wx.NewId()

        self.winCount = 0


        self.CreateStatusBar(1)

        menu = wx.Menu()


        menu.Append(ID_ScanUSB, u"USB-RS485")
        menu.Append(ID_Connect, u"Проверка связи")
        menu.AppendSeparator()
        menu.Append(ID_SaveConf, u"Запись в ПЗУ")
        menu.AppendSeparator()
	menu.Append(ID_Close, u"Закрыть все")
#	menu.Append(ID_TPList, "Тарифы")
        menu.AppendSeparator()
#	menu.Append(ID_UlList, "Справочник улиц")
#        menu.AppendSeparator()
	menu.Append(ID_Exit, u"Выход")
        menubar = wx.MenuBar()
        menubar.Append(menu, u"Настройка панели")



        menu2 = wx.Menu()
        menu2.Append(ID_GSM, "GSM")
        menu2.Append(ID_Eth, "Ethernet")
        menubar.Append(menu2, u"Сетевые настройки")


        menu3 = wx.Menu()
#        menu3.Append(ID_PL_OUT, "Выгрузить список для \"Платёжки\"")
        menubar.Append(menu3, u"Пожарные зоны")


        menu4 = wx.Menu()
        menu4.Append(ID_Keys, "Ключи")
        menubar.Append(menu4, u"Пользователи")


        menu5 = wx.Menu()
#        menu5.Append(ID_About, "О программе")
        menubar.Append(menu5, u"Основные выхода")


        menu6 = wx.Menu()
#        menu5.Append(ID_About, "О программе")
        menubar.Append(menu6, u"Дополнительные настройки")


        menu7 = wx.Menu()
        menu7.Append(ID_About, u"About")
        menubar.Append(menu7, u"О программе")

	self.SetMenuBar(menubar)



        self.Bind(wx.EVT_MENU, self.OnExit, id=ID_Exit)
        self.Bind(wx.EVT_MENU, self.OnClose, id=ID_Close)
        self.Bind(wx.EVT_MENU, self.Ab, id=ID_About)
        self.Bind(wx.EVT_MENU, self.SetUsb, id=ID_ScanUSB)
        self.Bind(wx.EVT_MENU, self.GSM, id=ID_GSM)
        self.Bind(wx.EVT_MENU, self.Eth, id=ID_Eth)
        self.Bind(wx.EVT_MENU, self.CheckConn, id=ID_Connect)
        self.Bind(wx.EVT_MENU, self.SaveConf, id=ID_SaveConf)
        self.Bind(wx.EVT_MENU, self.UserKeys, id=ID_Keys)





	def ShowVidPid(self):
		db = shelve.open(CFG_FILE)
		dev = db['dev']
		db.close()

		self.SetStatusText(u'dev: %s' % (dev), 0)

	ShowVidPid(self)






#### --- USB ---
    def SetUsb(self, evt):
		dlg = ListUsb(self,-1,u"Список устройств USB", size=(450,300), style = wx.DEFAULT_DIALOG_STYLE)
		dlg.ShowModal()

		db = shelve.open(CFG_FILE)
		dev = db['dev']
		db.close()

		self.SetStatusText(u'dev: %s' % (dev), 0)





#### --- Завершение работы ---
    def OnExit(self, evt):
        self.Close(True)




#### --- Закрытие дочерних фреймов в главном окне ---
    def OnClose(self, evt):

        for m in self.GetChildren():
            if isinstance(m, wx.aui.AuiMDIClientWindow):
                for k in m.GetChildren():
                    k.Close()
                    #if isinstance(k, ChildFrame):

        evt.Skip()


#	win = self.GetActiveChild()
#	if win:
#	    win.Destroy()



    def CheckConn(self,evt):
        CheckConnect(self)



    def SaveConf(self,evt):
        SaveConfig(self)



#### --- Вывод информации "О программе" ---
    def Ab(self,evt):
        About.Info(self)





#### --- GSM ---
    def GSM(self, evt):
        child = GSMSetting(self)
        child.Activate()




#### --- Ethernet ---
    def Eth(self, evt):
        child = EthSetting(self)
        child.Activate()



#### Ключи
    def UserKeys(self, evt):
        child = Keys(self)
        child.Activate()







#----------------------------------------------------------------------

if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            wx.InitAllImageHandlers()
            MainFrame = MyParentFrame()
            MainFrame.Show(True)
            self.SetTopWindow(MainFrame)
            return True


    app = MyApp(False)
    app.MainLoop()



