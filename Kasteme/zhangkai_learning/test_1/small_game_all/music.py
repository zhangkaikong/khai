import wx
import wx.lib.filebrowsebutton
import mp3play
class MyFrame(wx.Frame):
  def __init__(self, parent, mytitle, mysize):
    wx.Frame.__init__(self, parent, wx.ID_ANY, mytitle,
      size=mysize)
    self.SetBackgroundColour("green")
    panel = wx.Panel(self)
    # mask file browser to look for .wav sound files
    self.fbb = wx.lib.filebrowsebutton.FileBrowseButton(panel,
      labelText="Select a WAVE file:", fileMask="*.mp3")
    self.play_button = wx.Button(panel, wx.ID_ANY, ">> Play")
    self.play_button.Bind(wx.EVT_BUTTON, self.onPlay)
    # setup the layout with sizers
    hsizer = wx.BoxSizer(wx.HORIZONTAL)
    hsizer.Add(self.fbb, 1, wx.ALIGN_CENTER_VERTICAL)
    hsizer.Add(self.play_button, 0, wx.ALIGN_CENTER_VERTICAL)
    # create a border space
    border = wx.BoxSizer(wx.VERTICAL)
    border.Add(hsizer, 0, wx.EXPAND|wx.ALL, 10)
    panel.SetSizer(border)

  def onPlay(self, evt):
    filename = self.fbb.GetValue()
    print filename
    try:
        mp3 = mp3play.load(filename)
        mp3.play()
    except Exception:
      print 'mp3play can\'t run on your operating system'
app = wx.App(0)
# create a MyFrame instance and show the frame
mytitle = "wx.lib.filebrowsebutton and wx.Sound"
width = 600
height = 90
MyFrame(None, mytitle, (width, height)).Show()
app.MainLoop()