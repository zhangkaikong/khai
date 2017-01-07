# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.animate
import os

class MusicPalyer(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(328, 538), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        AllInIt = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"青花瓷", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        AllInIt.Add(self.m_staticText1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_slider1 = wx.Slider(self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        AllInIt.Add(self.m_slider1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_animCtrl1 = wx.animate.AnimationCtrl(self, wx.ID_ANY, wx.animate.NullAnimation, wx.DefaultPosition,
                                                    wx.DefaultSize, wx.animate.AC_DEFAULT_STYLE)

        self.m_animCtrl1.SetInactiveBitmap(
            wx.Bitmap(u"/home/zhangkai/Pictures/专业测试用图/100张图片/SW2s_1183292368.bmp", wx.BITMAP_TYPE_ANY))
        AllInIt.Add(self.m_animCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        self.listView = wx.ListCtrl(self, -1, size=(200,330),style = wx.LC_REPORT)
        self.listView.InsertColumn(0, '朕的歌曲列表')
        self.listView.SetColumnWidth(0, 330)
        AllInIt.Add(self.listView, 0, wx.EXPAND | wx.ALL , 5)

        self.SetSizer(AllInIt)
        self.Layout()

        self.Centre(wx.BOTH)
        self.InitPlayList()
        self.AddSongsIntoList()


    def __del__(self):
        pass


    def InitPlayList(self):
        folder = r'/home/zhangkai/Music/'
        self.musics = [folder+music for music in os.listdir(folder) if music.endswith('.mp3')]

    def AddSongsIntoList(self):
        self.i = 1
        for music in self.musics:
            strings = music.split("/")
            music = strings[len(strings) - 1]
            self.listView.InsertStringItem(self.i,music)
            self.i += 1


app = wx.App()
myFrame = MusicPalyer(None)
myFrame.Show()
app.MainLoop()