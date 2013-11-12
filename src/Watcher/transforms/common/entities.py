#!/usr/bin/env python

from canari.maltego.message import Entity, EntityField, EntityFieldType, MatchingRule

__author__ = 'catalyst256'
__copyright__ = 'Copyright 2013, Watcher Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'catalyst256'
__email__ = 'catalyst256@gmail.com'
__status__ = 'Development'

__all__ = [
    'WatcherEntity'
]

class WatcherEntity(Entity):
    _namespace_ = 'Watcher'

class Interface(WatcherEntity):
    pass

@EntityField(name='Watcher.pktcount', propname='pktcount', displayname='Pkt Count', type=EntityFieldType.String)
class MonitorInterface(WatcherEntity):
    pass

@EntityField(name='Watcher.rssi', propname='aprssi', displayname='RSSI', type=EntityFieldType.String)
@EntityField(name='Watcher.bssid', propname='apbssid', displayname='BSSID', type=EntityFieldType.String)
@EntityField(name='Watcher.channel', propname='apchannel', displayname='Channel', type=EntityFieldType.String)
@EntityField(name='Watcher.encryption', propname='apencryption', displayname='Encryption', type=EntityFieldType.String)
@EntityField(name='Watcher.apmoninterface', propname='apmoninterface', displayname='Monitor Interface', type=EntityFieldType.String)
class AccessPoint(WatcherEntity):
    pass

@EntityField(name='Watcher.cmac', propname='cmac', displayname='MAC Addr', type=EntityFieldType.String)
@EntityField(name='Watcher.monint', propname='monint', displayname='Monitor Interface', type=EntityFieldType.String)
class SSID(WatcherEntity):
    pass

class WirelessClient(WatcherEntity):
    pass

class Database(WatcherEntity):
    pass

#@EntityField(name='Watcher.monInt', propname='monInt', displayname='Monitor Interface', type=EntityFieldType.String)
