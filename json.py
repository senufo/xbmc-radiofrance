#!/usr/bin/python
from pprint import pprint
import simplejson as json

import socket, random
req = {'jsonrpc':'2.0', 'id':str(random.randint(0,100)), 'method':'JSONRPC.Ping'}
s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost",9090))
#s.send(json.dumps(req))
#reponse = s.recv(1024)
#print reponse
#req = {'jsonrpc':'2.0', 'method':'Player.OnPlay'}
#req = {"jsonrpc":"2.0","id":1,"method":"System.GetInfoLabels","params":{"labels":["MusicPlayer.Cover"]}}
#{"jsonrpc":"2.0","method":"Player.OnPlay","params":{"data":{"item":{"type":"movie"},"player":{"playerid":1,"speed":1},"title":""},"sender":"xbmc"}}

#req = {"jsonrpc":"2.0","id":str(random.randint(0,100)),"method":"Player.OnPlay"}
#req = {"jsonrpc": "2.0", "method": "Player.GetActivePlayers", "id":"10"}
req = {"method":"Player.GetItem","id":2097173,"jsonrpc":
       "2.0","params":{"playerid":0,"properties":["title","artist","albumartist","genre","year",
                                                  "rating","album","track","duration","comment",
                                                  "lyrics","playcount","fanart","runtime",
                                                  "streamdetails","thumbnail","file","artistid","albumid"]}}
s.send(json.dumps(req))
reponse = s.recv(2048)
print reponse
print "===================="
#json_data=open('json_data')

data = json.loads(reponse)
pprint(data)
#json_data.close()

print "==> %s " % data["result"]["item"]["file"]
print "==> %s " % data["result"]["item"]["label"]
#data["om_points"]


print reponse[0]
f = open('/tmp/workfile', 'w')
f.write(reponse)
f.close()
