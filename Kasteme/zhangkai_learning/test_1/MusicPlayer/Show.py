#!/usr/bin python
# -*-coding:utf-8 -*-

import wx
import wx.lib.mixins.listctrl  as  listmix


class TestListCtrl(wx.ListCtrl, listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.LC_REPORT | wx.LC_NO_HEADER | wx.LC_HRULES):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)


class ShowPanel(wx.Panel):
    def __init__(self, parent, id, musiclist):
        wx.Panel.__init__(self, parent, id, size=(380, 600),
                          style=wx.SUNKEN_BORDER)
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
        # self.musiclist.SetForegroundColour(wx.Colour(0,150,0))

    def initListCtrlData(self, musiclist):
        self.insert2ListCtrl(musiclist)

    def insert2ListCtrl(self, data):
        i = self.itemcount
        for item in data:
            self.musiclist.InsertStringItem(i, str(i + 1) + '.' + item)
            self.itemcount += 1
            i += 1

    def bindEvents(self):
        #        self.musiclist.Bind(wx.EVT_LIST_ITEM_SELECTED,self.OnSelected)
        self.musiclist.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnDoubleClick)
        self.musiclist.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRightClickItem)

    def OnDoubleClick(self, event):
        index = self.musiclist.GetFirstSelected()
        operationpanel = self.GetParent().GetWindow1()
        operationpanel.LoadFileByIndex(index)

    def OnRightClickItem(self, event):
        print 'right click'
        self.createPopMenu()

    def createPopMenu(self):
        if not hasattr(self, "popupDel"):
            self.popupDel = wx.NewId()
            self.Bind(wx.EVT_MENU, self.OnDelItem, id=self.popupDel)

        menu = wx.Menu()
        menu.Append(self.popupDel, 'Delete')
        self.PopupMenu(menu)
        menu.Destroy()

    def OnDelItem(self, event):
        pass

    def setMusicFocus(self, index):
        if self.lastindex != -1:
            self.musiclist.SetItemTextColour(self.lastindex, 'black')
        self.lastindex = index
        self.musiclist.SetItemTextColour(index, 'blue')