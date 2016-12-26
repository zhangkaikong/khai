#!/usr/bin python
# -*-coding:utf-8 -*-

import wx
import ConfigParser
import os.path
from Operation import OperationPanel
from Show import ShowPanel


class MainFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, title='music player', size=(380, 700),
                          style=wx.DEFAULT_FRAME_STYLE & (~wx.MAXIMIZE_BOX) & (~ wx.RESIZE_BORDER))

        self.parser = ConfigParser.ConfigParser()
        self.playlist = None
        self.musiclist = []
        self.musicnames = []
        self.initPlayList()
        self.initMusicList()

        self.splitter = wx.SplitterWindow(self)
        self.operationPanel = OperationPanel(self.splitter, wx.NewId(), self.playlist, self.musiclist)
        self.showPanel = ShowPanel(self.splitter, wx.NewId(), self.musicnames)
        self.splitter.SplitHorizontally(self.operationPanel, self.showPanel, 100)
        self.splitter.SetMinimumPaneSize(100)
        self.initMenuBar()

    def initPlayList(self):
        self.parser.read('config.conf')
        self.playlist = str(self.parser.get('PlayList', 'PlayListDir')) + "/" + str(
            self.parser.get('PlayList', 'lastPlayList'))

    def initMusicList(self):
        f = open(self.playlist)
        self.musiclist = [x[:-1] for x in f.readlines()]
        f.close()
        self.musicnames = [os.path.basename(x) for x in self.musiclist]

    def initAddMenu(self):
        self.addMenu = wx.Menu()
        self.addFileId = wx.NewId()
        self.addDirId = wx.NewId()
        title_list = [u'文件', u'文件夹']
        self.appendMenuItem(self.addMenu, [self.addFileId, self.addDirId], title_list)

    def initDelMenu(self):
        self.delMenu = wx.Menu()
        self.delSelId = wx.NewId()
        self.delDuplicateId = wx.NewId()
        self.delErrId = wx.NewId()
        self.delAllId = wx.NewId()
        self.delPhyicalId = wx.NewId()
        title_list = [u'选中的文件', u'重复的文件', u'错误的文件', '', u'全部删除', '', u'物理删除']
        self.appendMenuItem(self.delMenu,
                            [self.delSelId, self.delDuplicateId, self.delErrId, 'separator', self.delAllId, 'separator',
                             self.delPhyicalId],
                            title_list)

    def initPlayListMenu(self):
        self.playlistMenu = wx.Menu()
        self.newPlayListId = wx.NewId()
        self.addPlayListId = wx.NewId()
        self.openPlayListId = wx.NewId()
        self.savePlayListId = wx.NewId()
        self.delPlayListId = wx.NewId()
        self.saveAllPlayListId = wx.NewId()
        title_list = [u'新建列表', u'添加列表', u'打开列表', u'保存列表', u'删除列表', '', u'保存所有列表']
        self.appendMenuItem(self.playlistMenu,
                            [self.newPlayListId, self.addPlayListId, self.openPlayListId, self.savePlayListId,
                             self.delPlayListId, 'separator', self.saveAllPlayListId],
                            title_list)

    def initSortMenu(self):
        self.sortMenu = wx.Menu()
        self.sortByFileNameId = wx.NewId()
        self.sortByFilePathId = wx.NewId()
        self.sortByFileTypeId = wx.NewId()
        title_list = [u'按文件名', u'按文件路径', u'按文件类型']
        self.appendMenuItem(self.sortMenu,
                            [self.sortByFileNameId, self.sortByFilePathId, self.sortByFileTypeId],
                            title_list)

    def initFindMenu(self):
        self.findMenu = wx.Menu()
        self.fastLocateId = wx.NewId()
        self.findMusicId = wx.NewId()
        title_list = [u'快速定位', u'查找歌曲']
        self.appendMenuItem(self.findMenu,
                            [self.fastLocateId, self.findMusicId],
                            title_list)

    def initModeMenu(self):
        self.modeMenu = wx.Menu()
        self.single = wx.NewId()
        self.singleCycle = wx.NewId()
        self.sequence = wx.NewId()
        self.cycle = wx.NewId()
        self.random = wx.NewId()
        title_list = [u'单曲播放', u'单曲循环', u'顺序播放', u'循环播放', u'随机播放']
        self.appendMenuItem(self.modeMenu,
                            [self.single, self.singleCycle, self.sequence, self.cycle, self.random],
                            title_list)

    def appendMenuItem(self, menu, id_list, title_list):
        length = len(id_list)
        for i in range(length):
            if id_list[i] == 'separator':
                menu.AppendSeparator()
            else:
                menu.Append(id_list[i], title_list[i])

    def append2MenuBar(self, menu_list, title_list):
        length = len(menu_list)
        for i in range(length):
            self.menuBar.Append(menu_list[i], title_list[i])

    def initMenu(self):
        self.initAddMenu()
        self.initDelMenu()
        self.initPlayListMenu()
        self.initSortMenu()
        self.initFindMenu()
        self.initModeMenu()

    def initMenuBar(self):
        self.initMenu()
        self.menuBar = wx.MenuBar()
        self.append2MenuBar(
            [self.addMenu, self.delMenu, self.playlistMenu, self.sortMenu, self.findMenu, self.modeMenu],
            [u'添加', u'删除', u'播放列表', u'排序', u'查找', u'播放模式'])
        self.SetMenuBar(self.menuBar)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MainFrame(parent=None, id=wx.NewId())
    frame.Show()
    app.MainLoop()