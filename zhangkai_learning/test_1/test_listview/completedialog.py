import wx
class MyDialog(wx.Frame):
    def __init__(self,image,parent=None,id=-1,title='zhangkai',pos=wx.DefaultPosition):
        temp = image.ConvertToBitmap()
        size = temp.GetWidth(),temp.GetHeight()
        wx.Frame.__init__(self,parent,id,title,pos,size)
        wx.StaticBitmap(parent=self, bitmap=temp)