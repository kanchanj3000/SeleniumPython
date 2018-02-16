from selenium import webdriver

import wmi

c = wmi.WMI()

for process in c.Win32_Process():
    k = process.ProcessId, process.Name
    print k
