#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
rottapaci.py watches your PHP site as a Rottweiler.

Usage: rottapaci.py [OPTIONS]
OPTIONS are:
   -h, --help   print help
   -p, --path   specify one or more paths to monitor (separeted by space)

   Example: rottapaci.py -p '/var/www/first_site /var/www/secondo_site'

   URL: https://github.com/Gelma/rottapache
   ------

   Copyright 2012 - Andrea Gelmini (andrea.gelmini@gelma.net)

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

# FIX:
#     read file configuration
#     check python version
#     check for inotify enabled
#     check for inotify resources
#     intercept signals like 15
#     log to syslog
#     send analysis to other machine

import atexit, ConfigParser, getopt, multiprocessing, os, sys
import csi

try:
    import pyinotify # https://github.com/seb-m/pyinotify
except:
    sys.exit("Error: I need PyInotify package - https://github.com/seb-m/pyinotify/wiki\n       Debian/Ubuntu: apt-get install python-pyinotify\n       Else: sudo easy_install pyinotify")

def killall_threads():
	"I kill every multiprocessing thread"

	for id in multiprocessing.active_children():
	    id.terminate()

class EventHandler(pyinotify.ProcessEvent):
    "My subclass to manage events"

    def start_check(self, filename):
	multiprocessing.Process(target=csi.EventAnalysis, args=(filename,)).start()

    def process_IN_CLOSE_WRITE(self, event):
	self.start_check(event.pathname)

    def process_IN_MOVED_TO(self, event):
	self.start_check(event.pathname)

def start_watching(paths):
    "Start watching the paths specified in list PATHS"

    if not len(paths): sys.exit("Error: no path to monitor")

    wm = pyinotify.WatchManager()
    handler = EventHandler()
    notifier = pyinotify.Notifier(wm, handler)
    mask = pyinotify.IN_CLOSE_WRITE|pyinotify.IN_MOVED_TO # IN_CLOSE_WRITE implies IN_CREATE and IN_MODIFY

    for path in paths: # just dirs
        if not os.path.isdir(path):
            sys.exit("Error: %s is not a directory" % path)

    paths = [os.path.abspath(dir) for dir in arg.split()]

    try:
        wm.add_watch(paths, mask, quiet=False, rec=True, auto_add=True)
    except pyinotify.WatchManagerError, err:
        print err, err.wmd
        sys.exit(1)

    notifier.loop()

if __name__ == "__main__":

    configuration = ConfigParser.ConfigParser()
    config = configuration.read(['/etc/rottapaci.conf', os.path.join(os.environ["HOME"], '.rottapaci.conf'), 'rottapaci.conf'])
    if not config:
	sys.exit("Error: problems with configuration file")

    paths = []
    try: # parsing command line arguments
        opts, args = getopt.getopt(sys.argv[1:], "hp:", ["help", "path"])
    except getopt.GetoptError, err:
        print str(err) # will print something like "option -a not recognized"
        sys.exit(__doc__)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            sys.exit(__doc__)
        elif opt in ("-p", "--path"):
            paths = [os.path.abspath(dir) for dir in arg.strip().split()]

    # add path from config file
    
    atexit.register(killall_threads)
    p = multiprocessing.Process(target=start_watching, args=(paths,))
    p.start()
    p.join()
