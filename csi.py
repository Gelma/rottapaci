# -*- coding: utf-8 -*-
#
# Copyright 2012 - Andrea Gelmini (andrea.gelmini@gelma.net)
# Licensed under the terms of the GPL3 License
# (see README.md for details)
"""
I receive a file, and analyze it
"""

import sys
import logit

try:
    import magic # FIX: add check to be sure about which magic package is loaded
except:
    sys.exit("Error: I need python-magic package - https://github.com/ahupp/python-magic\n       sudo easy_install python-magic")

class EventAnalysis():
    "I receive a filename and check it"

    filename = None

    def __init__(self, filename):
        self.filename = filename

    def run(self):
        logit.log("Start check",self.filename)
        

    # A file can be:
    #   white: I know it's good, I stop check
    #   black: I know it's dangerous, I alert
    #   neutral: I dunno, keep goin', give a warning
    #   with an int: a niceness value
    # check if file still exists
    # whitelist/blacklist by regexp
    # whitelist/blacklist by type
    # whitelist/blacklist by hash

