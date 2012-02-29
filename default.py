"""
Fix bug in stream mp3 : MP3codec reading
in transcode this stream with ffmpeg

Author : Senufo 2012 (c)
"""

import xbmcplugin, xbmcgui, xbmc
import subprocess, time, sys

# magic; id of this plugin's instance - cast to integer
thisPlugin = int(sys.argv[1])
#add on id - name of addon director y
_id = 'plugin.audio.franceinfo'
#resources direc tory
_resdir = "special://home/addons/" + _id + "/resources"
#add our library to python search path
sys.path.append ( _resdir + "/lib/" )

url = 'http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3'
#url = 'http://radioblagon-serveur3.zik.dj:8010/'
ffmpeg_cmd = '/usr/bin/ffmpeg'
ffmpeg_arg = '-i /tmp/fifo /tmp/foo.ogg'
objProcess = subprocess.Popen(['/usr/bin/ffmpeg', '-y', '-i',
                'http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3',
                '/tmp/fifo.ogg'])
PID = '%s' % objProcess.pid

print "Return code 2 = %s " % objProcess
time.sleep(10)
listitem = xbmcgui.ListItem('FRANCE INFO')
listitem.setInfo('music', {'Title': 'France Info', 'genre': 'news'})
listitem.setIconImage('icon.png')
listitem.setThumbnailImage(
    '/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/icon.png')
listitem.setProperty( "Fanart_Image",
    '/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/fanart.jpg' )
#xbmc.Player( xbmc.PLAYER_CORE_MPLAYER ).play('/tmp.fifo.ogg', listitem, True)
xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
time.sleep(10)
objProcess = subprocess.Popen(
    ['/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/json.py',PID])
#xbmc.Player().play('/tmp.fifo.ogg', listitem, True)
#xbmc.Player().play('/tmp/fifo.ogg')
print 'FIN FRANCEINFO'
