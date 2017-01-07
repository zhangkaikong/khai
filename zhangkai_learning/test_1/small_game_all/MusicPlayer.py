#coding:utf-8
import wx
import os
import pygame
import random
import wx.lib.mixins.listctrl  as  listmix

class PlayerInterface(wx.Frame):
    def __init__(self,title):
        super(PlayerInterface,self).__init__(None,title=title,size=(250,250))
        self.InitUI()
        self.Centre()

    #Init the window of the music player
    def InitUI(self):
        #place a button
        panel = wx.Panel(self)
        panel.SetBackgroundColour('Yellow')
        self.song_title = wx.StaticText(panel,-1,size=wx.DefaultSize,style=wx.TE_CENTER,label='青花瓷')
        self.InitButton(panel)

    #Init the buttons on the panel
    def InitButton(self,panel):
        self.buttonPlay = wx.Button(parent=panel,label='播放',pos=(80,40))
        self.buttonPause = wx.Button(parent=panel,label='暂停',pos=(80,80))
        self.buttonStop = wx.Button(parent=panel,label='停止',pos=(80,120))
        self.Bind(wx.EVT_BUTTON,self.OnPlay,self.buttonPlay)
        self.Bind(wx.EVT_BUTTON, self.OnPause, self.buttonPause)
        self.Bind(wx.EVT_BUTTON, self.OnStop, self.buttonStop)

    #some control methods
    def OnPlay(self,event):
        musics = self.InitPlaylist()
        for music in musics:
            print music
        pygame.mixer.init()
        total = len(musics)
        if not pygame.mixer.music.get_busy():
            playMusic = random.choice(musics)
            pygame.mixer.music.load(playMusic)
            pygame.mixer.music.play(1)

    def OnPause(self,event):
        self.song_title.SetLabel('暂停中...')

    def OnStop(self,event):
        self.song_title.SetLabel('已停止...')

    #Init the playlist
    def InitPlaylist(self):
        folder = r'/home/zhangkai/Music/'
        musics = [folder+music for music in os.listdir(folder) if music.endswith('.mp3')]
        return musics

class TestListCtrl(wx.ListCtrl,listmix.ListCtrlAutoWidthMixin):
    def __init__(self, parent, ID, pos=wx.DefaultPosition,
                 size=wx.DefaultSize, style=wx.LC_REPORT | wx.LC_NO_HEADER | wx.LC_HRULES):
        wx.ListCtrl.__init__(self, parent, ID, pos, size, style)
        listmix.ListCtrlAutoWidthMixin.__init__(self)

    def initListCtrlData(self,musics):
        pass


#Start the music player
app = wx.App()
player = PlayerInterface('MusicPlayer')
player.Show()
app.MainLoop()
