#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('UTF8')

alphabet = "abcdefghijklmnopqrstuvwxyz"

emojibet = [('🅰').decode('utf-8'), ('🅱').decode('utf-8'), ('©').decode('utf-8'), ('↩').decode('utf-8'), ('🎼').decode('utf-8'), ('🎏').decode('utf-8'), ('🌊').decode('utf-8'), ('🙌').decode('utf-8'), ('ℹ').decode('utf-8'), ('🎷').decode('utf-8'), ('🎋').decode('utf-8'), ('🕒').decode('utf-8'), ('Ⓜ').decode('utf-8'), ('♑').decode('utf-8'), ('⚙️').decode('utf-8'), ('🅿').decode('utf-8'), ('🔍').decode('utf-8'), ('®️️').decode('utf-8'), ('⚡').decode('utf-8'), ('🌴').decode('utf-8'), ('⛎').decode('utf-8'), ('♈').decode('utf-8'), ('📈').decode('utf-8'), ('⚒').decode('utf-8'), ('✌').decode('utf-8'), ('Ⓩ').decode('utf-8')]

while message != "exit":

    message = raw_input("enter some stuff: ")

    return_message = ''

    for c in message:
        if c in alphabet:
            return_message += emojibet[alphabet.index(c)]
        else:
            return_message += c

    print(return_message)

