"""
Fix bug in stream mp3 : MP3codec reading
in transcode this stream with ffmpeg

Author : Senufo 2012 (c)
"""

import xbmcaddon, xbmcplugin, xbmcgui, xbmc
import subprocess, time, sys, os

__addonid__  = 'plugin.audio.radiofrance'
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
objProcess = subprocess.Popen(['/usr/bin/ffmpeg', '-y', '-i',
                url,
                '/tmp/fifo.ogg'])
PID = '%s' % objProcess.pid

time.sleep(5)
listitem = xbmcgui.ListItem('FRANCE INFO')
listitem.setInfo('music', {'Title': 'France Info', 'genre': 'news'})
listitem.setIconImage('icon.png')
listitem.setThumbnailImage('%s/media/icon.png' % __resource__)
listitem.setProperty( "Fanart_Image", '%s/media/fanart.jpg' % __resource__)
xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
time.sleep(10)
objProcess = subprocess.Popen(['%s/lib/json.py' % __resource__, PID])
