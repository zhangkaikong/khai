# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import pygame
###########################################################################
## Class MyDialog2
###########################################################################

class MyDialog2(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(336, 667), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        exSizer12 = wx.BoxSizer(wx.VERTICAL)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer13 = wx.BoxSizer(wx.VERTICAL)

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.title = wx.StaticText(self, wx.ID_ANY, u"青花瓷", wx.DefaultPosition, wx.DefaultSize, 0)
        self.title.Wrap(-1)
        bSizer9.Add(self.title, 1, wx.ALL | wx.EXPAND, 5)

        self.singer = wx.StaticText(self, wx.ID_ANY, u"周杰伦", wx.DefaultPosition, wx.DefaultSize, 0)
        self.singer.Wrap(-1)
        bSizer9.Add(self.singer, 1, wx.ALL | wx.EXPAND, 5)

        bSizer13.Add(bSizer9, 7, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.previewButton = wx.Button(self, wx.ID_ANY, u"上一曲", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.previewButton, 1, wx.ALL, 5)

        self.playPauseButton = wx.Button(self, wx.ID_ANY, u"播放", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.playPauseButton, 1, wx.ALL, 5)

        self.nextButton = wx.Button(self, wx.ID_ANY, u"下一曲", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer10.Add(self.nextButton, 1, wx.ALL, 5)

        bSizer13.Add(bSizer10, 5, wx.EXPAND, 5)

        bSizer7.Add(bSizer13, 3, wx.EXPAND, 5)

        bSizer8 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticline7 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 100), wx.LI_VERTICAL)
        bSizer8.Add(self.m_staticline7, 0, wx.EXPAND | wx.ALL, 5)

        self.volumeBar = wx.Slider(self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size(-1, 100),
                                   wx.SL_INVERSE | wx.SL_VERTICAL)
        bSizer8.Add(self.volumeBar, 0, wx.ALL | wx.EXPAND, 5)

        bSizer7.Add(bSizer8, 1, wx.ALL | wx.EXPAND, 5)

        exSizer12.Add(bSizer7, 5, wx.EXPAND, 5)

        bSizer6.Add(exSizer12, 2, wx.EXPAND, 5)

        exSizer11 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline5 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        exSizer11.Add(self.m_staticline5, 0, wx.EXPAND | wx.ALL, 5)

        self.showTime = wx.StaticText(self, wx.ID_ANY,
                                      u"00:00                                                        12:00",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.showTime.Wrap(-1)
        exSizer11.Add(self.showTime, 0, wx.ALL | wx.EXPAND, 5)

        self.progressBar = wx.Slider(self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        exSizer11.Add(self.progressBar, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(exSizer11, 2, wx.EXPAND, 5)

        exSizer15 = wx.BoxSizer(wx.VERTICAL)

        self.dirPicker = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition,
                                          wx.DefaultSize, wx.DIRP_DIR_MUST_EXIST )
        exSizer15.Add(self.dirPicker, 0, wx.ALL | wx.EXPAND, 5)

        bSizer6.Add(exSizer15, 1, wx.EXPAND, 5)

        exSizer14 = wx.BoxSizer(wx.VERTICAL)

        self.musicListView = wx.ListCtrl(self, -1, size=(220, 250), style=wx.LC_REPORT)
        self.musicListView.InsertColumn(0, '歌曲列表')
        self.musicListView.SetColumnWidth(0, 330)
        exSizer14.Add(self.musicListView, 4, wx.EXPAND | wx.ALL, 5)

        bSizer6.Add(exSizer14, 6, wx.EXPAND, 5)

        self.SetSizer(bSizer6)
        self.Layout()

        self.Centre(wx.BOTH)
        self.InitPlayList()
        self.AddSongsIntoList()

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.MyDialog2OnClose)
        self.previewButton.Bind(wx.EVT_BUTTON, self.previewButtonOnButtonClick)
        self.playPauseButton.Bind(wx.EVT_BUTTON, self.playPauseButtonOnButtonClick)
        self.nextButton.Bind(wx.EVT_BUTTON, self.nextButtonOnButtonClick)
        self.volumeBar.Bind(wx.EVT_COMMAND_SCROLL, self.volumeBarOnCommandScroll)
        self.volumeBar.Bind(wx.EVT_COMMAND_SCROLL_CHANGED, self.volumeBarOnCommandScrollChanged)
        self.volumeBar.Bind(wx.EVT_SCROLL_CHANGED, self.volumeBarOnScrollChanged)
        self.progressBar.Bind(wx.EVT_COMMAND_SCROLL, self.progressBarOnCommandScroll)
        self.progressBar.Bind(wx.EVT_COMMAND_SCROLL_CHANGED, self.progressBarOnCommandScrollChanged)
        self.progressBar.Bind(wx.EVT_SCROLL_CHANGED, self.progressBarOnScrollChanged)
        self.progressBar.Bind(wx.EVT_SET_FOCUS, self.progressBarOnSetFocus)
        self.dirPicker.Bind(wx.EVT_DIRPICKER_CHANGED, self.dirPickerOnDirChanged)
        self.dirPicker.Bind(wx.EVT_ENTER_WINDOW, self.dirPickerOnEnterWindow)
        self.dirPicker.Bind(wx.EVT_LEAVE_WINDOW, self.dirPickerOnLeaveWindow)
        self.dirPicker.Bind(wx.EVT_LEFT_DCLICK, self.dirPickerOnLeftDClick)
        self.dirPicker.Bind(wx.EVT_LEFT_DOWN, self.dirPickerOnLeftDown)
        self.musicListView.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.musicListViewOnListItemActivated)
        self.musicListView.Bind(wx.EVT_LIST_ITEM_FOCUSED, self.musicListViewOnListItemFocused)
        self.musicListView.Bind(wx.EVT_LIST_ITEM_SELECTED, self.musicListViewOnListItemSelected)
        self.i = 0
        self.isMusicActive = False
        self.musicpath = ''

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def MyDialog2OnClose(self, event):
        event.Skip()

    def previewButtonOnButtonClick(self, event):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        if self.i == 0:
            self.i == 0
        else:
            self.i = self.i-1
        pygame.mixer.music.load(self.musics[self.i])
        pygame.mixer.music.play(1)
        self.title.SetLabel(self.GetSongTitle())
        print '上一曲'

    def playPauseButtonOnButtonClick(self, event):
        print self.progressBar.GetValue()
        if self.isMusicActive:
            print '1'
            if self.playPauseButton.GetLabel() == u'暂停':
                pygame.mixer.music.pause()
                self.playPauseButton.SetLabel(u'播放')
            elif self.playPauseButton.GetLabel() == u'播放':
                pygame.mixer.music.unpause()
                self.playPauseButton.SetLabel(u'暂停')
        else:
            print '2'
            pygame.mixer.init()
            pygame.mixer.music.load(self.musics[self.i])
            pygame.mixer.music.play(1)
            self.playPauseButton.SetLabel(u'暂停')
            self.isMusicActive = True

    def nextButtonOnButtonClick(self, event):
        print '下一曲'
        if pygame.mixer.music.get_busy():
            if self.i == len(self.musics) - 1:
                self.i = len(self.musics) - 1
            else:
                self.i += 1
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.musics[self.i])
        print self.i
        pygame.mixer.music.play(1)
        print '下一曲'
        self.title.SetLabel(self.GetSongTitle())

    def volumeBarOnCommandScroll(self, event):
        event.Skip()

    def volumeBarOnCommandScrollChanged(self, event):
        event.Skip()

    def volumeBarOnScrollChanged(self, event):
        self.volume = self.volumeBar.GetValue()
        pygame.mixer.music.set_volume(self.volume/100.0)
        print pygame.mixer.music.get_volume()
        print self.volume
        print 'volume change'

    def progressBarOnCommandScroll(self, event):
        event.Skip()

    def progressBarOnCommandScrollChanged(self, event):
        event.Skip()

    def progressBarOnScrollChanged(self, event):
        pygame.mixer.music.play(1,)

    def progressBarOnSetFocus(self, event):

        print event

    def dirPickerOnDirChanged(self, event):
        self.musicpath = self.dirPicker.GetPath()
        print '目录切换'

    def dirPickerOnEnterWindow(self, event):
        print '.....'

    def dirPickerOnLeaveWindow(self, event):
        print 'likai'

    def dirPickerOnLeftDClick(self, event):
        print '右边点击'

    def dirPickerOnLeftDown(self, event):
        print 'zuoji'

    def musicListViewOnListItemActivated(self, event):
        item = event.GetIndex()
        self.i = item
        pygame.mixer.init()
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.musics[item])
            pygame.mixer.music.play(1)

        total = len(self.musics)
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.musics[item])
            pygame.mixer.music.play(1)
        #Update the title of the song
        self.title.SetLabel(self.GetSongTitle())
        self.isMusicActive = True
        self.playPauseButton.SetLabel(u'暂停')

    def musicListViewOnListItemFocused(self, event):
        event.Skip()

    def musicListViewOnListItemSelected(self, event):
        print 'heheh'


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
            self.musicListView.InsertStringItem(self.i,music)
            self.i += 1

    def GetSongTitle(self):
        strings = self.musics[self.i].split("/")
        return strings[len(strings) - 1]


app = wx.App()
musicplayer =  MyDialog2(None)
musicplayer.Show()
app.MainLoop()