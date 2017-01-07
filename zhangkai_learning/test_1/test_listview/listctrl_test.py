# coding:utf-8
import wx
import os
import pygame
import random

class MusicDialog(wx.Dialog):
    def __init__(self, parent, id, title):
        wx.Dialog.__init__(self, parent, id, title, size=(800, 500), style=wx.DEFAULT_DIALOG_STYLE)
        self.InitWindow()
        self.i = 0

    def InitWindow(self):
        boxSizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        boxSizer_3 = wx.BoxSizer(wx.VERTICAL)

        buttonPrev = wx.Button(self, 10,'上一曲')
        buttonPlay = wx.Button(self, 10, '播放')
        buttonPause = wx.Button(self, 10, '暂停')
        buttonStop = wx.Button(self, 10, '停止')
        buttonNext = wx.Button(self, 10, '下一曲')
        self.Bind(wx.EVT_BUTTON,self.OnPrev,buttonPrev)
        self.Bind(wx.EVT_BUTTON, self.OnPlay, buttonPlay)
        self.Bind(wx.EVT_BUTTON, self.OnPause, buttonPause)
        self.Bind(wx.EVT_BUTTON, self.OnStop, buttonStop)
        self.Bind(wx.EVT_BUTTON, self.OnNext, buttonNext)


        boxSizer_2.Add(buttonPrev, 1, wx.ALL, 3)
        boxSizer_2.Add(buttonPlay, 1,  wx.ALL, 3)
        boxSizer_2.Add(buttonPause, 1, wx.ALL, 3)
        boxSizer_2.Add(buttonStop, 1, wx.ALL, 3)
        boxSizer_2.Add(buttonNext, 1, wx.ALL, 3)

        boxSizer_1.Add(boxSizer_2, -1, wx.EXPAND)
        boxSizer_1.Add(boxSizer_3, -1, wx.EXPAND)


        self.lc = wx.ListCtrl(self, -1, style=wx.LC_REPORT)
        self.lc.InsertColumn(0, '朕的歌曲列表')
        self.lc.SetColumnWidth(0, 300)
        self.InitPlayList()
        self.AddSongsIntoList()
        self.lc.Bind(wx.EVT_LIST_ITEM_ACTIVATED,self.OnItemClick,self.lc)

        boxSizer_3.Add(self.lc,1,wx.EXPAND | wx.ALL, 3)

        self.SetSizer(boxSizer_1)

    def OnItemClick(self,event):
        item = event.GetIndex()
        self.i = item
        pygame.mixer.init()
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            pygame.mixer.music.load(self.musics[item])
            pygame.mixer.music.play(1)

        total = len(self.musics)
        if not pygame.mixer.music.get_busy():
            # playMusic = random.choice(musics)
            pygame.mixer.music.load(self.musics[item])
            pygame.mixer.music.play(1)
        print item


    def InitPlayList(self):
        folder = r'/home/zhangkai/Music/'
        self.musics = [folder+music for music in os.listdir(folder) if music.endswith('.mp3')]

    def AddSongsIntoList(self):
        self.i = 1
        for music in self.musics:
            strings = music.split("/")
            music = strings[len(strings) - 1]
            self.lc.InsertStringItem(self.i,music)
            self.i += 1

    def OnPrev(self,event):
        print '上一首！'
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        if self.i == 0:
            self.i == 0
        else:
            self.i = self.i-1
        pygame.mixer.music.load(self.musics[self.i])
        pygame.mixer.music.play(1)

    def OnPlay(self,event):
        print '播放'

    def OnPause(self,event):
        print '暂停'

    def OnStop(self,event):
        print '停止'

    def OnNext(self,event):
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

app = wx.App()
musicDialog = MusicDialog(None, -1, title='MusicPlayer')
musicDialog.Show()
app.MainLoop()
