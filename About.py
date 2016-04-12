#coding:utf-8


""" Диалог о программе """

import	wx
import	wx.html
from wx.lib.wordwrap import wordwrap



class Info(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1)

	info = wx.AboutDialogInfo()
	info.Name = "Officer+"
	info.Version = "0.9"
	info.Copyright = "(C) 2016 ГПБ Ураган"
	info.Description = wordwrap(
		"A \"hello world\" program is a software program that prints out "
		"\"Hello world!\" on a display device. It is used in many introductory "
		"tutorials for teaching a programming language."

		"\n\nSuch a program is typically one of the simplest programs possible "
		"in a computer language. A \"hello world\" program can be a useful "
		"sanity test to make sure that a language's compiler, development "
		"environment, and run-time environment are correctly installed.",
		350, wx.ClientDC(self))
	info.WebSite = ("http://www.officer24.ru", "Officer")
	info.Developers = [ "Vladimir Komarov",
						"Roman Tayursky",
						"Anatoly Zamyatin" ]

	wx.AboutBox(info)







