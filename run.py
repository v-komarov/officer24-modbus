#!/usr/bin/env python
#coding:utf-8

import	wx
import	mainwin





if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            MainFrame = mainwin.MyParentFrame()
            MainFrame.Show(True)
            self.SetTopWindow(MainFrame)
            return True


    app = MyApp(False)
    app.MainLoop()


