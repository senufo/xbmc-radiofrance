"""
Fix bug in stream mp3 : MP3codec reading
in transcode this stream with ffmpeg

Author : Senufo 2012 (c)
"""

import xbmcaddon, xbmcplugin, xbmcgui, xbmc
import subprocess, time, sys, os

# magic; id of this plugin's instance - cast to integer
thisPlugin = int(sys.argv[1])
#add on id - name of addon director y
_id = 'plugin.audio.franceinfo'
__addonid__  = 'plugin.audio.franceinfo'
__addon__ = xbmcaddon.Addon( __addonid__ )
__addonDir__ = __addon__.getAddonInfo( "path" )
__author__     = "Senufo"

__cwd__        = __addon__.getAddonInfo('path')
__version__    = __addon__.getAddonInfo('version')
__language__   = __addon__.getLocalizedString

__profile__    = xbmc.translatePath( __addon__.getAddonInfo('profile') )
__resource__   = xbmc.translatePath( os.path.join( __cwd__, 'resources',
                                                  'lib'))
sys.path.append (__resource__)

url = __addon__.getSetting( 'url' )

print "Ressource = %s " % __resource__
#url = 'http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3'
#url = 'http://radioblagon-serveur3.zik.dj:8010/'
ffmpeg_cmd = '/usr/bin/ffmpeg'
ffmpeg_arg = '-i /tmp/fifo /tmp/foo.ogg'
objProcess = subprocess.Popen(['/usr/bin/ffmpeg', '-y', '-i',
                url,
                '/tmp/fifo.ogg'])
PID = '%s' % objProcess.pid

print "Return code 2 = %s " % objProcess
time.sleep(5)
listitem = xbmcgui.ListItem('FRANCE INFO')
listitem.setInfo('music', {'Title': 'France Info', 'genre': 'news'})
listitem.setIconImage('icon.png')
listitem.setThumbnailImage(
    '/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/icon.png')
listitem.setProperty( "Fanart_Image",
    '/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/fanart.jpg' )
xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
time.sleep(10)
objProcess = subprocess.Popen(
    ['%s/json.py' % __resource__,PID])
print 'FIN FRANCEINFO'
