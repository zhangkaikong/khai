#coding:utf-8
import wx
class WindowLocation(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,None,-1,title = title,size=(250,250))
        panel = wx.Panel(self,-1)
        panel.Bind(wx.EVT_MOTION,self.OnTouch)
        wx.StaticText(panel,-1,'Pos:',(10,15))
        self.posCtrl = wx.TextCtrl(panel,-1,'',pos=(40,10))

    def OnTouch(self,event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" % (pos.x, pos.y))
        pass

app = wx.App()
windowLocation = WindowLocation('Location')
windowLocation.Show()
app.MainLoop()