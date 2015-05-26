"""
from distutils.core import setup
import py2exe

setup(windows=['bull.py'])
"""
import os
import site
from distutils.core import setup
import py2exe

packages = site.getsitepackages()

pyqt4images_dll = []
qt_plugins_base_path = '/PyQt4/plugins/imageformats/'
images_dll = ['qjpeg4.dll','qgif4.dll','qico4.dll',
    'qmng4.dll','qsvg4.dll','qtiff4.dll']

for item in packages:
    for dll in images_dll:
        dll_path = '%s%s%s'%(item,qt_plugins_base_path,dll)
        if os.path.exists(dll_path):
            pyqt4images_dll.append(dll_path)

DATA=[('imageformats',pyqt4images_dll)]
setup(windows=[{"script":"bull.py"}], 
    data_files = DATA,
    options={"py2exe":{
        "includes":["sip", "PyQt4.QtNetwork", "PyQt4.QtWebKit", "PyQt4.QtSvg" ],
        "bundle_files":3,
        "compressed":True,
        "xref":True}}, 
    zipfile=None)