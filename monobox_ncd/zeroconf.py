#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GNU General Public Licence (GPL)
# 
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 59 Temple
# Place, Suite 330, Boston, MA  02111-1307  USA
#
# Copyright (c) 2015 by OXullo Intersecans / bRAiNRAPERS

from __future__ import unicode_literals

import logging
import avahi
import dbus

logger = logging.getLogger(__name__)

class ZeroConf(object):
    def __init__(self, name, port, stype='_http._tcp', domain='', host='', text=''):
        self.name = name
        self.stype = stype
        self.domain = domain
        self.host = host
        self.port = port
        self.text = text
        self.group = None

        logger.info('Avahi interface available and ready to announce')

    def publish(self):
        bus = dbus.SystemBus()
        server = dbus.Interface(bus.get_object(avahi.DBUS_NAME, avahi.DBUS_PATH_SERVER),
                avahi.DBUS_INTERFACE_SERVER)

        g = dbus.Interface(bus.get_object(avahi.DBUS_NAME, server.EntryGroupNew()),
                avahi.DBUS_INTERFACE_ENTRY_GROUP)

        g.AddService(avahi.IF_UNSPEC, avahi.PROTO_UNSPEC, dbus.UInt32(0),
                self.name, self.stype, self.domain, self.host,
                dbus.UInt16(self.port), self.text)

        g.Commit()
        self.group = g

        logger.info('Publishing service %s:%s' % (self.name, self.port))

    def unpublish(self):
        if self.group is not None:
            self.group.Reset()
            self.group = None

            logger.info('Unpublishing service %s:%s' % (self.name, self.port))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    zc = ZeroConf('Monobox test', 5000)
    zc.publish()
    raw_input()
    zc.unpublish()