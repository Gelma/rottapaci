# Rottapaci

* License          : GPL3
* Project URL      : [http://github.com/](http://github.com/)
* Project Wiki     : [http://github.com/](http://github.com/)

## Dependencies

* Linux kernel with Inotify enabled
* Python ≥ 2.6

## Install

### Get the git repository:

    $ git clone

### and run as root:

## What's up, doc?

Rottapaci is a quick&dirty way to detect PHP break in.
It keep an eye on what happens in the Apache DocumentRoot of your site.
If some new file appears, it:
* checks white list filename (for files to ignore by name)
* checks file type (via file utility)
* if there something like a C file, it shouts via mail, chat, web