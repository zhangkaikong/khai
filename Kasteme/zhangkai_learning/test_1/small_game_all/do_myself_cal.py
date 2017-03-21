#coding:utf-8
import wx

class MyCal(wx.Frame):

    def __init__(self,title):
        super(MyCal,self).__init__(None,-1,size=(250,250))
        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.equation = ''
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.textprint = wx.TextCtrl(self,style=wx.TE_LEFT)
        vbox.Add(self.textprint,flag=wx.EXPAND,border = 4)
        gridbox = wx.GridSizer(5,4,5,5)

        labels=['AC','DEL','pi','CLS','7','8','9','/','4','5','6',
                '*','1','2','3','-','0','.','=','+']
        for label in labels:
            buttonItem = wx.Button(self,label=label)
            self.createHandler(buttonItem,label)
            gridbox.Add(buttonItem,1,wx.EXPAND)
        vbox.Add(gridbox,1,flag=wx.EXPAND)
        self.SetSizer(vbox)

    def createHandler(self,buttonItem,label):
        labels = 'AC DEL = CLS'
        if label not in labels:
            self.Bind(wx.EVT_BUTTON,self.OnAppend,buttonItem)
        elif label == 'AC':
            self.Bind(wx.EVT_BUTTON,self.OnAC,buttonItem)
        elif label == 'DEL':
            self.Bind(wx.EVT_BUTTON,self.OnDel,buttonItem)
        elif label == 'CLS':
            self.Bind(wx.EVT_BUTTON,self.OnClose,buttonItem)
        elif label == '=':
            self.Bind(wx.EVT_BUTTON,self.OnTarget,buttonItem)

    def OnAppend(self,event):
        eventButton = event.GetEventObject()
        label = eventButton.GetLabel()
        self.equation += label
        self.textprint.SetValue(self.equation)

    def OnAC(self,event):
        self.textprint.Clear()
        self.equation = ''

    def OnDel(self,event):
        self.equation = self.equation[:-1]
        self.textprint.SetValue(self.equation)

    def OnClose(self,event):
        self.Close()

    def OnTarget(self,event):
        string = self.equation
        try:
            target = eval(string)
            self.equation = str(target)
            self.textprint.SetValue(self.equation)
        except SyntaxError:
            self.textprint.SetValue('格式有误！')
            self.equation = ''


app = wx.App()
myCal = MyCal('Khai')
myCal.Show()
app.MainLoop()

