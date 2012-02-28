

import urllib,urllib2,re,xbmcplugin,xbmcgui,httplib,htmllib,xbmc
import subprocess, time

PLUGIN              ='plugin.audio.franceinfo'
VERSION             ='0.1'
USER_AGENT          ='Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'
# plugin modes
MODE_FIRST = 10
MODE_SECOND = 20

# parameter keys
PARAMETER_KEY_MODE = "mode"

# menu item names
FIRST_SUBMENU = "First Submenu"
SECOND_SUBMENU = "Second Submenu"

# plugin handle
handle = int(sys.argv[1])

# utility functions
def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

def addDirectoryItem(name, isFolder=True, parameters={}):
    ''' Add a list item to the XBMC UI.'''
    li = xbmcgui.ListItem(name)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=isFolder)

# UI builder functions
def show_root_menu():
    ''' Show the plugin root menu. '''
    addDirectoryItem(name=FIRST_SUBMENU, parameters={ PARAMETER_KEY_MODE: MODE_FIRST }, isFolder=True)
    addDirectoryItem(name=SECOND_SUBMENU, parameters={ PARAMETER_KEY_MODE: MODE_SECOND }, isFolder=True)
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)

def show_first_submenu():
    ''' Show first submenu. '''
    for i in range(0, 5):
        name = "%s Item %d" % (FIRST_SUBMENU, i)
        addDirectoryItem(name, isFolder=False)
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)

def show_second_submenu():
    ''' Show second submenu. '''
    for i in range(0, 10):
        name = "%s Item %d" % (SECOND_SUBMENU, i)
        addDirectoryItem(name, isFolder=False)
    xbmcplugin.endOfDirectory(handle=handle, succeeded=True)

# parameter values
params = parameters_string_to_dict(sys.argv[2])
mode = int(params.get(PARAMETER_KEY_MODE, "0"))
print "##########################################################"
print("Mode: %s" % mode)
print "##########################################################"

# Depending on the mode, call the appropriate function to build the UI.
if not sys.argv[2]:
    # new start
    ok = show_root_menu()
elif mode == MODE_FIRST:
    ok = show_first_submenu()
elif mode == MODE_SECOND:
    ok = show_second_submenu()
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


print "Return code 2 = %s " % return_code
time.sleep(10)
listitem = xbmcgui.ListItem('FRANCE INFO')
listitem.setInfo('audio', {'Title': 'France Info'})
#xbmc.Player( xbmc.PLAYER_CORE_MPLAYER ).play('/tmp.fifo.ogg', listitem, True)
xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
#xbmc.Player().play('/tmp.fifo.ogg', listitem, True)
#xbmc.Player().play('/tmp/fifo.ogg')
print 'FIN FRANCEINFO'
