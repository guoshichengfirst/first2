import wx
app=wx.App()
win=wx.Frame(None,title='calculate',size=(500,600))
pan=wx.Panel(win)
result=wx.TextCtrl(pan)
bt1=wx.Button(pan,label='1')
bt2=wx.Button(pan,label='2')
bt3=wx.Button(pan,label='3')
bt4=wx.Button(pan,label='4')
bt5=wx.Button(pan,label='5')
bt6=wx.Button(pan,label='6')
bt7=wx.Button(pan,label='7')
bt8=wx.Button(pan,label='8')
bt9=wx.Button(pan,label='9')
bt11=wx.Button(pan,label='+')
bt12=wx.Button(pan,label='-')
bt13=wx.Button(pan,label='*')
bt14=wx.Button(pan,label='/')
bt15=wx.Button(pan,label='=')
bt16=wx.Button(pan,label='0')
bt17=wx.Button(pan,label='clear')
bt18=wx.Button(pan,label='back')
def bt1event(event):
    result.WriteText(bt1.Label)
bt1.Bind(wx.EVT_BUTTON,bt1event)
def bt2event(event):
    result.WriteText(bt2.Label)
bt2.Bind(wx.EVT_BUTTON,bt2event)

def bt3event(event):
    result.WriteText(bt3.Label)
bt3.Bind(wx.EVT_BUTTON,bt3event)

def bt4event(event):
    result.WriteText(bt4.Label)
bt4.Bind(wx.EVT_BUTTON,bt4event)

def bt5event(event):
    result.WriteText(bt5.Label)
bt5.Bind(wx.EVT_BUTTON,bt5event)

def bt6event(event):
    result.WriteText(bt6.Label)
bt6.Bind(wx.EVT_BUTTON,bt6event)

def bt7event(event):
    result.WriteText(bt7.Label)
bt7.Bind(wx.EVT_BUTTON,bt7event)

def bt8event(event):
    result.WriteText(bt8.Label)
bt8.Bind(wx.EVT_BUTTON,bt8event)

def bt9event(event):
    result.WriteText(bt9.Label)
bt9.Bind(wx.EVT_BUTTON,bt9event)

def bt11event(event):
    result.WriteText(bt11.Label)
bt11.Bind(wx.EVT_BUTTON,bt11event)

def bt12event(event):
    result.WriteText(bt12.Label)
bt12.Bind(wx.EVT_BUTTON,bt12event)

def bt13event(event):
    result.WriteText(bt13.Label)
bt13.Bind(wx.EVT_BUTTON,bt13event)

def bt14event(event):
    result.WriteText(bt14.Label)
bt14.Bind(wx.EVT_BUTTON,bt14event)

def bt15event(event):
    f=result.GetValue()
    dd=eval(f)
    result.SetValue(str(dd))    
bt15.Bind(wx.EVT_BUTTON,bt15event)

def bt16event(event):
    result.WriteText(bt16.Label)
bt16.Bind(wx.EVT_BUTTON,bt16event)

def bt17event(event):
    result.Clear()
bt17.Bind(wx.EVT_BUTTON,bt17event)

def bt18event(event):
    s=result.GetValue()
    result.Remove(s.index(s[-2]),s.index(s[-1]))
bt18.Bind(wx.EVT_BUTTON,bt18event)

box1=wx.BoxSizer()
box1.Add(result,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box2=wx.BoxSizer()
box2.Add(bt1,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box2.Add(bt2,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box2.Add(bt3,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box3=wx.BoxSizer()
box3.Add(bt4,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box3.Add(bt5,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box3.Add(bt6,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box4=wx.BoxSizer()
box4.Add(bt7,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box4.Add(bt8,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box4.Add(bt9,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box9=wx.BoxSizer()
box9.Add(bt16,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box9.Add(bt17,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box9.Add(bt18,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box5=wx.BoxSizer(wx.VERTICAL)
box5.Add(box2,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box5.Add(box3,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box5.Add(box4,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box5.Add(box9,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box6=wx.BoxSizer(wx.VERTICAL)
box6.Add(bt11,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box6.Add(bt12,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box6.Add(bt13,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box6.Add(bt14,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box6.Add(bt15,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box7=wx.BoxSizer()
box7.Add(box5,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box7.Add(box6,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box8=wx.BoxSizer(wx.VERTICAL)
box8.Add(box1,proportion=1,flag = wx.EXPAND|wx.ALL,border=1)
box8.Add(box7,proportion=5,flag = wx.EXPAND|wx.ALL,border=1)
pan.SetSizer(box8)
win.Show()
app.MainLoop()
