# !/usr/bin python
# -*-coding:utf-8 -*-
import wx.media
import os
import ConfigParser
from wx.media import MediaCtrl

wildcard = "mp3 file (*.mp3)|*.mp3|" \
           "wav file (*.wav)|*.wav|" \
           "All file (*.*)|*.*"


class CustomPopupWindow(wx.PopupWindow):
    def __init__(self ,parent ,text='' ,style=wx.BORDER_NONE):
        wx.PopupWindow.__init__(self ,parent ,style)
        self.statictext = wx.StaticText(self ,label=text)

    def SetText(self ,text):
        self.statictext.SetLabel(text)

class OperationPanel(wx.Panel):

    def __init__(self ,parent ,id ,playlist ,musiclist):
        wx.Panel.__init__(self ,parent ,id ,size=(380 ,100),
                          style=wx.SUNKEN_BORDER)
        self.allfilepath = musiclist
        self.playlist = playlist
        self.newfilepaths = []
        self.newfilenames = []
        self.count = 0
        self.preIndex = 0
        self.curIndex = 0
        self.nextIndex = 0
        self.volume = 0.0
        self.parser = ConfigParser.ConfigParser()
        self.initConfig()
        self.mc = MediaCtrl(self ,style=wx.SIMPLE_BORDER ,szBackend=wx.media.MEDIABACKEND_WMP10)
        self.createSlider()
        self.createButton()
        self.bindEvents()
        self.createTimer()
        self.startPlayMusic()

    def startPlayMusic(self):
        self.LoadFile(self.allfilepath[self.curIndex])

    def initConfig(self):
        self.parser.read('config.conf')
        self.count = int(self.parser.get('Index' ,'count'))
        self.preIndex = int(self.parser.get('Index', 'preIndex'))
        self.curIndex = int(self.parser.get('Index', 'curIndex'))
        self.nextIndex = int(self.parser.get('Index', 'nextIndex'))
        self.workingdir = self.parser.get('Other' ,'LastOpenDir')
        self.volume = self.parser.get('Other' ,'volume')
        self.lastvolume =  self.volume

    def createSlider(self):
        self.curmusic = wx.StaticText(self ,label='test' ,size=(300 ,-1) ,pos=(0 ,5)
                                      ,style=wx. ALIGN_CENTRE |wx.ST_NO_AUTORESIZE)
        self.progress = wx.StaticText(self ,label='00:00' ,pos=(140 ,25))
        self.slider = wx.Slider(self ,wx.NewId() ,pos=(0 ,40) ,size=(300 ,-1))
        self.slider.SetToolTipString(u'播放进度')
        self.volume_slider = wx.Slider(self ,wx.NewId() ,pos=(320 ,0) ,style=wx. SL_VERTICAL |wx.SL_INVERSE)
        self.volume_slider.SetRange(0 ,100)
        self.volume_slider.SetValue(30)
        self.volume_slider.SetToolTipString(u'音量:%d%%' %self.volume_slider.GetValue())

    def createButton(self):
        self.stop_btn = wx.Button(self, wx.NewId(), label=u'停止', pos=(10, 65), size=(45, 24))
        self.play_btn = wx.Button(self, wx.NewId(), label=u'播放', pos=(60, 65), size=(45, 24))
        self.pause_btn = wx.Button(self, wx.NewId(), label=u'暂停', pos=(110, 65), size=(45, 24))
        self.pre_btn = wx.Button(self, wx.NewId(), label=u'上一首', pos=(160, 65), size=(45, 24))
        self.next_btn = wx.Button(self, wx.NewId(), label=u'下一首', pos=(210, 65), size=(45, 24))
        self.open_btn = wx.Button(self, wx.NewId(), label=u'打开', pos=(260, 65), size=(45, 24))

    #        self.volume_btn = wx.Button(self,wx.NewId(),label=u'立体声',pos=(260,18),size=(45,20))

    def bindEvents(self):
        self.stop_btn.Bind(wx.EVT_BUTTON, self.OnStop)
        self.play_btn.Bind(wx.EVT_BUTTON, self.OnPlay)
        self.pause_btn.Bind(wx.EVT_BUTTON, self.OnPause)
        self.pre_btn.Bind(wx.EVT_BUTTON, self.OnPre)
        self.next_btn.Bind(wx.EVT_BUTTON, self.OnNext)
        self.slider.Bind(wx.EVT_SLIDER, self.OnSeek)
        self.volume_slider.Bind(wx.EVT_SCROLL, self.ChangeVolume)
        self.open_btn.Bind(wx.EVT_BUTTON, self.OnOpen)
        #        self.volume_btn.Bind(wx.EVT_BUTTON,self.OnVolume)
        self.mc.Bind(wx.media.EVT_MEDIA_LOADED, self.OnMediaLoaded)
        self.mc.Bind(wx.media.EVT_MEDIA_PLAY, self.OnMediaPlay)
        self.mc.Bind(wx.media.EVT_MEDIA_FINISHED, self.OnMediaFinished)

    def createTimer(self):
        self.slider_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onUpdateSlider, self.slider_timer)
        self.slider_timer.Start(100)
        self.text_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.onUpdateText, self.text_timer)

        # stop the song

    def OnStop(self, event):
        self.mc.Stop()

        # play the song

    def OnPlay(self, event):
        self.Play()

        # pause the song

    def OnPause(self, event):
        self.mc.Pause()

        # play the previous song

    def OnPre(self, event):
        self.mc.Stop()
        self.LoadFileByIndex(self.preIndex)

        # stop the next song

    def OnNext(self, event):
        self.mc.Stop()
        self.LoadFileByIndex(self.nextIndex)

    #    def OnVolume(self,event):
    #        if self.volume_btn.GetLabel() == u'立体声':
    #            self.volume_slider.SetValue(0)
    #            self.setVolumeAndTip()
    #            self.volume_btn.SetLabel(u'静音')
    #        else:
    #            self.volume_slider.SetValue(self.lastvolume)
    #            self.setVolumeAndTip()
    #            self.volume_btn.SetLabel(u'立体声')
    #
    # play the spcified position of the song
    def OnSeek(self, event):
        offset = self.slider.GetValue()
        self.mc.Seek(offset)

    def OnMediaLoaded(self, event):
        self.Play()
        self.curmusic.SetLabel(os.path.basename(self.allfilepath[self.curIndex])[:-4])
        self.text_timer.Start(1000)

    def OnMediaPlay(self, event):
        showpanel = self.GetParent().GetWindow2()
        showpanel.setMusicFocus(self.curIndex)

    def OnMediaFinished(self, event):
        self.progress.SetLabel('00:00')
        self.text_timer.Stop()
        if self.count > 0:
            self.curIndex = (self.curIndex + 1) % self.count
        self.refreshIndex(0)
        self.LoadFile(self.allfilepath[self.curIndex])

    def OnOpen(self, event):
        dlg = wx.FileDialog(
            self, message='Choose a music file...',
            defaultDir=self.workingdir,
            defaultFile='',
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR)
        if dlg.ShowModal() == wx.ID_OK:
            self.newfilepaths = dlg.GetPaths()
            self.curIndex = self.count
            self.count += len(self.newfilepaths)
            self.refreshIndex(0)
            self.newfilenames = dlg.GetFilenames()
            self.refreshMusicList(self.newfilepaths)
            os.chdir(self.workingdir)  # change the working directory to the project
            self.save2File(self.newfilepaths)
            self.LoadFile(self.newfilepaths[0])
            showpanel = self.Parent.GetWindow2()
            showpanel.insert2ListCtrl(self.newfilenames)
            self.newfilepaths = []
            self.newfilenames = []
        dlg.Destroy()

    def LoadFile(self, path):
        if not self.mc.Load(path):
            wx.MessageBox("Unable to load %s: Unsupported format?" % path, "ERROR", wx.ICON_ERROR | wx.OK)
        else:
            self.mc.SetVolume(0.3)

    def LoadFileByIndex(self, index):
        self.curIndex = index
        self.refreshIndex(0)
        self.LoadFile(self.allfilepath[self.curIndex])

    def Play(self):
        # self.mc.SetPlaybackRate(2)
        self.mc.Play()
        self.slider.SetRange(0, self.mc.Length())

    def ChangeVolume(self, event):
        # volume range is 0.0-1.0
        self.setVolumeAndTip()

        # move the silder to show the progress of play music

    def onUpdateSlider(self, evt):
        offset = self.mc.Tell()
        self.slider.SetValue(offset)

    def onUpdateText(self, evt):
        offset = self.mc.Tell() / 1000
        progress_text = '%02d:%02d' % (offset / 60, offset % 60)
        self.progress.SetLabel(progress_text)

    def setVolumeAndTip(self):
        value = self.volume_slider.GetValue()
        self.volume = value / 100.0
        if self.volume != 0:
            self.lastvolume = self.volume
        self.mc.SetVolume(self.volume)
        self.volume_slider.SetToolTipString(u'音量:%d%%' % value)

    def save2File(self, filepathlist):
        f = open(self.playlist, 'a')
        for filepath in filepathlist:
            f.write(filepath + '\n')
        f.close()

    def isEmpty(self):
        f = open(self.mlistfile)
        text = f.readline()
        f.close()
        if not text:
            return True
        else:
            return False

    def refreshMusicList(self, filepathlist):
        for filepath in filepathlist:
            self.allfilepath.append(filepath)

    def refreshIndex(self, mode):
        """
        mode:the play mode,like recyle,order or random
        """
        if mode == 0:
            self.refreshIndexInMode0()
        elif mode == 1:
            self.refreshIndexInMode1()
        elif mode == 2:
            self.refreshIndexInMode2()

    def refreshIndexInMode0(self):
        """
        mode 0:the recyle mode
        """
        if self.count == 1:
            self.preIndex = 0
            self.curIndex = 0
            self.nextIndex = 0
            # deal with that the selected item is last one
        elif self.curIndex + 1 == self.count:
            self.nextIndex = 0
            self.preIndex = self.curIndex - 1
            # deal with that the selected item is first one
        elif self.curIndex == 0:
            self.preIndex = self.count - 1
            self.nextIndex = self.curIndex + 1
        else:
            self.nextIndex = self.curIndex + 1
            self.preIndex = self.curIndex - 1

    def refreshIndexInMode1(self):
        pass

    def refreshIndexInMode2(self):
        pass

    def __del__(self):
        self.parser.read('Config.conf')
        self.parser.set('Index', 'count', self.count)
        self.parser.set('Index', 'preIndex', self.preIndex)
        self.parser.set('Index', 'curIndex', self.curIndex)
        self.parser.set('Index', 'nextIndex', self.nextIndex)
        self.parser.set('Other', 'LastOpenDir', self.workingdir)
        self.parser.write(open("Config.conf", "w"))