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

import cgi
from flask import Flask, render_template, jsonify, request

import netconf

app = Flask(__name__)

intf = netconf.Interface('wlan0')


@app.route('/scan')
def scan():
    aps = intf.scan()

    return render_template('scan.html', aps=aps)

@app.route('/connect', methods=['POST'])
def connect():
    address = request.form['address']

    target_ap = None
    for ap in intf.last_scan:
        if ap.address == address:
            target_ap = ap
            break

    if not target_ap:
        return jsonify({'rc': 1, 'reason': 'Cannot find address %s' % address,
                'ssid': '<not found>'})
    else:
        return jsonify({'rc': 0, 'reason': None, 'ssid': ap.ssid})

@app.route('/')
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

