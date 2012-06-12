#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Rottapaci watches your PHP site as a Rottweiler.
   See the README.md for details.

   Copyright 2010-2012 - Andrea Gelmini (andrea.gelmini@gelma.net)

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>."""

# FIX:
#     check for inotify enabled
#     check for inotify resources

import pyinotify, sys

if __name__ == "__main__":
    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm)
    events_to_monitor=pyinotify.IN_CREATE|pyinotify.IN_MODIFY|pyinotify.IN_CLOSE_WRITE
    path_to_monitor=['/tmp/test1','/tmp/test2']

    try:
        wm.add_watch(path_to_monitor, events_to_monitor, quiet=False, rec=True, auto_add=True)
    except pyinotify.WatchManagerError, err:
        print err, err.wmd
        sys.exit()

    notifier.loop()
