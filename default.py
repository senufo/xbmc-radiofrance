

import urllib,urllib2,re,xbmcplugin,xbmcgui,httplib,htmllib,xbmc
import subprocess, time

PLUGIN              ='plugin.audio.franceinfo'
VERSION             ='0.1'
USER_AGENT          ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
#mplayer -vo null -ao pcm:file=/tmp/fi.mp3 http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3
#ffmpeg -i /tmp/fifo /tmp/foo.ogg
url = 'http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3'
#url = 'http://radioblagon-serveur3.zik.dj:8010/'
#xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(url)
mplayer_cmd = "/usr/bin/mplayer"
mplayer_arg = "-vo null -ao pcm:file=/tmp/fifo http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3"
ffmpeg_cmd = '/usr/bin/ffmpeg'
ffmpeg_arg = '-i /tmp/fifo /tmp/foo.ogg'
print "%s, %s " % (mplayer_cmd,mplayer_arg)
return_code = subprocess.check_call([mplayer_cmd, mplayer_arg] , shell=True)
print "Return code = %s " % return_code
return_code = subprocess.call([ffmpeg_cmd, ffmpeg_arg])
#return_code = subprocess.call([ffmpeg_cmd, '-y','-i',
#                               'http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3',
#                              '/tmp/foo.ogg', '&'])
return_code = subprocess.Popen(['/usr/bin/ffmpeg', '-y','-i',
                               'http://mp3.live.tv-radio.com/franceinfo/all/franceinfo.mp3',
                              '/tmp/fifo.ogg'])
PID = '%s' % return_code.pid

print "Return code 2 = %s " % return_code
time.sleep(10)
listitem = xbmcgui.ListItem('FRANCE INFO')
listitem.setInfo('music', {'Title': 'France Info','genre': 'news'})
listitem.setIconImage('icon.png')
listitem.setThumbnailImage('/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/icon.png')
listitem.setProperty( "Fanart_Image",
                     '/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/fanart.jpg' )
#xbmc.Player( xbmc.PLAYER_CORE_MPLAYER ).play('/tmp.fifo.ogg', listitem, True)
xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
time.sleep(10)
return_code = subprocess.Popen(['/home/henri/Sources/Video/xbmc/addons/github/plugin.audio.franceinfo/json.py',PID])
#xbmc.Player().play('/tmp.fifo.ogg', listitem, True)
#xbmc.Player().play('/tmp/fifo.ogg')
print 'FIN FRANCEINFO'
