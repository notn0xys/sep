import js
from pyscript import document
from pyodide.ffi import create_proxy
from datetime import datetime 
from abc import ABC, abstractmethod 

def getTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S")
class NotificationWidget(Absrac):

