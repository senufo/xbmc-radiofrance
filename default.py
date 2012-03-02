"""
Fix bug in stream mp3 : MP3codec reading
in transcode this stream with ffmpeg

Author : Senufo 2012 (c)
"""

import xbmcaddon, xbmcplugin, xbmcgui, xbmc
import subprocess, time, sys, os

__addonid__  = 'plugin.audio.franceinfo'
__addon__ = xbmcaddon.Addon( __addonid__ )
__addonDir__ = __addon__.getAddonInfo( "path" )
__author__     = "Senufo"

__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

__profile__    = xbmc.translatePath( __addon__.getAddonInfo('profile') )
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources'))
sys.path.append (__resource__)

url = __addon__.getSetting( 'url' )
player = __addon__.getSetting( 'player' )
if 'ffmpeg' in player:
    objProcess = subprocess.Popen([player, '-y', '-i',
                url,
                '/tmp/fifo.ogg'])
elif 'vlc' in player:
    objProcess = subprocess.Popen([player, '-I dummy', '-v', url,
                       '--sout', 
                       '#transcode{acodec=vorb}:standard{access=file,dst=/tmp/fifo.ogg,mux=ffmpeg}'
                       ])

PID = '%s' % objProcess.pid
print "PID = %s" % PID
time.sleep(5)
listitem = xbmcgui.ListItem('FRANCE INFO')
listitem.setInfo('music', {'Title': 'France Info', 'genre': 'news'})
listitem.setIconImage('icon.png')
listitem.setThumbnailImage('%s/media/icon.png' % __resource__)
listitem.setProperty( "Fanart_Image", '%s/media/fanart.jpg' % __resource__)
xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
time.sleep(10)
objProcess = subprocess.Popen(['%s/lib/json.py' % __resource__, PID])
