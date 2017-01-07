import wx
import wx.lib.mixins.listctrl  as  listmix

class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):

    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.LC_REPORT | wx.LC_NO_HEADER | wx.LC_HRULES):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

class ShowPanel(wx.Panel):
    def __init__(self, parent, id, musiclist):
        wx.Panel.__init__(self, parent, id, size=(380, 600),style=wx.SUNKEN_BORDER)
        self.curIndex = 0
        self.preIndex = 0
        self.nextIndex = 0
        self.itemcount = 0
        self.initListCtrl()
        self.initListCtrlData(musiclist)
        self.bindEvents()
        self.lastindex = -1

    def initListCtrl(self):
        self.playlist = TestListCtrl(self, wx.NewId(), size=(100, 600))
        self.playlist.InsertColumn(0, 'test', width=100)
        self.playlist.InsertStringItem(0, u'默认')

        self.musiclist = TestListCtrl(self, wx.NewId(), pos=(100, 0), size=(270, 600))
        self.musiclist.InsertColumn(0, 'test', width=270)
