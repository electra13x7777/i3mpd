#!/usr/bin/python"
#
# File: i3mpd.py
# Author: Alex Barney (electra13x7777)
# Fork of spotify.py by firatakandere
#
# Description: Fork of spotify.py that aims to add more functionality

import dbus
import os
import sys

try:
    bus = dbus.SessionBus()

    # Spotify Player
    spotify = bus.get_object("org.mpris.MediaPlayer2.spotify", "/org/mpris/MediaPlayer2")


    if os.environ.get('BLOCK_BUTTON'):
        control_iface = dbus.Interface(spotify, 'org.mpris.MediaPlayer2.Player')
        if (os.environ['BLOCK_BUTTON'] == '1'):
            control_iface.Previous()
        elif (os.environ['BLOCK_BUTTON'] == '2'):
            control_iface.PlayPause()
        elif (os.environ['BLOCK_BUTTON'] == '3'):
            control_iface.Next()

    spotify_iface = dbus.Interface(spotify, 'org.freedesktop.DBus.Properties')
    props = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Metadata')

    # Update PlaybackStatus
    pbstate = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'PlaybackStatus')
    pbtn = ''

    if(pbstate == 'Paused'):
        pbtn = ' (⏵) '
    elif(pbstate == 'Playing'):
        pbtn = ' (⏸) '
    else:
        pbtn = ' (⏹) '

    # Construct Position Bar
    #songlen = probs['mpris:Track_Id']
    #pos = spotify_iface.Get('org.mpris.MediaPlayer2.Player', 'Position')

    # Wrapping Text
    text = str(props['xesam:album']) + ' - ' + str(props['xesam:title'])
    #sfile = open("~/.config/i3blocks/i3mpd.txt", 'r+')
    #n = int(sfile.readline())
    #sfile.close()
    aas = str(props['xesam:artist'][0]) + ' : ' + text

    if (sys.version_info > (3, 0)):
        print('❲ ⏮ ' + pbtn + '⏭ ❳  ' + aas)
    else:
        print(props['xesam:artist'][0] + pbtn + props['xesam:title']).encode('utf-8')
    exit

except dbus.exceptions.DBusException:
    exit



