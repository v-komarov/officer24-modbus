#coding:utf-8


""" Диалог о программе """

import	wx
import	wx.html
from wx.lib.wordwrap import wordwrap




def Info(self):

	info = wx.AboutDialogInfo()
	info.Name = u"Утилита программирования\nППКОП \"Офицер\" 04"
	info.Version = u"0.5"
	info.Copyright = u"(C) 2016 ГПБ Ураган"
	info.Description = wordwrap(
		u"Основное назначение:\n"
		u"Программирование панели по протоколу modbus."

		u"\n\nИспользуемые библиотеки:\n"
		u"wxPython(ver 3.0.2.0)\n"
		u"Twisted(ver 16.0.0)\n"
		u"pymodbus(ver 1.2.0)\n"
		u"pyserial(ver 2.7)\n"
		u"zope.interface(ver 4.1.2)\n"
		u"",
		350, wx.ClientDC(self))
	info.WebSite = (u"http://www.officer24.ru", u"Officer")
	info.Developers = [ u"Vladimir Komarov",
						u"Roman Tayursky",
						u"Anatoly Zamyatin" ]

	wx.AboutBox(info)







