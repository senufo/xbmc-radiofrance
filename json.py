#!/usr/bin/python
"""
Kill ffmpeg when xbmc player stop
"""

import simplejson as json
import socket, sys, time
import subprocess

#Get ffmpeg PID
PID = sys.argv[1]
#Connection au serveur XBMC json PORT 9090
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 9090))
#requete json pour savoir si le player est en fonction
req = {"method":"Player.GetItem", "id":2097173, "jsonrpc":
       "2.0", "params":{"playerid":0,"properties":
                         ["title", "artist", "albumartist", "genre", "year",
                          "rating", "album", "track", "duration", "comment",
                          "lyrics", "playcount", "fanart", "runtime",
                          "streamdetails", "thumbnail", "file", "artistid",
                          "albumid"]}}
s.send(json.dumps(req))
reponse = s.recv(2048)
data = json.loads(reponse)

#Boucle pour attendre la fin du player et tuer ffmpeg
while True:
    s.send(json.dumps(req))
    reponse = s.recv(2048)
    data = json.loads(reponse)

    try:
        if data["result"]["item"]["label"] in "FRANCE INFO":
            print "En cours de lecture"
        else:
            print "Label = %s " % data["result"]["item"]["label"]
        
    except:
        print "C'est fini"
        subprocess.Popen(['kill', '-9', PID])
        exit()
    time.sleep(10)
