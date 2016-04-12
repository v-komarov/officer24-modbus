#!/usr/bin/env python
#coding:utf-8

import	wx
import	shelve
import	mainwin



CFG_FILE = 'ps.cfg'



if __name__ == '__main__':
    class MyApp(wx.App):
        def OnInit(self):
            MainFrame = mainwin.MyParentFrame()
            MainFrame.Show(True)
            self.SetTopWindow(MainFrame)
            return True


    app = MyApp(False)
    app.MainLoop()


#    file = shelve.open(CFG_FILE)
#    file['dbpasswd'] = ''
#    file.close()
