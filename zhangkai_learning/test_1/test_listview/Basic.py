import wx
import completedialog

app = wx.App()
image = wx.Image('/home/zhangkai/Pictures/image009.jpg', wx.BITMAP_TYPE_JPEG)
dialog = completedialog.MyDialog(image)
dialog.Show()
app.MainLoop()
