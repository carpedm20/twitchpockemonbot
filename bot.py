#-*- coding: utf-8 -*-

import socket
import pywinauto
import time
from pywinauto.application import Application
from pywinauto.findwindows import find_windows

HOST = "199.9.253.199"
PORT = 6667

NICK = 'carpedm20'
PASS = 'oauth:rgfox58xdt1zzi0sblc58odou7nt6i1'
IDENT = 'carpedm20'

REALNAME = "carpedm20"
CHANNEL = "#carpedm20"

irc = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
irc.connect ((HOST, PORT))
# print irc.recv (4096)

irc.send("PASS %s\r\n" % PASS)
irc.send("NICK %s\r\n" % NICK)
irc.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
irc.send("JOIN %s\r\n" % CHANNEL)

readbuffer = ""

app = Application()
#windows = find_windows(title_re=u".*VisualBoy.*")
windows = find_windows(title_re=u".*GameBoy.*")
print windows

if windows:
    w = app.window_(handle = windows[0])
    title_name = w.WindowText()

    # 'Style', 'ClientRects', 'IsEnabled', 'Fonts', 'IsUnicode', 'ContextHelpID', 'IsVisible', 
    # 'Rectangle', 'UserData', 'MenuItems', 'FriendlyClassName', 'ControlCount', 'Texts', 'ExStyle', 'ControlID', 'Class
    prop = pywinauto.controls.HwndWrapper.GetDialogPropsFromHandle(windows[0])[0]



while (1):
    data = irc.recv(1024)
    if data.find ( 'PRIVMSG' ) != -1:
          key = ''
          nick = data.split ( '!' ) [ 0 ].replace ( ':', '' )
          message = ':'.join ( data.split ( ':' ) [ 2: ] ).replace('\r\n','')

          print nick + ':', message
          command = ''.join([i for i in message if not i.isdigit()])

          if command in ['위','up']:
              key = 'up'
          elif command in ['아래','아','down']:
              key = 'down'
          elif command in ['왼쪽','왼','left'] :
              key = 'left'
          elif command in ['오른쪽','오른','오','right']:
              key = 'right'
          elif command[0] in ['a']:
              key = 'a'
          elif command[0] in ['b']:
              key = 'b'
          elif command in ['select']:
              key = 'select'
          elif command in ['start']:
              key = 'start'
        
          cnt = 1
          if message[0:3] in ['위','아','왼','오','a','b']:
              try:
                  cnt = int(message[3:])
              except:
                  cnt = 1
          elif message[0:6] in ['아래','왼쪽','오른']:
              try:
                  cnt = int(message[6:])
              except:
                  cnt = 1
          elif message[0:9] in ['오른쪽']:
              try:
                  cnt = int(message[9:])
              except:
                  cnt = 1

          elif message[0:2] in ['up']:
              try:
                  cnt = int(message[2:])
              except:
                  cnt = 1

          elif message[0:4] in ['down','left']:
              try:
                  cnt = int(message[4:])
              except:
                  cnt = 1

          elif message[0:5] in ['start','right']:
              try:
                  cnt = int(message[5:])
              except:
                  cnt = 1

          elif message[0:6] in ['select']:
              try:
                  cnt = int(message[6:])
              except:
                  cnt = 1

          if cnt > 5:
              cnt = 5

          if key != '':
              print nick + ':', key
              # w.SetFocus();w.TypeKeys("^ljavascript:GameBoyKeyDown{(}'" + key + "'{)};{ENTER}")
              for i in range(cnt):
                  w.SetFocus();w.TypeKeys("kd{(}'" + nick + "','" + key + "'{)};{ENTER}")
                  time.sleep(0.000001)
              # w.TypeKeys("^ljavascript:GameBoyKeyUp{(}'" + key + "'{)};{ENTER}")
