#coding:utf-8
import wx

app = wx.App()
window = wx.Frame(None,title='MyWindow',size=(300,300))
panel = wx.Panel(window)
wx.StaticText(panel,label='老王,尼玛！',pos=(100,100))
window.Show()
app.MainLoop()