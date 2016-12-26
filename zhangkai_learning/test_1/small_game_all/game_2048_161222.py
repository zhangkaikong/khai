#coding:utf-8
import wx
class MyFrame(wx.Frame):

    def __init__(self,title):
        super(MyFrame,self).__init__(None,title=title,size=(250,250))
        self.InitUI()
        self.Centre()

#init the UI of the frame
    def InitUI(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.equation = ''
        self.textprint = wx.TextCtrl(self,wx.TE_CENTER)
        vbox.Add(self.textprint,flag=wx.EXPAND,border=4)

        gridbox = wx.GridSizer(6,4,4,5)
        labels = ['AC','DEL','pi','CLS','7','8','9','/','4','5','6',
                '*','1','2','3','-','0','.','=','+','(',')','张','凯']

        for label in labels:
            buttonItem = wx.Button(self,label=label)
            self.creatHandler(buttonItem,label)
            gridbox.Add(buttonItem,1,wx.EXPAND)
        vbox.Add(gridbox,proportion=7,flag=wx.EXPAND)

        self.SetSizer(vbox)

    def creatHandler(self,buttonItem,label):
        labels = 'AC DEL CLS ='
        if label not in labels:
            self.Bind(wx.EVT_BUTTON,self.OnAppend,buttonItem)
        elif label == 'AC':
            self.Bind(wx.EVT_BUTTON,self.OnAC,buttonItem)
        elif label == 'DEL':
            self.Bind(wx.EVT_BUTTON,self.OnDel,buttonItem)
        elif label == '=':
            self.Bind(wx.EVT_BUTTON,self.OnTarget,buttonItem)
        elif label == 'CLS':
            self.Bind(wx.EVT_BUTTON,self.OnExit,buttonItem)

    def OnAppend(self,event):
        eventButton = event.GetEventObject()
        label = eventButton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)
    def OnAC(self,event):
        self.equation = ''
        self.textprint.SetValue(self.equation)
    def OnDel(self,event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)
    def OnClose(self,event):
        self.textprint.SetValue('Close')
    def OnTarget(self,event):
        string = self.equation
        try:
            target = eval(string)
            self.equation = str(target)
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            self.equation = ''
            self.textprint.SetValue('尼玛，格式错误！')
    def OnExit(self,event):
        self.Close()

#start showing the frame
app = wx.App()
frame = MyFrame('Khai')
frame.Show()
app.MainLoop()