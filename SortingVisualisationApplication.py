import matplotlib.pyplot as plt
import wxPython
from wx import wx


class SortingApp(wx.App):
    def OnInit(self):
        self.frame = SortingFrame


class SortingFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title)

        self.panel = wx.Panel(self)
