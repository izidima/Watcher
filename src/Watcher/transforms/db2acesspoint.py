#!/usr/bin/env python
import sys
import sqlite3 as lite
from common.entities import AccessPoint, MonitorInterface
from canari.maltego.message import Field, UIMessage
from canari.framework import configure #, superuser

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2013, Watcher Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


#@superuser
@configure(
    label='Watcher - Map Wireless AP',
    description='Maps an Wireless Access Points',
    uuids=[ 'Watcher.v2.db_2_ap' ],
    inputs=[ ( 'Watcher', MonitorInterface ) ],
    debug=False
)
def dotransform(request, response):

    # Setup the sqlite database connection
    watcher_db = 'Watcher/resources/databases/watcher.db'
    con = lite.connect(watcher_db)

    ap_list = []

    with con:
        cur = con.cursor()
        cur.execute('SELECT * FROM aplist')
        while True:
            row = cur.fetchone()
            if row == None:
                break
            if row not in ap_list:
                ap_list.append(row)

    for ssid, bssid, channel, enc, monint in ap_list:
        e = AccessPoint(ssid)
        e.apbssid = bssid
        e.apchannel = channel
        e.apencryption = enc
        e.apmoninterface = monint
        response += e
    return response
