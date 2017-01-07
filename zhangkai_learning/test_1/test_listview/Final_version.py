# -*- coding: utf-8 -*-
import wx
import wx.xrc
import os
import pygame

class MyDialog(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                           size=wx.Size(317, 616), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        Sizer1 = wx.BoxSizer(wx.VERTICAL)

        Sizer2 = wx.BoxSizer(wx.VERTICAL)

        self.songTitle = wx.StaticText(self, wx.ID_ANY, u"周杰伦-青花瓷", wx.DefaultPosition, wx.DefaultSize, 0)
        self.songTitle.Wrap(-1)
        Sizer2.Add(self.songTitle, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        Sizer2.Add(self.m_staticline1, 0, wx.EXPAND | wx.ALL, 5)

        self.timeShow = wx.StaticText(self, wx.ID_ANY,
                                      u"00:00                                                     12:00",
                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.timeShow.Wrap(-1)
        Sizer2.Add(self.timeShow, 0, wx.ALL | wx.EXPAND, 5)

        self.progressBar = wx.Slider(self, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL)
        Sizer2.Add(self.progressBar, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, 15), wx.LI_HORIZONTAL)
        Sizer2.Add(self.m_staticline3, 0, wx.EXPAND | wx.ALL, 5)

        Sizer1.Add(Sizer2, 1, wx.EXPAND, 5)

        Sizer3 = wx.BoxSizer(wx.VERTICAL)

        Sizer4 = wx.BoxSizer(wx.HORIZONTAL)

        self.previewButton = wx.Button(self, wx.ID_ANY, u"上一曲", wx.DefaultPosition, wx.DefaultSize, 0)
        self.playPauseButton = wx.Button(self, wx.ID_ANY, u"播放", wx.DefaultPosition, wx.DefaultSize, 0)
        self.nextButton = wx.Button(self, wx.ID_ANY, u"下一曲", wx.DefaultPosition, wx.DefaultSize, 0)

        Sizer4.Add(self.previewButton, 1, wx.ALL, 5)
        Sizer4.Add(self.playPauseButton, 1, wx.ALL, 5)
        Sizer4.Add(self.nextButton, 1, wx.ALL, 5)

        Sizer3.Add(Sizer4, 1, wx.EXPAND, 5)

        Sizer5 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL)
        Sizer5.Add(self.m_staticline2, 0, wx.EXPAND | wx.ALL, 5)

        self.album_show = wx.StaticBitmap(self, wx.ID_ANY,
                                          wx.Bitmap(u"/home/zhangkai/Pictures/qq.jpg", wx.BITMAP_TYPE_ANY),
                                          wx.DefaultPosition, wx.Size(-1, 60), 0)
        Sizer5.Add(self.album_show, 0, wx.ALL | wx.EXPAND, 5)

        self.music_dir_select = wx.DirPickerCtrl(self, wx.ID_ANY, wx.EmptyString, u"Select a folder",
                                                 wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE)
        Sizer5.Add(self.music_dir_select, 0, wx.ALL | wx.EXPAND, 5)

        self.listView = wx.ListCtrl(self, -1, size=(200,430), style=wx.LC_REPORT)
        self.listView.InsertColumn(0, '朕的歌曲列表')
        self.listView.SetColumnWidth(0, 330)
        Sizer5.Add(self.listView, 0, wx.ALL | wx.EXPAND, 5)

        Sizer3.Add(Sizer5, 13, wx.EXPAND, 5)

        Sizer1.Add(Sizer3, 13, wx.EXPAND, 5)

        self.SetSizer(Sizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.InitPlayList()
        self.AddSongsIntoList()

        # Connect Events
        self.progressBar.Bind(wx.EVT_SCROLL, self.progressBarOnScroll)
        self.progressBar.Bind(wx.EVT_SCROLL_CHANGED, self.progressBarOnScrollChanged)
        self.previewButton.Bind(wx.EVT_BUTTON, self.previewButtonOnKeyDown)
        self.playPauseButton.Bind(wx.EVT_BUTTON, self.playPauseButtonOnKeyDown)
        self.nextButton.Bind(wx.EVT_BUTTON, self.nextButtonOnKeyDown)
        self.music_dir_select.Bind(wx.EVT_DIRPICKER_CHANGED, self.music_dir_selectOnDirChanged)
        self.listView.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.listViewOnListItemActivated)
        self.listView.Bind(wx.EVT_LIST_ITEM_SELECTED, self.listViewOnListItemSelected)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def progressBarOnScroll(self, event):
        print '进度更新...。。。。'
        print event.Get

    def progressBarOnScrollChanged(self, event):
        print '进度更新...'

    def previewButtonOnKeyDown(self, event):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        if self.i == 0:
            self.i == 0
        else:
            self.i = self.i-1
        pygame.mixer.music.load(self.musics[self.i])
        pygame.mixer.music.play(1)
        self.songTitle.SetLabel(self.GetSongTitle())
        print '上一曲'

    def playPauseButtonOnKeyDown(self, event):
        print '暂停/播放'

    def nextButtonOnKeyDown(self, event):
        print '下一曲'
        if pygame.mixer.music.get_busy():
            if self.i == len(self.musics)-1:
                self.i = len(self.musics)-1
            else:
                self.i +=1
        pygame.mixer.music.stop()
        pygame.mixer.music.load(self.musics[self.i])
        print self.i
        pygame.mixer.music.play(1)
        print '下一曲'
        self.songTitle.SetLabel(self.GetSongTitle())

    def music_dir_selectOnDirChanged(self, event):
        print '目录切换...'

    def listViewOnListItemActivated(self, event):
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
        self.songTitle.SetLabel(self.GetSongTitle())
        print 'Item点击'

    def listViewOnListItemSelected(self, event):
        print 'Item选择'



    def InitPlayList(self):
        folder = r'/home/zhangkai/Music/'
        self.musics = [folder+music for music in os.listdir(folder) if music.endswith('.mp3')]

    def AddSongsIntoList(self):
        self.i = 1
        for music in self.musics:
            strings = music.split("/")
            music = strings[len(strings) - 1]
            self.title = music
            self.listView.InsertStringItem(self.i,music)
            self.i += 1

    def GetSongTitle(self):
        strings = self.musics[self.i].split("/")
        return strings[len(strings) - 1]


app = wx.App()
musicPlayer = MyDialog(None)
musicPlayer.Show()
app.MainLoop()