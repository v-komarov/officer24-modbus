#coding:utf-8



import wx
import wx.aui

import	About
from    additions   import  Settings
from    checkconnect        import  CheckConnect
from    ethsetting import  EthSetting
from    firezones   import  FireZone1,FireZone2
from    gsmsetting import  GSMSetting
from    outputs     import  OutPuts
from    searchusb import	ListUsb
from    tools import SaveConfig, GetDev, SetDev
from    userskeys   import  Keys,MasterKey
from    zones import Zones

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
ID_MasterKey = wx.NewId()
ID_FireZone1 = wx.NewId()
ID_FireZone2 = wx.NewId()
ID_Additions = wx.NewId()
ID_OutPuts = wx.NewId()
ID_Man = wx.NewId()
ID_Zones = wx.NewId()





#### --- Самое верхнее окно ---

class MyParentFrame(wx.aui.AuiMDIParentFrame):
    def __init__(self):
        wx.aui.AuiMDIParentFrame.__init__(self, None, 1, u"Программирование ППКОП \"Офицер\" 04", size=(1200,800),style=wx.FRAME_NO_WINDOW_MENU | wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.RESIZE_BORDER | wx.CAPTION)


        self.MId=wx.NewId()

        self.winCount = 0


        self.CreateStatusBar(1)

        menu = wx.Menu()


        menu.Append(ID_ScanUSB, u"USB-RS485")
        menu.Append(ID_Man, u"Указать COM порт вручную")
        menu.Append(ID_Connect, u"Проверка связи")
        menu.AppendSeparator()
        menu.Append(ID_SaveConf, u"Запись в ПЗУ")
        menu.AppendSeparator()
        menu.Append(ID_Close, u"Закрыть все")
        menu.AppendSeparator()
        menu.Append(ID_Exit, u"Выход")
        menubar = wx.MenuBar()
        menubar.Append(menu, u"Настройка панели")



        menu2 = wx.Menu()
        menu2.Append(ID_GSM, u"GSM")
        menu2.Append(ID_Eth, u"Ethernet")
        menubar.Append(menu2, u"Сетевые настройки")


        menu3 = wx.Menu()
        menu3.Append(ID_FireZone1, u"Пожарная зона 1")
        menu3.Append(ID_FireZone2, u"Пожарная зона 2")
        menubar.Append(menu3, u"Пожарные зоны")


        menu4 = wx.Menu()
        menu4.Append(ID_Keys, u"Ключи")
        menu4.Append(ID_MasterKey, u"Мастер ключ")
        menubar.Append(menu4, u"Пользователи")


        menu5 = wx.Menu()
        menu5.Append(ID_OutPuts, u"Выходы")
        menu5.Append(ID_Zones, u"Зоны")
        menubar.Append(menu5, u"Основные")


        menu6 = wx.Menu()
        menu6.Append(ID_Additions, u"Дополнительне настройки")
        menu6.AppendSeparator()
        menu6.Append(ID_About, u"О программе")
        menubar.Append(menu6, u"Дополнительно")



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
        self.Bind(wx.EVT_MENU, self.Masterkey, id=ID_MasterKey)
        self.Bind(wx.EVT_MENU, self.FireZ1, id=ID_FireZone1)
        self.Bind(wx.EVT_MENU, self.FireZ2, id=ID_FireZone2)
        self.Bind(wx.EVT_MENU, self.Outputs, id=ID_OutPuts)
        self.Bind(wx.EVT_MENU, self.Setting, id=ID_Additions)
        self.Bind(wx.EVT_MENU, self.Man, id=ID_Man)
        self.Bind(wx.EVT_MENU, self.Mainzones, id=ID_Zones)




	def ShowVidPid(self):

		self.SetStatusText(u'dev: %s' % (GetDev()), 0)

	ShowVidPid(self)






#### --- USB ---
    def SetUsb(self, evt):
		dlg = ListUsb(self,-1,u"Список устройств USB", size=(450,300), style = wx.DEFAULT_DIALOG_STYLE)
		dlg.ShowModal()

		self.SetStatusText(u'dev: %s' % (GetDev()), 0)





#### --- Завершение работы ---
    def OnExit(self, evt):
        for m in self.GetChildren():
            if isinstance(m, wx.aui.AuiMDIClientWindow):
                for k in m.GetChildren():
                    k.Close()


        evt.Skip()

        self.Close(True)




#### --- Закрытие дочерних фреймов в главном окне ---
    def OnClose(self, evt):

        for m in self.GetChildren():
            if isinstance(m, wx.aui.AuiMDIClientWindow):
                for k in m.GetChildren():
                    k.Close()


        evt.Skip()




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



#### Мастер ключ
    def Masterkey(self, evt):
        child = MasterKey(self)
        child.Activate()




#### Пожарная зона 1
    def FireZ1(self, evt):
        child = FireZone1(self)
        child.Activate()




#### Пожарная зона 2
    def FireZ2(self, evt):
        child = FireZone2(self)
        child.Activate()




#### Выходы
    def Outputs(self, evt):
        child = OutPuts(self)
        child.Activate()




#### Зоны
    def Mainzones(self, evt):
        child = Zones(self)
        child.Activate()






#### Дополнительные настройки
    def Setting(self, evt):
        child = Settings(self)
        child.Activate()




#### Указание Com порта вручную
    def Man(self, evt):
        dev = ''
        dlg = wx.TextEntryDialog(self, u'Введите название COM порта ',u'COM1,COM2 или /dev/ttyUSB0 ?', '')
        if dlg.ShowModal() == wx.ID_OK:
            SetDev(dlg.GetValue())

        dlg.Destroy()

        self.SetStatusText(u'dev: %s' % (dev), 0)






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



