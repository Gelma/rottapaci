# Rottapaci

* Project URL      : https://github.com/Gelma/rottapaci
* License          : GPL3
* Author           : Andrea Gelmini (andrea.gelmini@gelma.net)

## Dependencies

* Linux kernel with Inotify enabled
* Python ≥ 2.6
* [python-magic](https://github.com/ahupp/python-magic)
* [python-pynotify](https://github.com/seb-m/pyinotify/wiki)

## Install

### Get the git repository:

    $ git clone git://github.com/Gelma/rottapache.git

### and run it to have some help:

    $ ./rottapaci.py -h

## What's up, doc?

Rottapaci is a quick&dirty way to detect PHP break in.
It keeps an eye on what happens in the Apache DocumentRoot of your site.
If a suspicious file appears, it complains.

### Long story
When a file is created/moved in your site Apache DocumentRoot, it:
* checks white list filename (for files to ignore by name)
* checks file type (via file utility)
* checks if is a good known file
* if there something like a C file, it shouts via mail, chat, web, syslog
