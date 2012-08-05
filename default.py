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
# plugin modes
MODE_FILE = 1
MODE_FOLDER = 10

# utility functions
# parse parameters for the menu
def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
                #print "paramDict[%s] = %s " % (paramSplits[0], paramSplits[1])
    return paramDict

# UI builder functions
def show_menu(path, racine='video'):
    ''' Show the plugin menu. '''
    #addFile('France Info', 'Info', 1, "icon.png")
    listitem = xbmcgui.ListItem('FRANCE INFO')
    listitem.setInfo('music', {'Title': 'France Info', 'genre': 'news', 'duration':
                          0})
    listitem.setIconImage('icon.png')
    listitem.setThumbnailImage('%s/media/icon.png' % __resource__)
    url_2 = sys.argv[0] + '?title=' + 'France_Info'  + "&mode=" + '1'

    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url_2,
                                       listitem=listitem, isFolder=False)
#   addFile('France Inter', 'Inter', 1, "icon.png")
    listitem = xbmcgui.ListItem('FRANCE INTER')
    listitem.setInfo('music', {'Title': 'France Inter', 'genre': 'news', 'duration':
                          0})
    listitem.setIconImage('icon.png')
    listitem.setThumbnailImage('%s/media/icon.png' % __resource__)
    url_2 = sys.argv[0] + '?title=' + 'France_Inter' + '&url' + '' + "&mode=" + '1'
    xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url_2,
                                       listitem=listitem, isFolder=False)
    xbmcplugin.endOfDirectory(handle=int(handle), succeeded=True)


# Depending on the mode, call the appropriate function to build the UI.
#On recupere les parametres de la listBox
params = parameters_string_to_dict(sys.argv[2])
handle = sys.argv[1]

if not sys.argv[2]:
    # new start
    path = __addon__.getSetting('dir')
    ok = show_menu(path)
elif int(params['mode']) == MODE_FILE:
    listitem = xbmcgui.ListItem(params['title'])
    print "MODE FILE"
    url = __addon__.getSetting( 'url' )
    objProcess = subprocess.Popen(['/usr/bin/ffmpeg', '-y', '-i',
                url, 
                '/tmp/fifo.ogg'])
    PID = '%s' % objProcess.pid

    time.sleep(5)
    #listitem = xbmcgui.ListItem('FRANCE INFO')
    listitem.setInfo('music', {'Title': 'France Info', 'genre': 'news', 'duration':
                          0})
    listitem.setIconImage('icon.png')
    listitem.setThumbnailImage('%s/media/icon.png' % __resource__)
    xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
    time.sleep(10)
    objProcess = subprocess.Popen(['%s/lib/json.py' % __resource__, PID])

###############################################################################
# BEGIN !
################################################################################

if ( __name__ == "__main__" ):
    try:
        print "=========================================="
        print "  Radiofrance plugin - Version: %s" % __version__
        print "=========================================="
        print

        #params=get_params()
        url = None
        name = None
        mode = None
        print "sys.arg = %s " % sys.argv[ 1 ]
        xbmcplugin.addSortMethod( handle=int( sys.argv[ 1 ] ), 
                                   sortMethod=xbmcplugin.SORT_METHOD_LABEL )
        xbmcplugin.endOfDirectory(int(sys.argv[1]))
    except:
        print "Erreur"

#url = __addon__.getSetting( 'url' )
#objProcess = subprocess.Popen(['/usr/bin/ffmpeg', '-y', '-i',
#                url, 
#                '/tmp/fifo.ogg'])
#PID = '%s' % objProcess.pid

#time.sleep(5)
#listitem = xbmcgui.ListItem('FRANCE INFO')
#listitem.setInfo('music', {'Title': 'France Info', 'genre': 'news', 'duration':
#                          0})
#listitem.setIconImage('icon.png')
#listitem.setThumbnailImage('%s/media/icon.png' % __resource__)
#listitem.setProperty( "Fanart_Image", '%s/media/fanart.jpg' % __resource__)
#listitem.setProperty("duration", '100')
#xbmc.Player().play('/tmp/fifo.ogg', listitem, True)
#time.sleep(10)
#objProcess = subprocess.Popen(['%s/lib/json.py' % __resource__, PID])
