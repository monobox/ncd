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

import logging

import server
import zeroconf

DEBUG = False
PORT = 5000

logger = logging.getLogger(__name__)

def run():
    logging.basicConfig(level=logging.INFO)

    logger.info('Monobox NCD starting up')
    zcs = zeroconf.ZeroConf('Monobox Configuration Panel', PORT)
    zcs.publish()

    try:
        server.app.run(debug=DEBUG, host='0.0.0.0', port=PORT)
    except KeyboardInterrupt:
        zcs.unpublish()
        logger.info('Monobox NCD shutting down')
