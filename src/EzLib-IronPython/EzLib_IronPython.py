import clr
clr.AddReference('System.Drawing')
clr.AddReference('System.Windows.Forms')
clr.AddReference('Ezlib')

from EZLib import *
from System.Drawing import *
from System.Windows.Forms import *


class MyForm(Form):
    def __init__(self):
        # Create child controls and initialize form
        pass


Application.EnableVisualStyles()
Application.SetCompatibleTextRenderingDefault(False)

form = MyForm()
#im not the best at Python
settings = EzLibSettings()
settings.AntiDebug=False
settings.AntiSuspend=False
settings.AntiDump=False 
settings.ProcessShield=True
settings.RealTimeInterval=2

Initialize("JiThi7WwND", "1.0.0", settings)
Application.Run(Forms.AuthenticationForm(form))
