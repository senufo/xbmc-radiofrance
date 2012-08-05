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
def show_menu():
    ''' Show the plugin menu. '''
    for index in range(1, 7): 
        #Recup des url, titre et genre dans settings.xml
        url_rf = __addon__.getSetting( 'url%s' % index )
        title_rf = __addon__.getSetting( 'title%s' % index )
        genre_rf = __addon__.getSetting( 'genre%s' % index )
        logo_rf = __addon__.getSetting( 'logo%s' % index ) 
        li = xbmcgui.ListItem(title_rf)
        
        li.setInfo('music', {'Title': title_rf, 'genre': genre_rf, 'duration':
                                   0})
        #On defini le logo (n'a pas l'air de fonctionner !!)
        li.setIconImage(logo_rf)
        li.setThumbnailImage('%s/media/%s' % (__resource__, logo_rf))
        url_2 = sys.argv[0] + '?title=' + title_rf  + '&url=' + url_rf
        url_2 += '&genre=' + genre_rf  + '&logo=' + logo_rf + '&mode=' + '1'

        xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url_2,
                                       listitem=li, isFolder=False)
    
    xbmcplugin.endOfDirectory(handle=int(handle), succeeded=True)


# Depending on the mode, call the appropriate function to build the UI.
#On recupere les parametres de la listBox
params = parameters_string_to_dict(sys.argv[2])
handle = sys.argv[1]

if not sys.argv[2]:
    # new start
    show_menu()
elif int(params['mode']) == MODE_FILE:
    listitem = xbmcgui.ListItem(params['title'])
    print "MODE FILE"
    url = params['url'] 
    title = params['title']
    genre = params['genre']
    logo = params['logo']
    objProcess = subprocess.Popen(['/usr/bin/ffmpeg', '-y', '-i',
                url, 
                '/tmp/fifo.ogg'])
    PID = '%s' % objProcess.pid

    time.sleep(5)
    #listitem = xbmcgui.ListItem('FRANCE INFO')
    listitem.setInfo('music', {'Title': title, 'genre': 'news', 'duration':
                          0})
    listitem.setIconImage(logo)
    listitem.setThumbnailImage('%s/media/%s' % (__resource__, logo))
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
