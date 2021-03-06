#!/usr/bin/env python
## Copyright 2012, En7788.com, Inc. All rights reserved.
##
## FormUI is a easy used GUI framwork for python, which is based on wxpython.
## FormUI is a free software: you can redistribute it and/or modify it under
## the terms of version 3 of the GNU Lesser General Public License as
## published by the Free Software Foundation.
##
## You should have received a copy of the GNU Lesser General Public License
## along with AndBug.  If not, see <http://www.gnu.org/licenses/>.

import sys
sys.path.append('../')

from FormUI import *
import os

builder = Builder()

#laod Layout

#builder.loadLayout('demo_menu.xml')
#builder.mergeLayout('demo_common.xml')
#builder.mergeLayout('demo_others.xml')
builder.loadLayout('demo.xml')

#Setup Handler
def OkButtonHandler(windowHandler, handlerPara):
    print(handlerPara.getEventId() + ":" + handlerPara.getEventType())
    valueList = handlerPara.valueList
    for k, v in valueList.iteritems():
        print "result[%s]=" % k, v
    windowHandler.update(builder,True)
    windowHandler.closeWindow()
builder.setCtrlHandler('id_ok', OkButtonHandler)

def cancelButtonHandler(windowHandler, handlerPara):
    windowHandler.closeWindow()
builder.setCtrlHandler('id_cancel', cancelButtonHandler)


def button_handler(windowHandler, handlerPara):
    #windowHandler.setValue('id_text', 'button onclick')
    #ret = windowHandler.confirmMessageBox("ok button click", "title")
    #windowHandler.enableCtrl('id_multi_files', False)
    #windowHandler.highlightItem('id_multi_files')
    builder.setCtrlAttribute('id_text', 'value', 'update builder')
    windowHandler.update(builder,True)
builder.setCtrlHandler('id_button', button_handler)

builderFind = Builder()
builderFind.loadLayout('findgui.xml')
def findOk(windowHandler, handlerPara):
    windowHandler.closeWindow()
builderFind.setCtrlHandler('id_btn_search', findOk)

def button_findgui_handler(windowHandler, handlerPara):
    state, valueList = windowHandler.showForm(builderFind,True)
    print valueList
builder.setCtrlHandler('id_button_findgui', button_findgui_handler)

def menu_handler(windowHandler, handlerPara):
    windowHandler.closeWindow()
builder.setCtrlHandler('id_menu', menu_handler)

def onlist(windowHandler, handlerPara):
    print(handlerPara.getEventType()+":" +handlerPara.getValue('id_list'))
builder.setCtrlHandler('id_list', onlist)

#Show FormUI
valueList = FormUI.loadCachedValue(os.path.expanduser('~') + "/.demo.cfg")
builder.updateValue(valueList)
formUI = FormUI(builder)
formUI.show()
formUI.saveCachedValue(os.path.expanduser('~') + "/.demo.cfg")
